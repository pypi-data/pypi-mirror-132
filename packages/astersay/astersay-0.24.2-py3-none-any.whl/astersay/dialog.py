#
# Copyright (c) 2020, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the same license as the current project.
#
"""
Функционал для обработки моделей диалогов.
"""
import json
import logging
import re
import subprocess
import wave
from collections import OrderedDict
from datetime import datetime
from gettext import gettext as _, ngettext
from os.path import splitext, basename
from tempfile import NamedTemporaryFile
from time import time, sleep
from threading import Thread
from uuid import uuid4

from astersay.exceptions import AgiError, AgiHangupError, AgiSigpipeError

logger = logging.getLogger(__name__)
log_debug = logger.debug
log_info = logger.info
log_warning = logger.warning
log_error = logger.error


class TextBuffer(list):

    def __init__(self, key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key = key
        # Список индексов зафиксированных текстов.
        self.fixed = []
        # Время финализированного текста, должно сбрасываться предварительным
        # распознаванием.
        self.final = None

    def get_text(self, mode=1):
        """
        Возвращает текст буфера в режимах:
        1 - финальный, 2 - промежуточный, 3 - весь, 4 - весь с разметкой.
        """
        fixed = self.fixed
        if mode == 1:
            L = [x for i, x in enumerate(self) if x and i in fixed]
        elif mode == 2:
            L = [x for i, x in enumerate(self) if x and i not in fixed]
        elif mode == 3:
            L = [x for x in self if x]
        else:
            L = ['%s: %s' % (i + 1, x) for i, x in enumerate(self) if x]
        return '\n'.join(L)

    @property
    def seconds_after_final(self):
        if self.final:
            return time() - self.final
        return 0


def make_say_params(saydata, variables):
    """Возвращает готовые аргументы для метода say()."""
    params = {'text': '', 'escape_digits': '', 'voice': ''}

    if 'voice' in saydata:
        params['voice'] = saydata['voice'] % variables
    elif 'file' in saydata:
        params['voice'] = splitext(saydata['file'])[0] % variables
    elif 'texts' in saydata:
        params['text'] = '|'.join(saydata['texts']) % variables
    else:
        params['text'] = saydata['text'] % variables

    if 'escape_digits' in saydata:
        escape_digits = saydata['escape_digits']
        if not isinstance(escape_digits, str):
            escape_digits = ''.join(map(str, escape_digits))
        params['escape_digits'] = escape_digits

    if 'nonblocking' in saydata:
        params['nonblocking'] = bool(saydata['nonblocking'])

    return params


def make_pause(data, key):
    try:
        pause = float(data.get(key, 0))
    except ValueError:
        pause = 0
    if pause:
        log_debug(_('Основной поток приостановлен. Пауза %s секунд.'), pause)
        sleep(pause)
        log_debug(_('Основной поток продолжен.'))
    return pause


def prepare_answer(answer, export_name, script, variables, source=None):
    export_name_source = export_name + '_source'
    if source is True:
        variables[export_name_source] = answer
    elif source is not None:
        variables[export_name_source] = source

    booleanize = script.get('booleanize')
    convert = script.get('convert')
    if booleanize:
        if booleanize.get('to_lowercase', True):
            answer = answer.lower()
        answer = bool(answer in booleanize['true_list'])
        text_true = booleanize.get('text_true') or _('Да')
        text_false = booleanize.get('text_false') or _('Нет')
        export_name_text = (
            booleanize.get('export_name_text') or
            export_name + '_text'
        )
        variables[export_name_text] = text_true if answer else text_false
    elif convert:
        variables[export_name + '_convert_from'] = answer
        if convert.get('to_lowercase', True):
            answer = answer.lower()
        default = convert.get('default')
        if default is None:
            default = answer
        answer = convert['values'].get(answer, default)
        labels = convert.get('labels')
        if labels and answer in labels:
            variables[export_name + '_label'] = labels[answer]
        names = convert.get('names')
        if names and answer in names:
            variables[export_name + '_name'] = names[answer]
        texts = convert.get('texts')
        if texts and answer in texts:
            variables[export_name + '_text'] = texts[answer]
    # Устанавливаем изменённый текст ответа в главную переменную.
    variables[export_name] = answer


class BaseDialog:
    """Диалог робота с позвонившим на номер абонентом."""
    is_closed = False
    # Значение меняется экземпляром распознавателя в процессе считывания стрима.
    stream_size = 0
    # Значение меняется каждый раз перед вызовом парсеров.
    partials_begin = 0
    # Заполнен в момент воспроизведения голоса.
    _voice = None
    _voice_duration = 0
    _voice_nonblocking = False
    # RMS-значение данных тихого участка звукового потока используется для
    # рассчёта тишины канала и может уменьшаться в процессе работы.
    _silence_rms = 1000
    # Момент начала тишины в Unix-time (целые секунды).
    _silence_from = None
    # Флаг, при установке которого сбрасывается счётчик секунд молчания.
    _reset_silence = False
    # Список истории действий внутри блока (скрипта).
    _blocklog = None

    def __init__(self, agi, settings, stream):
        self.id = str(uuid4())
        self.agi = agi
        self.settings = settings
        self.stream = stream
        self.amplitude = []
        self.silence_seconds = 0

        # Глобальная конфигурация бекендов уровня диалога. В атрибутах
        # `synthesizer` и `recognizer` хранятся экземпляры классов используемые
        # в текущий момент, поэтому нельзя на них ссылаться как на постоянные.
        scheme = settings.dialog_scheme
        self.synthesizer = self.main_synthesizer = settings.get_synthesizer(
            **scheme.get('synthesizer', {}))
        self.recognizer = settings.get_recognizer(
            **scheme.get('recognizer', {}))
        if hasattr(self.recognizer, 'token_manager'):
            self.recognizer.token_manager.update_token()

        self.morphology_processor = settings.get_morphology_processor()
        self.text_buffers = OrderedDict()
        # Словарь для экспортируемых после завершения в Asterisk переменных.
        self.export = OrderedDict()
        # Цепочка исполнения скриптов с их результатами и распознанным текстом.
        self.chain = []

    def make_text_buffer(self, key=None):
        if not key:
            key = len(self.text_buffers)
        text_buffer = TextBuffer(key)
        self.text_buffers[text_buffer.key] = text_buffer
        log_debug(_('Новый текстовый буфер: %s'), key)
        return key

    def get_last_text_buffer(self):
        text_buffers = self.text_buffers
        return text_buffers[list(text_buffers.keys())[-1]]

    def text_to_text_buffer(self, text, fixed=False, text_buffer=None):
        if text_buffer is None:
            text_buffer = self.get_last_text_buffer()
        text = text.strip()
        if not text:
            return
        text_buffer.final = None
        # Первые передварительные результаты не принимаются до заданного
        # ограничения.
        if not fixed:
            recognizer = getattr(self, 'recognizer', None)
            if recognizer and recognizer.partials_counter < self.partials_begin:
                return
        if not text_buffer:
            text_buffer.append(text)
        else:
            text_buffer[-1] = text
        # Для блокировки делаем пустую новую строку, в неё и будет писаться
        # текст в дальнейшем.
        if fixed:
            text_buffer.fixed.append(len(text_buffer) - 1)
            text_buffer.append('')
            text_buffer.final = time()

    def text_from_text_buffer(self, mode=1, text_buffer=None):
        """
        Возвращает текст буфера в режимах:
        1 - финальный, 2 - промежуточный, 3 - весь, 4 - весь с разметкой.
        """
        if text_buffer is None:
            text_buffer = self.get_last_text_buffer()
        return text_buffer.get_text(mode)

    def parse_names(self, mode=1, text_buffer=None):
        """Метод ищет в тексте буфера все имена."""
        # Слова должны быть в оригинальной последовательности.
        text = self.text_from_text_buffer(mode, text_buffer)
        processor = self.morphology_processor
        return processor.parse_names(text), text

    def search_by_buffer(self, regexp, mode=1, text_buffer=None):
        """Метод ищет в тексте буфера по регулярному выражению."""
        text = self.text_from_text_buffer(mode, text_buffer)
        return regexp.search(text), text

    def capture_text(self, stopwords, mode=1, text_buffer=None,
                     second=0, maxsilence=10, minlength=10, startsilence=0):
        """Собирает речь вплоть до выявления каких-либо ограничений."""
        if not text_buffer:
            text_buffer = self.get_last_text_buffer()
        text = self.text_from_text_buffer(mode, text_buffer)
        stop = False
        silence = self.silence_seconds
        if stopwords and stopwords.intersection(text.split(' ')):
            stop = True
            log_debug('Сработало ограничение по стоп-слову.')
        elif not text and startsilence and silence >= startsilence:
            stop = True
            log_debug('Сработало ограничение по изначальной тишине.')
        else:
            _expire = silence >= maxsilence
            _size = len(text) >= minlength
            _final = text_buffer.seconds_after_final > 1
            stop = _expire and _size and _final
            if _expire:
                log_debug('Сработало ограничение по тишине.')
                if _size:
                    log_debug('Сработало ограничение по длине.')
                    if _final:
                        log_debug('Сработало ограничение по финалу '
                                  'распознавания.')
                    else:
                        log_debug('Ожидаем финальное распознавание.')
                else:
                    log_debug('Длина текста недостаточна для завершения.')

        return text, stop

    def text_processing(self, name, mode=1, text_buffer=None):
        """
        Метод отправляет текст буфера в подпроцесс обработчика текста и
        возвращает результат его обработки им.
        """
        text = self.text_from_text_buffer(mode, text_buffer)
        if not text:
            return '', text
        text = text.replace('\n', ' ')
        processor = self.settings.get_processor(name)
        if getattr(self, '_text_processing_processor', '') != processor:
            self._text_processing_processor = processor
            self._text_processing_result = self._text_processing_text = ''
        # Кэшированое значение результата для текста.
        if self._text_processing_text == text:
            return self._text_processing_result, self._text_processing_text

        procname = basename(processor)
        log_debug('> PROCESSOR %s %r', procname, text)
        res = subprocess.run(
            [processor, text],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            # universal_newlines=True,
        )
        if res.returncode:
            result = ''
            log_error(_('Текстовый процессор %r сломан.'), processor)
            log_error('< PROCESSOR %s', res.stderr)
        else:
            result = res.stdout.decode('utf-8').rstrip()
            log_debug('< PROCESSOR %s %r', procname, result)
        self._text_processing_result = result
        self._text_processing_text = text
        return result, text

    def say(self, text: str, voice: str, escape_digits: str, nonblocking=False,
            reset_silense=True, disable_blocklog=False):
        if not text and not voice:
            log_error(_('Текст и файл голоса отсутствуют.'))
            return

        synthesis = 0
        # Здесь "voice" - это путь к файлу без его расширения.
        if voice:
            log_info(_('Голос робота: %s'), voice)
        else:
            log_info(_('Текст робота: %s'), text)
            synthesis_started = time()
            try:
                voice = self.synthesizer.make_voice(text)
            except Exception as e:
                log_error(_('Ошибка синтеза речи.'), exc_info=e)
                return
            synthesis = time() - synthesis_started

        n = 0
        while self._voice and n < 1000:
            log_warning(_('Другой голос %s ещё не завершён.'), self._voice)
            n += 1
            sleep(0.5)

        if self._voice:
            log_warning(_('Заменяем голос %s на новый.'), self._voice)

        self._voice = voice
        with wave.open(voice + '.wav') as f:
            duration = f.getnframes() / f.getframerate()
            log_debug(_('Продолжительность голоса %s секунд.'), duration)
            self._voice_duration = duration

        if nonblocking:
            log_debug(_('Голос отправляется в неблокирующем режиме.'))
        else:
            log_debug(_('Голос отправляется в блокирующем режиме.'))

        def clear_voice():
            if self._voice == voice:
                self._voice = None
                self._voice_duration = 0
                log_debug(_('Голос %s завершён.'), voice)
                # После завершения любой речи робота мы должны сбросить счётчик
                # молчания.
                if reset_silense:
                    self._reset_silence = True

        def runner():
            rest = duration
            while rest > 0 and self._voice == voice:
                sleep(0.5)
                rest -= 0.5
            clear_voice()

        try:
            self.agi.stream_file(voice, escape_digits=escape_digits)
        except AgiSigpipeError:
            self._voice = None
            self._voice_duration = 0
            self.is_closed = True
            log_info(_('Голос не отправлен. Связь разорвана.'))
            return

        thread = Thread(target=runner, daemon=True)
        thread.start()

        if not disable_blocklog:
            self.blocklog(
                'robot', text=text, voice=voice, nonblocking=nonblocking,
                escape_digits=escape_digits, reset_silense=reset_silense,
                synthesis=synthesis, duration=duration)

        self._voice_nonblocking = nonblocking
        if not nonblocking:
            log_debug(_('Останавливаем основной поток на %s секунд.'), duration)
            # Останавливаем основной поток.
            sleep(duration + 0.1)
            # Запускаем гарантированную очистку.
            clear_voice()

    def say_silence(self, conf, index, variables):
        try:
            s = conf['phrases'][index]
            index += 1
        except IndexError:
            s = conf['phrases'][0]
            index = 1
        saydata = {'text': s}
        self.say(**make_say_params(saydata, variables))
        return index

    def calc_silence_seconds(self):
        silence_rms = self._silence_rms
        # Граница тихого участка - это 200% от минимума.
        # Вроде бы смысла нет иметь границу ниже 500 единиц RMS.
        if silence_rms > 250:
            # Уменьшаем минимальное значение.
            for second, rms in self.amplitude:
                if rms < 250:
                    self._silence_rms = silence_rms = 250
                    log_debug(_('Установлен минимальный RMS=250(%d).'), rms)
                    break
                if rms < silence_rms:
                    self._silence_rms = silence_rms = rms
                    log_debug(_('Установлен минимальный RMS=%d.'), rms)

        border = silence_rms * 2
        silence_from = self._silence_from
        for second, rms in reversed(self.amplitude):
            if rms > border:
                self._silence_from = silence_from = second + 1
                break
        if silence_from is None:
            value = 0
        else:
            seconds = int(time()) - silence_from
            value = seconds if seconds > 0 else 0
        self.silence_seconds = value
        if value:
            msg = ngettext(
                'Тишина %d секунду.',
                'Тишина %d секунд.',
                value
            )
            log_debug(msg, value)
        return value

    def has_start_recognize(self):
        if self.is_closed:
            return False
        agi = self.agi
        return not agi.is_sighup and not agi.is_hungup

    def start_recognizing(self):
        log_debug(_('Включаем передачу голоса на распознавание.'))
        # Принудительно сбрасываем кол-во секунд тишины, чтобы при быстром
        # переходе с блока на блок не словить старую паузу.
        self.silence_seconds = 0
        self._silence_from = int(time())
        self.recognizer.pause = False

    def stop_recognizing(self):
        log_debug(_('Отключаем передачу голоса на распознавание.'))
        self.recognizer.pause = True

    @property
    def is_stopped(self):
        if self.is_closed:
            return True
        agi = self.agi
        return agi.is_sighup or agi.is_hungup

    def start(self):
        if getattr(self, '_recognizer_thread', None):
            raise RuntimeError(_('Другой поток распознавания уже запущен.'))
        if not self.text_buffers:
            raise RuntimeError(_('Начальный текстовый буфер удалён.'))

        def calc_silence():
            # От начала и до конца беседы поток голоса абонента анализируется
            # на тишину каждую секунду.
            while self.has_start_recognize():
                if self._reset_silence:
                    # self.amplitude.clear()
                    self._silence_from = int(time())
                    self._reset_silence = False
                    log_debug(_('Сброс счётчика молчания.'))
                sleep(1)
                if self.recognizer.pause:
                    self._silence_from = int(time())
                self.calc_silence_seconds()
            thread = self._calc_silence_thread
            self._calc_silence_thread = None
            log_debug(_('Завершён поток подсчёта тишины %s.'), thread.name)

        log_debug(_('Запуск отдельного потока подсчёта тишины.'))
        thread = Thread(target=calc_silence, daemon=True)
        thread.start()
        log_debug(_('Запущен поток подсчёта тишины %s.'), thread.name)
        self._calc_silence_thread = thread

        def listen():
            # От начала и до конца беседы поток голоса абонента анализируется.
            # Причём, когда объём потока превышает разрешённые 10 мегабайт
            # и парсинг завершается, мы запускаем новый парсинг.
            recieved = 0
            while self.has_start_recognize():
                log_debug(_('Запуск recognizer.recognize()'))
                recognizer = self.recognizer
                recognizer.listen(self)
                if hasattr(recognizer, 'listener'):
                    recieved += recognizer.listener.total_size
                else:
                    log_error(_('Слушатель не был подключен.'))
                log_debug(_('Остановка recognizer.recognize()'))
            thread = self._recognizer_thread
            self._recognizer_thread = None
            log_debug(
                _('Завершён поток распознавания %(name)s. Считано '
                  'аудио-данных: %(recieved)d байт.'),
                {
                    'name': thread.name,
                    'recieved': recieved,
                }
            )

        self.is_closed = False
        log_debug(_('Запуск отдельного потока распознавания.'))
        thread = Thread(target=listen, daemon=True)
        thread.start()
        log_debug(_('Запущен поток распознавания %s.'), thread.name)
        self._recognizer_thread = thread
        return thread

    def stop(self):
        log_debug(_('Диалог останавливается.'))
        self.is_closed = True
        # Отключаем здесь листенер, чтобы быстрее выйти, а не ждать слова в
        # трубку.
        if hasattr(self.recognizer, 'listener'):
            listener = self.recognizer.listener
            listener.stop()
            log_debug(_('Слушатель выключен.'))
        else:
            log_error(_('Слушатель не был подключен.'))

    def run(self):
        log_info(
            _('Диалог начат: %(agi_callerid)s (%(agi_calleridname)s)'),
            self.agi.params,
        )
        # Делаем самый первый текстовый буфер.
        self.make_text_buffer()
        # Затем запускаем процесс потокового распознавания речи.
        self.start()
        hangup = False
        error = None
        started = datetime.utcnow()
        try:
            self.main_script()
        except AgiHangupError:
            log_info(_('Абонент повесил трубку до окончания диалога.'))
            hangup = True
        except AgiError as e:
            error = _('Ошибка в AGI при исполнении диалога.')
            log_error(error, exc_info=e)
        except Exception as e:
            error = _('Ошибка в сценарии диалога.')
            log_error(error, exc_info=e)
        self.stop()
        finished = datetime.utcnow()

        agi = self.agi
        try:
            for key, value in self.export.items():
                if key.startswith('_'):
                    continue
                # В Asterisk отправляем только самые примитивные типы.
                if value is not None and not isinstance(value, (str, int, float, bool)):
                    continue
                value = str(value)
                log_debug(_('Передача в Asterisk %(key)s=%(value)s'), {
                    'key': key, 'value': value})
                agi.set(key, value)
        except AgiHangupError:
            log_info(
                _('Абонент повесил трубку до окончания передачи переменных.'))
            hangup = True
        except AgiError as e:
            error = _('Ошибка в AGI при передаче переменных.')
            log_error(error, exc_info=e)

        filename = self.settings.export_dialog(
            self.agi.params, self.export, self.text_buffers,
            dialog_id=self.id,
            hangup=hangup,
            error=error,
            chain=self.chain,
            started='%sZ' % started.isoformat(),
            finished='%sZ' % finished.isoformat(),
            duration=(finished - started).total_seconds(),
        )
        if filename:
            log_info(_('Диалог был экспортирован в файл %s'), filename)

        for key, text_buffer in self.text_buffers.items():
            for line in text_buffer.get_text(4).split('\n'):
                log_debug(_('Текст буфера %(key)s: %(line)s'),
                          {'key': key, 'line': line})

        log_info(_('Диалог завершён.'))

    def execute_plugin(self, name, result, speech, variables, config=None):
        """
        Возвращает кортеж из результата выполнения подпроцесса и словаря данных,
        которыми плагин оперировал.
        Плагин может устанавливать свои переменные в процессе своей работы или
        ещё какие-либо данные в файл обмена данными.
        """
        plugin = self.settings.get_plugin(name)
        log_debug('> PLUGIN %s', plugin)
        plugin_data = {
            'dialog_id': self.id,
            'agi_params': self.agi.params,
            'work_dir': self.settings.work_dir,
            'speech': speech,
            'variables': variables,
            'chain': self.chain,
            'text_buffers': self.text_buffers,
            'config': config or {},
        }
        if result is None or \
                isinstance(result, (str, bool, list, tuple, int, float)):
            plugin_data['result'] = result
        else:
            plugin_data['result'] = str(result)
        tempfile = NamedTemporaryFile(mode='w', suffix='.json')
        tempfile_name = tempfile.name
        json.dump(plugin_data, tempfile)
        tempfile.flush()
        log_debug('JSONFILE %s', tempfile_name)
        res = subprocess.run(
            [plugin, tempfile_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )

        if res.returncode:
            log_error(_('Плагин %r сломан.'), plugin)
            log_error('< PLUGIN %s', res.stderr)
        else:
            log_debug('< PLUGIN %s', res.stdout)
            plugin_data = json.load(open(tempfile_name))
            variables.update(plugin_data['variables'])
            # Предварительный фоновый синтез текстов.
            # Заметьте, что такой синтез будет выполняться с тем синтезатором,
            # который используется для блока, в котором запускается вызов
            # плагина.
            synthesize = plugin_data.get('synthesize', [])
            if synthesize and isinstance(synthesize, list):
                def make_voices():
                    log_debug(
                        _('Предварительный синтез для %d текста(ов).'),
                        len(synthesize)
                    )
                    for txt in synthesize:
                        self.synthesizer.make_voice(str(txt), early=True)
                    log_debug(_('Предварительный синтез речи завершён.'))

                t = Thread(target=make_voices, daemon=True)
                t.start()
            # Логгирование каких-либо строк из плагина.
            loggers = (
                ('log_debug', log_debug),
                ('log_info', log_info),
                ('log_warning', log_warning),
                ('log_error', log_error),
                # TODO: удалить следующие параметры в версии 0.30:
                ('debug', log_debug),
                ('info', log_info),
                ('warnings', log_warning),
                ('errors', log_error),
            )
            for _name, _logger in loggers:
                if _name in ("debug", "info", "warnings", "errors") and _name in plugin_data:
                    # TODO: удалить в версии 0.30:
                    log_warning(_(
                        '< PLUGIN Параметр %r скоро устареет, используйте один из: '
                        '"log_debug", "log_info", "log_warning" или "log_error"'
                    ), _name)
                strings = plugin_data.get(_name, [])
                for string in strings:
                    _logger('< PLUGIN %s', string)
        tempfile.close()
        return res, plugin_data

    def blocklog(self, logname, *args, **kwargs):
        log = self._blocklog
        if log is None:
            self._blocklog = log = []
        now = datetime.utcnow()
        log.append(['%sZ' % now.isoformat(), logname, args, kwargs])

    def main_script(self):
        settings = self.settings
        scheme = settings.dialog_scheme
        constants = scheme.get('constants', {})
        default_variables = scheme.get('variables', {})
        self.export = variables = OrderedDict()
        self.chain = chain = []
        variables.update(default_variables)
        variables.update(constants)
        # Словарь скриптов.
        scripts = scheme.get('scripts', {})
        # Программа главного скрипта.
        program = OrderedDict([(p['name'], p) for p in scheme['main_script']])
        index = tuple(program.keys())
        process = program[index[0]]
        log_debug(_('Главный скрипт начат.'))
        while process and not self.is_closed:
            name = process['name']
            script = scripts.get(name)
            if not script:
                log_error(_('Скрипт %r отсутствует.'), name)
                break
            script_type = script['type']
            # Здесь должна возникать ошибка AttributeError для сломанных схем.
            method = getattr(self, '_script_%s' % script_type)

            # Сбрасываем логгирование для блока (скрипта).
            self._blocklog = None
            block_start = time()
            self.blocklog('block_start')

            debug_msg = '  SCRIPT %s'
            debug_args = [name.upper()]
            if 'group' in process:
                debug_msg += ' GROUP %s'
                debug_args.append(process['group'].upper())
            log_debug(debug_msg, *debug_args)

            # Конфигурация `synthesizer` уровня блока (скрипта).
            # Объект `recognizer` нельзя переопределить на этом уровне.
            synth_conf = script.get('synthesizer', {})
            if synth_conf:
                self.synthesizer = settings.get_synthesizer(**synth_conf)
            else:
                self.synthesizer = self.main_synthesizer

            self.partials_begin = 0
            if 'partials_begin' in script:
                try:
                    self.partials_begin = int(script['partials_begin'])
                except ValueError:
                    pass

            say_debug = process.get('say_debug')
            if say_debug:
                saydata = {'text': _('Запускаю скрипт %(name)r') % process}
                self.say(**make_say_params(saydata, variables))

            result, speech = method(script, variables)
            self.blocklog('block_result')
            log_debug('  RESULT %r', result)
            log_debug('  SPEECH %r', speech)
            # Экспортируем разговор в отдельную переменную, чтобы иметь
            # доступ к нему в других скриптах и плагинах.
            export_speech = script.get('export_speech')
            if export_speech:
                variables[export_speech] = speech

            # Запускаем плагин при его наличии.
            plugin_name = process.get('plugin')
            if plugin_name:
                plugin_conf = process.get('plugin_conf')
                self.execute_plugin(plugin_name, result, speech, variables, plugin_conf)
                self.blocklog('plugin', name=plugin_name, conf=plugin_conf,
                              result=result, speech=speech)

            # Устанавливаем следующий процесс.
            success = process.get('success')
            if isinstance(success, dict):
                success = success.get(result)
            # Динамическое определение следующего скрипта может определяться
            # из ранее установленных переменных.
            if success and '%(' in success:
                success %= variables
            fail = process.get('fail')
            if fail and '%(' in fail:
                fail %= variables
            log_debug(' SUCCESS %s', success)
            log_debug('    FAIL %s', fail)
            if process.get('finish', False):
                log_debug('  FINISH')
                if say_debug:
                    saydata = {'text': _('Завершаю диалог.')}
                    self.say(**make_say_params(saydata, variables))
                process = None
            elif result and success in program:
                if say_debug:
                    saydata = {'text': _('Исходная речь. %s.') % speech}
                    self.say(**make_say_params(saydata, variables))
                    if result is True:
                        saydata = {'text': _('В результате получена истина.')}
                    else:
                        saydata = {
                            'text': _('Разультат обработки. %s.') % result}
                    self.say(**make_say_params(saydata, variables))
                process = program[success]
            elif not result and fail in program:
                if say_debug:
                    if speech:
                        saydata = {'text': _('Исходная речь. %s.') % speech}
                    else:
                        saydata = {'text': _('Исходная речь пуста.')}
                    self.say(**make_say_params(saydata, variables))
                    saydata = {'text': _('Результат отсутствует.')}
                    self.say(**make_say_params(saydata, variables))
                process = program[fail]
            else:
                try:
                    process = program.get(index[index.index(name) + 1])
                except IndexError:
                    process = None
            log_debug('    NEXT %s', process)
            # if say_debug and process:
            #     saydata = {'text': _('Следующий скрипт %(name)r') % process}
            #     self.say(**make_say_params(saydata, variables))

            # Восстанавливаем константы. Это проще, чем городить лес кода.
            variables.update(constants)
            # Сохраняем цепочку вызовов скриптов.
            block_finish = time()
            self.blocklog('block_finish', duration=(block_finish - block_start))
            chain.append([name, result, speech, self._blocklog])

        log_debug(_('Главный скрипт завершён.'))

    def _agi_execute(self, commands, key):
        try:
            command = commands.get(key, [])
            assert isinstance(command, list)
        except AssertionError:
            command = []
        if command:
            # Обрабатываем аргументы, преобразовывая шаблонные переменные.
            kw = self.agi.params.copy()
            kw.update(self.export)
            for i, val in enumerate(command):
                # Пропускаем первый аргумент и все не строковые аргументы.
                if i and isinstance(val, str):
                    command[i] = val.format(**kw)
            log_debug(_('Выполняется команда AGI: %s'), command)
            self.agi.execute(*command)
            log_debug(_('Команда выполнена.'))
        return command

    def _agi_stop_playback(self, saydata=None):
        log_debug('_agi_stop_playback')
        if not saydata or not isinstance(saydata, dict):
            log_debug(_('Нечего опрерывать, saydata=%s'), saydata)
            return
        if not saydata.get('nonblocking', False):
            log_debug(_('Нечего прерывать, был задан блокирующий режим.'))
            return

        stop_voice = splitext(self.settings.get_stop_file())[0]
        if not stop_voice:
            log_debug(_('Стоп-голоса для прерывания нет.'))
            return
        if not self._voice:
            log_debug(_('Нечего прерывать, голос уже закончился.'))
            return
        # Сначала должен среагировать поток озвучки голоса, а затем отправляем
        # команду остановки.
        self._voice = None
        self._voice_duration = 0
        try:
            self.agi.stream_file(stop_voice)
        except AgiSigpipeError:
            self.is_closed = True
            log_info(_('Стоп-голос не отправлен. Связь разорвана.'))
            return
        except Exception as e:
            self.is_closed = True
            raise e
        log_debug(_('Прерывание воспроизведения выполнено.'))

    def _script_capture(self, script, variables):
        assert script['type'] == 'capture'

        assert 'export_name' in script
        export_name = script['export_name']
        assert export_name and isinstance(export_name, str)
        if 'initial_value' in script:
            variables[export_name] = script['initial_value']

        pauses = script.get('pauses', {})
        make_pause(pauses, 'before')

        commands = script.get('commands', {})
        self._agi_execute(commands, 'before')

        mode = int(script.get('mode_buffer', 1))
        assert mode in (1, 2, 3)
        # Для капчуринга всегда создаём новый буфер.
        self.make_text_buffer()
        text_buffer = self.get_last_text_buffer()

        saydata = script.get('say_start')
        if saydata:
            make_pause(pauses, 'before_say_start')
            self._agi_execute(commands, 'before_say_start')
            self.say(**make_say_params(saydata, variables))
            make_pause(pauses, 'after_say_start')
            self._agi_execute(commands, 'after_say_start')
        say_start_duration = self._voice_duration

        self.start_recognizing()

        maxtime = float(script.get('maxtime', 600))
        minlength = int(script.get('minlength', 10))
        maxsilence = int(script.get('maxsilence', 10))
        startsilence = int(script.get('startsilence', 0))
        stopwords = script.get('stopwords', [])
        log_debug(_('Ограничение по времени: %s секунд.'), maxtime)
        log_debug(_('Ограничение по длине: от %s символов.'), minlength)
        log_debug(_('Ограничение по тишине: %s секунд.'), maxsilence)
        log_debug(_('Ограничение по тишине в начале: %s секунд.'), startsilence)
        log_debug(_('Ограничение по стоп-словам: %s.'), stopwords)
        stopwords = set(stopwords)

        func = self.capture_text
        speech, stop = func(
            stopwords,
            mode=mode,
            text_buffer=text_buffer,
            second=0,
            maxsilence=maxsilence,
            minlength=minlength,
            startsilence=startsilence,
        )
        if stop:
            log_debug(_('Первая попытка успешна. Текст: %s'), speech)
        else:
            log_debug(_('Первая попытка провалилась. Текст: %s'), speech)
        # В блокирующем режиме голоса его длина уже будет сброшена в 0.
        maxtime += say_start_duration

        second = 0
        # Количество секунд тишины.
        while not stop and second < maxtime:
            log_debug(_('Стоп-слова пока нет, ждём %d-ю секунду.'), second)
            second += 0.5
            sleep(0.5)
            speech, stop = func(
                stopwords,
                mode=mode,
                text_buffer=text_buffer,
                second=second,
                maxsilence=maxsilence,
                minlength=minlength,
                startsilence=startsilence,
            )

            if self.is_stopped:
                log_debug(_('Диалог завершился до приёма данных.'))
                break

        self.stop_recognizing()

        if speech:
            answer = speech
            log_debug(_('Ответ: %r'), answer)
            self.blocklog('answer', answer=answer, speech=speech)
            prepare_answer(
                answer=answer, source=answer, export_name=export_name,
                script=script, variables=variables)

            self._agi_stop_playback(script.get('say_start'))

            # Когда указан файл плагина, то он должен обработать переменные
            # перед say_success.
            plugin_name = script.get('plugin')
            if plugin_name:
                plugin_conf = script.get('plugin_conf')
                self.execute_plugin(plugin_name, answer, speech, variables,
                                    plugin_conf)
                self.blocklog('plugin', name=plugin_name, conf=plugin_conf,
                              result=answer, speech=speech)

            saydata = script.get('say_success')
            if saydata:
                make_pause(pauses, 'before_say_success')
                self._agi_execute(commands, 'before_say_success')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_success')
                self._agi_execute(commands, 'after_say_success')
        else:
            answer = None
            if speech:
                self.blocklog('answer', speech=speech, invalid=True)
            log_debug(_('Ответа нет.'))
            saydata = script.get('say_fail')
            if saydata:
                make_pause(pauses, 'before_say_fail')
                self._agi_execute(commands, 'before_say_fail')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_fail')
                self._agi_execute(commands, 'after_say_fail')

        make_pause(pauses, 'after')
        self._agi_execute(commands, 'after')
        return answer, speech

    def _script_parse_names(self, script, variables):
        assert script['type'] == 'parse_names'

        assert 'export_name' in script
        export_name = script['export_name']
        assert export_name and isinstance(export_name, str)
        if 'initial_value' in script:
            variables[export_name] = script['initial_value']

        pauses = script.get('pauses', {})
        make_pause(pauses, 'before')

        commands = script.get('commands', {})
        self._agi_execute(commands, 'before')

        mode = int(script.get('mode_buffer', 1))
        assert mode in (1, 2, 3)
        if script.get('new_buffer', False):
            self.make_text_buffer()

        saydata = script.get('say_start')
        if saydata:
            make_pause(pauses, 'before_say_start')
            self._agi_execute(commands, 'before_say_start')
            self.say(**make_say_params(saydata, variables))
            make_pause(pauses, 'after_say_start')
            self._agi_execute(commands, 'after_say_start')
        say_start_duration = self._voice_duration

        self.start_recognizing()

        say_silence = script.get('say_silence')
        if say_silence:
            say_silence_time = say_silence['time']
        else:
            say_silence_time = 0
        say_silence_index = 0

        attempts = script.get('attempts') or {}
        attempts_count = abs(int(attempts.get('count', 0))) or 1
        attempts_iter_time = float(attempts.get('iter_time', 0))
        attempts_iter_pause = float(attempts.get('iter_pause', 0)) or 1.0

        func = self.parse_names
        names, speech = func(mode=mode)
        if names:
            log_debug(_('Первая попытка успешна. Имена: %s'), names)
        else:
            log_debug(_('Первая попытка провалилась. Имена: %s'), names)
        for attempt in range(attempts_count):
            _iter_time = attempts_iter_time
            if attempt == 0:
                # В блокирующем режиме голоса его длина уже будет сброшена в 0.
                _iter_time += say_start_duration
            second = 0
            while not names and second < _iter_time:
                log_debug(_('Ответа пока нет, ждём %d-ю секунду.'), second)
                second += attempts_iter_pause
                sleep(attempts_iter_pause)
                names, speech = func(mode=mode)
                if self.is_stopped:
                    log_debug(_('Диалог завершился до приёма данных.'))
                    break
                # Обработка молчания ягнят.
                if say_silence_time and (attempt > 0 or second > say_start_duration):
                    ss = self.silence_seconds
                    if second and ss and ss % say_silence_time == 0:
                        log_debug(_('Кратность %r.'), say_silence_time)
                        say_silence_index = self.say_silence(
                            say_silence, say_silence_index, variables)
            if names:
                length_names = int(script.get('length_names', 2))
                answer = ' '.join(names[:length_names])
                self.blocklog('answer', answer=answer, speech=speech)
                log_debug(_('Ответ: %r'), answer)
                prepare_answer(
                    answer=answer, source=answer, export_name=export_name,
                    script=script, variables=variables)

                self._agi_stop_playback(script.get('say_start'))

                saydata = script.get('say_success')
                if saydata:
                    make_pause(pauses, 'before_say_success')
                    self._agi_execute(commands, 'before_say_success')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_success')
                    self._agi_execute(commands, 'after_say_success')
                break
            elif attempt < attempts_count - 1:
                if attempts.get('new_buffer', False):
                    if speech:
                        self.blocklog('answer', speech=speech, invalid=True)
                    self.make_text_buffer()
                saydata = attempts.get('say')
                if saydata:
                    make_pause(pauses, 'before_say_attempt')
                    self._agi_execute(commands, 'before_say_attempt')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_attempt')
                    self._agi_execute(commands, 'after_say_attempt')

        self.stop_recognizing()

        if not names:
            if speech:
                self.blocklog('answer', speech=speech, invalid=True)
            log_debug(_('Ответа нет.'))
            saydata = script.get('say_fail')
            if saydata:
                make_pause(pauses, 'before_say_fail')
                self._agi_execute(commands, 'before_say_fail')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_fail')
                self._agi_execute(commands, 'after_say_fail')

        make_pause(pauses, 'after')
        self._agi_execute(commands, 'after')
        return names, speech

    def _script_search_by_buffer(self, script, variables):
        assert script['type'] == 'search_by_buffer'

        assert 'export_name' in script
        export_name = script['export_name']
        assert export_name and isinstance(export_name, str)
        if 'initial_value' in script:
            variables[export_name] = script['initial_value']

        assert 'regexp' in script
        regexp = script['regexp']
        assert regexp and isinstance(regexp, dict)

        assert 'pattern' in regexp
        pattern = regexp['pattern']
        assert pattern and isinstance(pattern, str)

        pauses = script.get('pauses', {})
        make_pause(pauses, 'before')

        commands = script.get('commands', {})
        self._agi_execute(commands, 'before')

        mode = int(script.get('mode_buffer', 1))
        assert mode in (1, 2, 3)
        if script.get('new_buffer', False):
            self.make_text_buffer()

        saydata = script.get('say_start')
        if saydata:
            make_pause(pauses, 'before_say_start')
            self._agi_execute(commands, 'before_say_start')
            self.say(**make_say_params(saydata, variables))
            make_pause(pauses, 'after_say_start')
            self._agi_execute(commands, 'after_say_start')
        say_start_duration = self._voice_duration

        self.start_recognizing()

        say_silence = script.get('say_silence')
        if say_silence:
            say_silence_time = say_silence['time']
        else:
            say_silence_time = 0
        say_silence_index = 0

        attempts = script.get('attempts') or {}
        attempts_count = abs(int(attempts.get('count', 0))) or 1
        attempts_iter_time = float(attempts.get('iter_time', 0))
        attempts_iter_pause = float(attempts.get('iter_pause', 0)) or 1.0

        func = self.search_by_buffer
        flag = re.UNICODE
        if regexp.get('ignorecase', False):
            flag |= re.IGNORECASE
        pattern = re.compile(pattern, flag)
        match, speech = func(pattern, mode=mode)
        answer = None
        for attempt in range(attempts_count):
            _iter_time = attempts_iter_time
            if attempt == 0:
                # В блокирующем режиме голоса его длина уже будет сброшена в 0.
                _iter_time += say_start_duration
            second = 0
            while not match and second < _iter_time:
                log_debug(_('Ответа пока нет, ждём %d-ю секунду.'), second)
                second += attempts_iter_pause
                sleep(attempts_iter_pause)
                match, speech = func(pattern, mode=mode)
                if self.is_stopped:
                    log_debug(_('Диалог завершился до приёма данных.'))
                    break
                # Обработка молчания ягнят.
                if say_silence_time and (attempt > 0 or second > say_start_duration):
                    ss = self.silence_seconds
                    if second and ss and ss % say_silence_time == 0:
                        log_debug(_('Кратность %r.'), say_silence_time)
                        say_silence_index = self.say_silence(
                            say_silence, say_silence_index, variables)
            if match:
                answer = match.group()
                self.blocklog('answer', answer=answer, speech=speech)
                log_debug(_('Ответ: %r'), answer)
                prepare_answer(
                    answer=answer, source=answer, export_name=export_name,
                    script=script, variables=variables)

                self._agi_stop_playback(script.get('say_start'))

                saydata = script.get('say_success')
                if saydata:
                    make_pause(pauses, 'before_say_success')
                    self._agi_execute(commands, 'before_say_success')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_success')
                    self._agi_execute(commands, 'after_say_success')
                break
            elif attempt < attempts_count - 1:
                if attempts.get('new_buffer', False):
                    if speech:
                        self.blocklog('answer', speech=speech, invalid=True)
                    self.make_text_buffer()
                saydata = attempts.get('say')
                if saydata:
                    make_pause(pauses, 'before_say_attempt')
                    self._agi_execute(commands, 'before_say_attempt')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_attempt')
                    self._agi_execute(commands, 'after_say_attempt')

        self.stop_recognizing()

        if not match:
            if speech:
                self.blocklog('answer', speech=speech, invalid=True)
            log_debug(_('Ответа нет.'))
            saydata = script.get('say_fail')
            if saydata:
                make_pause(pauses, 'before_say_fail')
                self._agi_execute(commands, 'before_say_fail')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_fail')
                self._agi_execute(commands, 'after_say_fail')

        make_pause(pauses, 'after')
        self._agi_execute(commands, 'after')
        if script.get('fail_on_false'):
            answer = variables.get(export_name) in (
                True, 'True', 'true', 'TRUE')
            log_debug(_('Режим `fail_on_false`, ответ %r.'), answer)
        return answer, speech

    def _script_text_processing(self, script, variables):
        assert script['type'] == 'text_processing'

        assert 'export_name' in script
        export_name = script['export_name']
        assert export_name and isinstance(export_name, str)
        if 'initial_value' in script:
            variables[export_name] = script['initial_value']

        assert 'file' in script
        filename = script['file']
        assert filename and isinstance(filename, str)

        pauses = script.get('pauses', {})
        make_pause(pauses, 'before')

        commands = script.get('commands', {})
        self._agi_execute(commands, 'before')

        mode = int(script.get('mode_buffer', 1))
        assert mode in (1, 2, 3)
        if script.get('new_buffer', False):
            self.make_text_buffer()

        saydata = script.get('say_start')
        if saydata:
            make_pause(pauses, 'before_say_start')
            self._agi_execute(commands, 'before_say_start')
            self.say(**make_say_params(saydata, variables))
            make_pause(pauses, 'after_say_start')
            self._agi_execute(commands, 'after_say_start')
        say_start_duration = self._voice_duration

        self.start_recognizing()

        say_silence = script.get('say_silence')
        if say_silence:
            say_silence_time = say_silence['time']
        else:
            say_silence_time = 0
        say_silence_index = 0

        attempts = script.get('attempts') or {}
        attempts_count = abs(int(attempts.get('count', 0))) or 1
        attempts_iter_time = float(attempts.get('iter_time', 0))
        attempts_iter_pause = float(attempts.get('iter_pause', 0)) or 1.0

        func = self.text_processing
        response, speech = func(filename, mode=mode)
        if response:
            log_debug(_('Первая попытка успешна. Ответ: %s'), response)
        else:
            log_debug(_('Первая попытка провалилась. Ответа нет.'))
        for attempt in range(attempts_count):
            _iter_time = attempts_iter_time
            if attempt == 0:
                # В блокирующем режиме голоса его длина уже будет сброшена в 0.
                _iter_time += say_start_duration
            second = 0
            while not response and second < _iter_time:
                log_debug(_('Ответа пока нет, ждём %d-ю секунду.'), second)
                second += attempts_iter_pause
                sleep(attempts_iter_pause)
                response, speech = func(filename, mode=mode)
                if self.is_stopped:
                    log_debug(_('Диалог завершился до приёма данных.'))
                    break
                # Обработка молчания ягнят.
                if say_silence_time and (attempt > 0 or second > say_start_duration):
                    ss = self.silence_seconds
                    if second and ss and ss % say_silence_time == 0:
                        log_debug(_('Кратность %r.'), say_silence_time)
                        say_silence_index = self.say_silence(
                            say_silence, say_silence_index, variables)
            if response:
                answer = response
                self.blocklog('answer', answer=answer, speech=speech)
                log_debug(_('Ответ: %r'), answer)
                prepare_answer(
                    answer=answer, source=speech, export_name=export_name,
                    script=script, variables=variables)

                self._agi_stop_playback(script.get('say_start'))

                saydata = script.get('say_success')
                if saydata:
                    make_pause(pauses, 'before_say_success')
                    self._agi_execute(commands, 'before_say_success')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_success')
                    self._agi_execute(commands, 'after_say_success')
                break
            elif attempt < attempts_count - 1:
                if attempts.get('new_buffer', False):
                    if speech:
                        self.blocklog('answer', speech=speech, invalid=True)
                    self.make_text_buffer()
                saydata = attempts.get('say')
                if saydata:
                    make_pause(pauses, 'before_say_attempt')
                    self._agi_execute(commands, 'before_say_attempt')
                    self.say(**make_say_params(saydata, variables))
                    make_pause(pauses, 'after_say_attempt')
                    self._agi_execute(commands, 'after_say_attempt')

        self.stop_recognizing()

        if not response:
            if speech:
                self.blocklog('answer', speech=speech, invalid=True)
            log_debug(_('Ответа нет.'))
            saydata = script.get('say_fail')
            if saydata:
                make_pause(pauses, 'before_say_fail')
                self._agi_execute(commands, 'before_say_fail')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_fail')
                self._agi_execute(commands, 'after_say_fail')

        make_pause(pauses, 'after')
        self._agi_execute(commands, 'after')
        return response, speech

    def _script_simple_say(self, script, variables):
        assert script['type'] == 'simple_say'

        if 'export_name' in script:
            export_name = script['export_name']
            assert export_name and isinstance(export_name, str)
            if 'initial_value' in script:
                variables[export_name] = script['initial_value']
            # TODO: удалить в версии 0.30.
            elif 'export_value' in script:
                variables[export_name] = script['export_value']

        pauses = script.get('pauses', {})
        make_pause(pauses, 'before')

        commands = script.get('commands', {})
        self._agi_execute(commands, 'before')

        mode = int(script.get('mode_buffer', 1))
        assert mode in (1, 2)
        if script.get('new_buffer', False):
            self.make_text_buffer()

        result = True
        plugin_name = script.get('plugin_before')
        if plugin_name:
            plugin_conf = script.get('plugin_before_conf')
            res, plugin_data = self.execute_plugin(
                plugin_name, result, '', variables, plugin_conf)
            self.blocklog('plugin', name=plugin_name, conf=plugin_conf,
                          result=result, speech='')
            result = plugin_data.get('result')
            self.blocklog('plugin_return', result)

        saydata = script.get('say_start')
        if saydata:
            make_pause(pauses, 'before_say_start')
            self._agi_execute(commands, 'before_say_start')
            self.say(**make_say_params(saydata, variables))
            make_pause(pauses, 'after_say_start')
            self._agi_execute(commands, 'after_say_start')

        plugin_name = script.get('plugin_after')
        if plugin_name:
            plugin_conf = script.get('plugin_after_conf')
            res, plugin_data = self.execute_plugin(
                plugin_name, result, '', variables, plugin_conf)
            self.blocklog('plugin', name=plugin_name, conf=plugin_conf,
                          result=result, speech='')
            result = plugin_data.get('result')
            self.blocklog('plugin_return', result)

        if result:
            log_debug(_('Результат есть.'))
            saydata = script.get('say_success')
            if saydata:
                make_pause(pauses, 'before_say_success')
                self._agi_execute(commands, 'before_say_success')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_success')
                self._agi_execute(commands, 'after_say_success')
        else:
            log_debug(_('Результата нет.'))
            saydata = script.get('say_fail')
            if saydata:
                make_pause(pauses, 'before_say_fail')
                self._agi_execute(commands, 'before_say_fail')
                self.say(**make_say_params(saydata, variables))
                make_pause(pauses, 'after_say_fail')
                self._agi_execute(commands, 'after_say_fail')

        make_pause(pauses, 'after')
        self._agi_execute(commands, 'after')

        speech = self.text_from_text_buffer()
        if speech:
            self.blocklog('answer', speech=speech)
        return result, speech
