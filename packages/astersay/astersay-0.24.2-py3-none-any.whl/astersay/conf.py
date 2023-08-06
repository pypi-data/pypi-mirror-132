#
# Copyright (c) 2020, Grigoriy Kramarenko
# All rights reserved.
# This file is distributed under the same license as the current project.
#
import json
import re
import requests
import sys
from datetime import datetime
from gettext import gettext as _
from logging import getLogger
from logging.config import dictConfig
from os import makedirs, remove, getpid
from os.path import join as path_join, expanduser, abspath, exists, dirname, basename
from threading import Thread

from astersay.exceptions import ImproperlyConfigured
from astersay.utils import prepare_dialog_name, import_string, make_checksum

logger = getLogger(__name__)

BASE_DIR = dirname(abspath(__file__))
DEFAULT_WORK_DIR = path_join(expanduser('~'), '.config', 'astersay')
DEFAULT_DIALOG = {
    'constants': {
        'manager_contact': 'Менеджер Василий +79008001234',
    },
    'variables': {
        # Инициализация переменных на уровне диалога.
        'caller_name': 'Аноним',
    },
    # Бэкэнды распознавания и синтеза можно задавать на уровне диалога,
    # но синтез ещё и на уровне конкретного блока (скрипта). Если эти
    # настройки не определены в диалоге или являются пустыми словарями, то
    # используются настройки уровня приложения.
    'recognizer': {
        # 'backend': 'astersay.backends.yandex.YandexRecognizer',
        # 'params': {}
    },
    'synthesizer': {
        # 'backend': 'astersay.backends.yandex.YandexSynthesizer',
        # 'params': {}
    },
    'main_script': [
        # При успехе следующим будет исполнен скрипт '003', иначе '005'.
        {'name': '001', 'success': '002', 'fail': '005'},
        # При любом завершении будет исполнен скрипт '003'.
        {'name': '002'},
        # При любом завершении будет исполнен скрипт '004'.
        {'name': '003'},
        # При любом завершении будет исполнен скрипт '005'.
        {'name': '004'},
        # При любом завершении данные будут переданы указанному плагину.
        # Принимать их или нет - решать плагину.
        {'name': '005', 'plugin': 'example.py'},
    ],
    'scripts': {
        '001': {
            'type': 'parse_names',
            'export_name': 'caller_name',
            'new_buffer': True,
            # Режим чтения буфера с распознанным текстом.
            # 1 - финальный текст, 2 - промежуточный текст, 3 - весь.
            'mode_buffer': 1,
            # Для режимов чтения буфера 2 и 3 следующая переменная определяет
            # начальную итерацию, с которой частичные результаты начнут
            # учитываться.
            # 'partials_begin': 1,
            'say_start': {
                # Текст можно задавать двумя вариантами:
                # 'text': 'Первое предложение. Последнее предложение.'
                # 'text': 'Первое предложение. |Последнее предложение.'
                # 'texts': ['Первое предложение.', 'Последнее предложение.']
                # Когда задан список или текст с разделителем, то эти части
                # синтезируются отдельно и потом соединяются в отдельный файл
                # голоса. Таким образом можно и нужно отделять часто
                # синтезируемый текст от редкосинтезируемого.

                # Вместо текста можно указать файл голоса двумя вариантами:
                # 'voice': '/full/path/to/voice' - без расширения;
                # 'file': '/full/path/to/voicefile.wav' - с расширением.
                'text': _(
                    'Здравствуйте, с Вами говорит базовая диалоговая модель. '
                    'Меня разрабатывали очень весёлые люди. Поэтому я могу '
                    'быть весьма неожиданной. В принципе обо мне - всё. '
                    'Позвольте мне теперь узнать о Вас. |Представьтесь, '
                    'пожалуйста.'
                ),
                'escape_digits': '1234567890',
                'nonblocking': True,
            },
            'say_success': {
                'text': _(
                    '%(caller_name)s| мне очень приятно было распознать '
                    'Ваше имя.'
                ),
            },
            'say_fail': {
                'text': _('Увы, но мне не удалось распознать Ваше имя.'),
            },
            'attempts': {
                # Количество итераций.
                'count': 3,
                # Максимальное время одной итерации.
                'iter_time': 15,
                # Размер пауз для ожидания ответа во время одной итерации.
                'iter_pause': 1.0,
                'new_buffer': True,
                'say': {
                    'text': _('Попробуйте назвать ещё раз своё имя.'),
                },
            },
            # Все паузы по-умолчанию равны нулю.
            'pauses': {
                'before': 0,
                'after': 0,
                'before_say_start': 0,
                'after_say_start': 3,
                'before_say_success': 0,
                'after_say_success': 0,
                'before_say_fail': 0,
                'after_say_fail': 0,
                'before_say_attempt': 0,
                'after_say_attempt': 0,
            },
            # Команда для Asterisk - это список аргументов, передаваемых
            # в метод `agi.execute`. Команда выполняется сразу после
            # одноимённой паузы. По-умолчанию команды равны пустому
            # списку и поэтому не производятся.
            'commands': {
                'before': [],
                'after': [],
                'before_say_start': [],
                'after_say_start': [],
                'before_say_success': [],
                'after_say_success': [],
                'before_say_fail': [],
                'after_say_fail': [],
                'before_say_attempt': [],
                'after_say_attempt': [],
            },
        },
        '002': {
            'type': 'search_by_buffer',
            'export_name': 'answered_yes',
            'export_name_text': 'answered_yes_text',
            'new_buffer': True,
            'mode_buffer': 3,
            'partials_begin': 3,
            'regexp': {
                # В такой регулярке отрицания нужно ставить перед
                # положительными ответами.
                'pattern': 'нет|^не | не |заткн|негатив|дура|отрица'
                           'да|конечн|угу|окей|отлично|может|положител',
                'ignorecase': True,
            },
            'booleanize': {
                'true_list': [
                    'да', 'конечн', 'угу', 'окей', 'отлично', 'может',
                    'положител'
                ],
                'text_true': 'положительно',
                'text_false': 'отрицательно'
            },
            'say_start': {
                'text': _(
                    'Если Вы, %(caller_name)s, сейчас скажете какое-нибудь '
                    'положительное или отрицательное утверждение, то я '
                    'попробую распознать и это.'
                ),
                'escape_digits': '1234567890',
                'nonblocking': True,
            },
            'say_success': {
                'text': _('Вы ответили %(answered_yes_text)s, благодарю Вас!.'),
            },
            'say_fail': {
                'text': _('Увы, но мне не удалось распознать утверждение.'),
            },
            'attempts': {
                # Количество итераций.
                'count': 2,
                # Максимальное время одной итерации.
                'iter_time': 10,
                # Размер пауз для ожидания ответа во время одной итерации.
                'iter_pause': 0.5,
                'new_buffer': True,
                'say': {
                    'text': _('Я не поняла Ваш ответ, попробуйте сказать ещё раз.'),
                },
            },
        },
        '003': {
            'type': 'text_processing',
            'file': 'example.py',
            'export_name': 'city',
            'new_buffer': True,
            'mode_buffer': 3,
            'partials_begin': 3,
            'say_start': {
                'text': _(
                    'Пожалуйста, назовите сейчас какой-нибудь известный '
                    'российский город, а я попробую распознать его.'
                ),
                'escape_digits': '1234567890',
                'nonblocking': True,
            },
            'say_success': {
                'text': _('Я распознала %(city)s, благодарю Вас!.'),
            },
            'say_fail': {
                'text': _('Увы, но мне не удалось распознать город.'),
            },
            'attempts': {
                # Количество итераций.
                'count': 3,
                # Максимальное время одной итерации.
                'iter_time': 10,
                # Размер пауз для ожидания ответа во время одной итерации.
                'iter_pause': 0.5,
                'new_buffer': True,
                'say': {
                    'text': _('Я не поняла Ваш ответ, попробуйте сказать ещё раз.'),
                },
            },
        },
        # Этот блок-скрипт запустит плагин, установит переменную, озвучит её
        # и установит результат False для последовательности `fail`.
        '004': {
            'type': 'simple_say',
            'new_buffer': True,
            'plugin_before': 'example.py',
            'say_start': {
                'text': '%(example_plugin_var)s',
            }
        },
        '005': {
            'type': 'simple_say',
            'new_buffer': True,
            'say_start': {
                'text': _('Всего хорошего! До свидания.'),
            }
        },
    }
}


def create_dirs(work_dir):
    dirs = (
        path_join(work_dir, 'config'),
        path_join(work_dir, 'dialogs'),
        path_join(work_dir, 'modules'),
        path_join(work_dir, 'logs'),
        path_join(work_dir, 'export'),
        path_join(work_dir, 'plugins'),
        path_join(work_dir, 'processors'),
    )
    for directory in dirs:
        makedirs(directory, 0o700, exist_ok=True)
    makedirs(path_join(work_dir, 'storage'), 0o755, exist_ok=True)


def get_dialog_scheme(work_dir, name, raise_error=False):
    if not name.lower().endswith('.json'):
        name += '.json'

    filename = path_join(work_dir, 'dialogs', name)

    if not exists(filename):
        if raise_error:
            msg = _('Диалог %r не найден') % filename
            raise ImproperlyConfigured(msg)

        if name != 'default.json':
            logger.error(_(
                'Диалог "%s" не найден, будет использоваться диалог '
                '"default.json".'
            ) % name)

        filename = path_join(work_dir, 'dialogs', 'default.json')

        if not exists(filename):
            json.dump(
                DEFAULT_DIALOG, open(filename, 'w'),
                indent=4, ensure_ascii=False)
            logger.info(_('Создан диалог "default.json".'))

            return DEFAULT_DIALOG

    scheme = json.load(open(filename, 'r'))
    return scheme


def get_plugin(work_dir, name, raise_error=False):
    filename = path_join(work_dir, 'plugins', name)

    if not exists(filename):
        internal = path_join(BASE_DIR, 'plugins')
        filename = path_join(internal, name)

        if not exists(filename):
            if raise_error:
                msg = _('Плагин с именем %r не найден.') % name
                raise ImproperlyConfigured(msg)

            logger.error(_('Плагин с именем %r не найден.'), name)
            filename = path_join(internal, 'example.py')

    return filename


def get_processor(work_dir, name, raise_error=False):
    filename = path_join(work_dir, 'processors', name)

    if not exists(filename):
        internal = path_join(BASE_DIR, 'processors')
        filename = path_join(internal, name)

        if not exists(filename):
            if raise_error:
                msg = _('Процессор с именем %r не найден.') % name
                raise ImproperlyConfigured(msg)

            logger.error(_('Процессор с именем %r не найден.'), name)
            filename = path_join(internal, 'example.py')

    return filename


def get_config(work_dir, default, name):
    filename = path_join(work_dir, 'config', '%s.json' % name)
    if not exists(filename):
        json.dump(default, open(filename, 'w'), indent=4)
    else:
        default.update(json.load(open(filename, 'r')))
    return default


def get_main_config(work_dir):
    default = {
        'recognizer': 'astersay.backends.yandex.YandexRecognizer',
        'synthesizer': 'astersay.backends.yandex.YandexSynthesizer',
        'morphology_processor': 'astersay.morphology.Pymorphy2Processor',
        'export': '{work_dir}/export/{date}/{dialog}_{time}.json',
        'remote_export': {
            'active': False,
            'url': 'https://example.com',
            'headers': {},
            'mode': 'data',  # 'data' для отправки json, 'file' для отправка файла
            'delete_local_on_success': True,  # удалить локальный файл в случае успеха
            'retries_on_failure': 3,  # кол-во попыток в случае неудачи
        },
        'disable_stop_voices': False,
    }
    return get_config(work_dir, default, 'main')


def get_logging_config(work_dir):
    default = {
        'version': 1,
        'disable_existing_loggers': False,
        'filters': {
        },
        'formatters': {
            'verbose': {
                'format': '[%(asctime)s] |%(process)08d| %(levelname)08s: %(message)s <%(name)s>'
            },
            # 'short': {
            #     'format': '%(levelname)s <%(name)s>: %(message)s'
            # },
        },
        'handlers': {
            'main': {
                'class': 'logging.FileHandler',
                'filename': path_join(work_dir, 'logs', 'main.log'),
                'formatter': 'verbose',
            },
            'backend': {
                'class': 'logging.FileHandler',
                'filename': path_join(work_dir, 'logs', 'backend.log'),
                'formatter': 'verbose',
            },
            'dialog': {
                'class': 'logging.FileHandler',
                'filename': path_join(work_dir, 'logs', 'dialog.log'),
                'formatter': 'verbose',
            },
        },
        'loggers': {
            'astersay': {
                'handlers': ['main'],
                'level': 'INFO',
            },
            'astersay.backends': {
                'handlers': ['backend'],
                'level': 'DEBUG',
            },
            'astersay.agi': {
                'handlers': ['dialog'],
                'level': 'DEBUG',
            },
            'astersay.dialog': {
                'handlers': ['dialog'],
                'level': 'DEBUG',
            },
            'astersay.conf': {
                'handlers': ['dialog'],
                'level': 'DEBUG',
            },
            'astersay.backends.yandex': {
                'handlers': ['dialog'],
                'level': 'INFO',
            },
            'astersay.backends.vosk': {
                'handlers': ['dialog'],
                'level': 'INFO',
            },
            'astersay.backends.tinkoff': {
                'handlers': ['dialog'],
                'level': 'INFO',
            },
        }
    }
    return get_config(work_dir, default, 'logging')


def get_yandex_config(work_dir):
    default = {
        'auth': {
            'private_filename': path_join(work_dir, 'yandex_private.pem'),
            'token_filename': path_join(work_dir, 'yandex_token.json'),
            'key_id': '',
            'service_account_id': '',
            'folder_id': '',
        },
        'recognizer': {
            'model': 'general',
            'audio_encoding': 'LINEAR16_PCM',
            'chunk_size': 1024,
            'language_code': 'ru-RU',
            'partial_results': True,
            'profanity_filter': False,
            'single_utterance': False,
            'raw_results': False,
            'sample_rate_hertz': 8000,
        },
        'synthesizer': {
            'emotion': 'neutral',
            'format': 'lpcm',
            'lang': 'ru-RU',
            'sample_rate_hertz': 48000,
            'speed': 1.0,
            'storage': path_join(work_dir, 'storage'),
            'voice': 'oksana',
            'convertor': {
                'command': (
                    'sox -t raw -r 48k -b 16 -e signed-integer -c 1 "%s" '
                    '-t wav -r 8k -c 1 "%s"'
                ),
                'src_format': 'raw',
                'src_delete': True,
            }
        },
    }
    return get_config(work_dir, default, 'yandex')


def get_vosk_config(work_dir):
    default = {
        'connection': {
            'host': 'localhost',
            'port': 2700,
        },
        'recognizer': {
            'chunk_size': 8000,
            'max_size': 10485760,
            'max_time': 300,
            'sample_rate_hertz': 8000,
        },
    }
    return get_config(work_dir, default, 'vosk')


def get_tinkoff_config(work_dir):
    default = {
        'auth': {
            'api_key': '',
            'private_filename': path_join(work_dir, 'tinkoff_private.pem'),
            'token_filename': path_join(work_dir, 'tinkoff_token.json'),
            'service_account_id': '',
            'sub': ''
        },
        'recognizer': {
            'model': 'general',
            'audio_encoding': 'LINEAR16',
            'chunk_size': 1024,
            'language_code': 'ru-RU',
            'profanity_filter': False,
            'sample_rate_hertz': 8000,
            'enable_automatic_punctuation': False,
            'enable_interim_results': False,
            'interim_results_interval': 1.0
        },
        'synthesizer': {
            'sample_rate_hertz': 48000,
            'speed': 1.0,
            'storage': path_join(work_dir, 'storage'),
            'voice': 'alyona',
            'lang': 'ru-RU',
            'format': 'lpcm',
            'convertor': {
                'command': (
                    'sox -t raw -r 48k -b 16 -e signed-integer -c 1 "%s" '
                    '-t wav -r 8k -c 1 "%s"'
                ),
                'src_format': 'raw',
                'src_delete': True,
            }
        }
    }
    return get_config(work_dir, default, 'tinkoff')


def make_export_data(agi_params_data: dict, export_data: dict,
                     text_buffers: dict, **extra):
    data = {
        'agi': agi_params_data,
        'export': export_data,
        'speech': text_buffers,
    }
    if extra:
        assert 'agi' not in extra
        assert 'export' not in extra
        assert 'speech' not in extra
        data.update(extra)
    return data


def check_pauses(script_name, pauses):
    assert isinstance(pauses, dict), \
        _('Поле "pauses" в скрипте %r должно '
          'быть словарём.') % script_name
    attrs = (
        'after,'
        'before',
        'after_say_start',
        'before_say_start',
        'after_say_success',
        'before_say_success',
        'after_say_fail',
        'before_say_fail',
        'after_say_attempt',
        'before_say_attempt',
    )

    for attr in attrs:
        if attr in pauses:
            assert isinstance(pauses[attr], (int, float)), (
                _('Поле "pauses.%(attr)s" в скрипте %(script)r должно '
                  'быть числом.') % {'attr': attr, 'script': script_name}
            )
    return True


def check_commands(script_name, commands):
    assert isinstance(commands, dict), \
        _('Поле "commands" в скрипте %r должно '
          'быть словарём.') % script_name
    attrs = (
        'after,'
        'before',
        'after_say_start',
        'before_say_start',
        'after_say_success',
        'before_say_success',
        'after_say_fail',
        'before_say_fail',
        'before_say_success',
        'after_say_attempt',
        'before_say_attempt',
    )

    for attr in attrs:
        if attr in commands:
            assert isinstance(commands[attr], list), (
                _('Поле "commands.%(attr)s" в скрипте %(script)r должно '
                  'быть списком.') % {'attr': attr, 'script': script_name}
            )
    return True


def check_saydata(script_name, key, saydata):
    assert isinstance(saydata, dict), \
        _('Поле "%(key)s" в скрипте %(script)r должно '
          'быть словарём.') % {'key': key, 'script': script_name}

    text = saydata.get('text')
    file = saydata.get('file')
    voice = saydata.get('voice')
    texts = saydata.get('texts')
    assert text or file or voice or texts, \
        _('Поле "%(key)s" в скрипте %(script)r должно включать текст или '
          'путь к файлу.') % {'key': key, 'script': script_name}

    if 'escape_digits' in saydata:
        v = saydata['escape_digits']
        assert v and isinstance(v, (str, list)), \
            _('Поле "%(key)s.escape_digits" в скрипте %(script)r должно быть '
              'строкой или списком.') % {'key': key, 'script': script_name}

    # if 'nonblocking' in saydata:
    #     pass

    return True


class Settings:
    """
    Конструктор для объекта управления настройками запускаемого приложения.
    """

    work_dir = None
    dialog_name = 'default'
    main = None
    logging = None
    yandex = None
    vosk = None
    tinkoff = None

    def configure(self):
        self.work_dir = work_dir = abspath(self.work_dir or DEFAULT_WORK_DIR)
        create_dirs(work_dir)
        # TODO: в версии 0.30 убрать `dialogs` в пользу `modules`
        # Каталог, где не только диалоги, но и импортируемые классы диалогов.
        sys.path.append(path_join(work_dir, 'dialogs'))
        # Каталог для импортируемых модулей, содержищих классы диалогов и
        # другие необходимые для расширения функционала вещи.
        sys.path.append(path_join(work_dir, 'modules'))

        self.main = get_main_config(work_dir)
        self.logging = get_logging_config(work_dir)
        self.yandex = get_yandex_config(work_dir)
        self.vosk = get_vosk_config(work_dir)
        self.tinkoff = get_tinkoff_config(work_dir)

        self.reconfigure_logging()

    def reconfigure_logging(self, logging=None):
        logging = logging or self.logging
        root = getLogger()
        map(root.removeHandler, root.handlers[:])
        map(root.removeFilter, root.filters[:])
        dictConfig(logging)

    def get_dialog_class(self):
        """Возвращает кастомный или базовый класс диалога."""
        name = self.dialog_scheme.get('dialog_class')
        if not name:
            name = self.main.get('dialog_class', 'astersay.dialog.BaseDialog')
        cls = import_string(name)
        logger.info(_('Используется класс диалога %r.'), cls)
        return cls

    @property
    def dialog_scheme(self):
        """Динамическая загрузка внешних изменений модели диалога."""
        return get_dialog_scheme(self.work_dir, self.dialog_name)

    def set_dialog_name(self, name):
        name = prepare_dialog_name(name or '')
        if name:
            self.dialog_name = name
        return self.dialog_name

    def get_recognizer(self, backend=None, **params):
        """
        Возвращает настроенный объект распознавателя.
        """
        if backend:
            suffix = '_%s' % make_checksum({
                'backend': backend,
                'params': params,
            })
        else:
            suffix = ''
        attr = '_recognizer%s' % suffix
        if not hasattr(self, attr):
            if not backend:
                backend = self.main['recognizer']
            Recognizer = import_string(backend)
            setattr(self, attr, Recognizer(self, extra=params))
        return getattr(self, attr)

    def get_synthesizer(self, backend=None, **params):
        """
        Возвращает настроенный объект синтезатора. Для уровня диалога в
        качестве уникальной строки задайте "_<backend>_<hash params>".
        """
        logger.info('Backend %s, params %s', backend, params)
        if backend:
            suffix = '_%s' % make_checksum({
                'backend': backend,
                'params': params,
            })
        else:
            suffix = ''
        attr = '_synthesizer%s' % suffix
        if not hasattr(self, attr):
            if not backend:
                backend = self.main['synthesizer']
            Synthesizer = import_string(backend)
            setattr(self, attr, Synthesizer(self, extra=params))
        return getattr(self, attr)

    def get_morphology_processor(self, raise_error=False):
        module = self.dialog_scheme.get('morphology_processor')
        if not module:
            module = self.main.get(
                'morphology_processor',
                'astersay.morphology.Pymorphy2Processor')
        try:
            Processor = import_string(module)
        except ImportError as e:
            logger.error(_('Модуль %s не установлен.'), module, exc_info=e)
            if raise_error:
                raise e
            Processor = import_string('astersay.morphology.Pymorphy2Processor')
        return Processor()

    def get_morphology_pattern(self):
        if self.main['morphology']:
            pattern = self.main['morphology_pattern']
            if pattern:
                return re.compile(pattern)
        return None

    def get_plugin(self, name):
        """
        Возвращает полный путь к гарантированно существующему файлу плагина.
        Когда плагина нет, то вернёт путь к файлу примера.
        """
        if name.startswith('/') and exists(name):
            return name
        return get_plugin(self.work_dir, name)

    def get_processor(self, name):
        """
        Возвращает полный путь к гарантированно существующему файлу внешнего
        обработчика. Когда такого обработчика нет, то вернёт путь к файлу
        примера.
        """
        if name.startswith('/') and exists(name):
            return name
        return get_processor(self.work_dir, name)

    def export_dialog(self, agi_params_data: dict, export_data: dict,
                      text_buffers: dict, **extra):
        export = self.main.get('export')
        if not export:
            return

        now = datetime.now()
        date = now.date()
        time = now.time()
        kw = {
            'work_dir': self.work_dir,
            'dialog': self.dialog_name,
            'now': now.isoformat(),
            'date': date.isoformat(),
            'time': time.isoformat(),
            'year': date.year,
            'month': date.month,
            'day': date.day,
        }
        filename = export.format(**kw)
        makedirs(dirname(filename), 0o700, exist_ok=True)
        data = make_export_data(
            agi_params_data,
            export_data,
            text_buffers,
            dialog=self.dialog_name,
            workdir=self.work_dir,
            pid=getpid(),
            **extra)
        json.dump(data, open(filename, 'w'),
                  indent=4, ensure_ascii=False)
        self.remote_export_dialog(filename, data)
        return filename

    def remote_export_dialog(self, filename, data=None):
        export = self.main.get('remote_export')
        if not export.get('active'):
            return
        assert export['mode'] in ('file', 'data')
        assert export['retries_on_failure'] >= 0

        logger_info = logger.info
        logger_error = logger.error
        request_url = export['url']
        request_kwargs = {
            'headers': export.get('headers', {}),
            'timeout': export.get('timeout', (2, 5)),
        }

        if export['mode'] == 'file':
            request_kwargs['files'] = {'file': (
                basename(filename),
                open(filename, 'rb'),
                'application/json',
                {},
            )}
        else:
            # В любом другом случае мы всё равно должны отправить данные.
            if not data:
                data = json.load(open(filename))
            request_kwargs['json'] = data

        def send(attempts):
            for n in range(attempts):
                try:
                    res = requests.post(request_url, **request_kwargs)
                    try:
                        data = res.json()
                    except Exception:
                        data = res.text
                    assert res.status_code == 200, _(
                        'Не удалось экспортировать диалог на удалённый сервис. '
                        'Сервер ответил кодом %(code)r: %(data)s'
                    ) % {
                        'code': res.status_code,
                        'data': data,
                    }
                except AssertionError as e:
                    logger_error(str(e))
                except requests.exceptions.Timeout:
                    logger_error(
                        _('Timeout при экспорте диалога на удаленный сервер.'))
                except requests.exceptions.RequestException as e:
                    logger_error(
                        _('Ошибка при экспорте диалога на удаленный сервер: %s'),
                        e, exc_info=e)
                else:
                    logger_info(
                        _('Диалог экспортирован на удаленный сервер %(url)s '
                          'в режиме %(mode)s'),
                        {'url': request_url, 'mode': export['mode']})
                    if export['delete_local_on_success'] and filename:
                        try:
                            remove(filename)
                        except FileNotFoundError:
                            logger_error(
                                _('Локальный файл диалога %s не найден.'),
                                filename)
                        else:
                            logger_info(_('Локальный файл диалога %s удален'),
                                        filename)
                    return True
            return False

        # Первая попытка выполняется в текущем контексте, чтобы можно было
        # гарантировать успешность доставки. Это бывает необходимо для
        # продолжения каких-либо действий в астериске.
        # Если первая попытка была неуспешной, то остальные выполняются в
        # отдельном потоке.

        success = send(1)
        retries = export['retries_on_failure']

        if not success and retries:
            t = Thread(target=send, args=(retries,))
            t.start()

    def get_stop_file(self):
        if self.main.get('disable_stop_voices'):
            logger.info(_('Остановка голоса отключена в настройках.'))
            return ''
        filename = path_join(BASE_DIR, 'sounds', 'stop_voice_file.wav')
        return filename if exists(filename) else ''

    def validate(self, scheme=None):
        """
        Проверяет каталоги, настройки, модель диалога и поднимает ошибку.
        """
        work_dir = self.work_dir
        assert work_dir, _('Не установлен рабочий каталог.')

        create_dirs(work_dir)

        if scheme is None:
            assert self.dialog_name, _('Не установлено имя диалога.')
            scheme = get_dialog_scheme(
                work_dir, self.dialog_name, raise_error=True)

        Dialog = self.get_dialog_class()

        self.get_morphology_processor(raise_error=True)

        main_script = scheme.get('main_script')
        assert main_script, \
            _('Поле "main_script" пустое или отсутствует.')
        assert isinstance(main_script, list), \
            _('Поле "main_script" должно быть списком.')

        scripts = scheme.get('scripts')
        assert scripts, \
            _('Поле "scripts" пустое или отсутствует.')
        assert isinstance(scripts, dict), \
            _('Поле "scripts" должно быть словарём.')

        # Определённые в main_script.
        defined_processes = set()
        # Чётко заданные в fail и succes.
        mentioned_processes = set()
        # Заданные в fail и succes в виде переменных.
        mentioned_var_processes = set()

        def dispatch_mentioned(processes):
            for p in processes:
                if '%(' in p:
                    m = mentioned_var_processes
                else:
                    m = mentioned_processes
                m.add(p)

        for i, process in enumerate(main_script):
            name = process.get('name')
            assert name, \
                _('Поле "name" отсутствует в скрипте %d.') % i

            defined_processes.add(name)

            for result in ('fail', 'success'):
                if result in process:
                    f = process[result]
                    assert f and isinstance(f, (str, dict)), \
                        _('Поле %(field)r в скрипте %(script)r должно быть строкой '
                          'или словарём.') % {'field': f, 'script': name}
                    if isinstance(f, str):
                        dispatch_mentioned((f,))
                    else:
                        dispatch_mentioned(f.values())

            if 'finish' in process:
                finish = process['finish']
                assert isinstance(finish, bool), \
                    _('Поле "finish" в скрипте %r должно быть булево.') % name

            if 'say_debug' in process:
                say_debug = process['say_debug']
                assert isinstance(say_debug, bool), \
                    _('Поле "say_debug" в скрипте %r должно быть булево.') % name

            if 'group' in process:
                group = process['group']
                assert group and isinstance(group, str), \
                    _('Поле "group" в скрипте %r должно быть строкой.') % name

            if 'plugin' in process:
                plugin = process['plugin']
                assert plugin and isinstance(plugin, str), \
                    _('Поле "plugin" в скрипте %r должно быть строкой.') % name
                get_plugin(work_dir, plugin, raise_error=True)

            script = scripts.get(name)
            assert script, \
                _('Скрипт %r отсутствует в поле "scripts".') % name

            script_type = script.get('type')
            assert script_type and isinstance(script_type, str), \
                _('Поле "type" в скрипте %r должно быть строкой.') % name

            m = '_script_%s' % script_type
            method = getattr(Dialog, m, None)
            assert method and callable(method), (
                _('Метод "%(cls)s.%(method)s" не определён.') % {
                    'cls': Dialog.__name__,
                    'method': m,
                }
            )

            if 'synthesizer' in script:
                v = script['synthesizer']
                assert isinstance(v, dict), \
                    _('Поле "synthesizer" в скрипте %r должно '
                      'быть словарём.') % name

            if 'partials_begin' in script:
                v = script['partials_begin']
                assert isinstance(v, int), \
                    _('Поле "partials_begin" в скрипте %r должно '
                      'быть целым.') % name

            if 'export_speech' in script:
                v = script['export_speech']
                assert v and isinstance(v, str), \
                    _('Поле "export_speech" в скрипте %r должно '
                      'быть строкой.') % name

            if 'export_name' in script:
                v = script['export_name']
                assert v and isinstance(v, str), \
                    _('Поле "export_name" в скрипте %r должно '
                      'быть строкой.') % name

            if not script_type.startswith('simple_'):
                assert 'export_name' in script, \
                    _('Поле "export_name" в скрипте %r должно '
                      'быть oбязательно.') % name

            if 'export_name_text' in script:
                v = script['export_name_text']
                assert v and isinstance(v, str), \
                    _('Поле "export_name_text" в скрипте %r должно '
                      'быть строкой.') % name

            if 'file' in script:
                v = script['file']
                assert v and isinstance(v, str), \
                    _('Поле "file" в скрипте %r должно '
                      'быть строкой.') % name

            if script_type == 'text_processing':
                assert 'file' in script, \
                    _('Поле "file" в скрипте %r должно '
                      'быть oбязательно.') % name
                get_processor(work_dir, script['file'], raise_error=True)

            if 'pauses' in script:
                check_pauses(name, script['pauses'])

            if 'commands' in script:
                check_commands(name, script['commands'])

            for key in ('say_start', 'say_success', 'say_fail'):
                saydata = script.get(key)
                # Пустой словарь может быть, но он будет пропущен.
                if saydata:
                    check_saydata(name, key, saydata)

        # Теперь проверяется соответствие упомянутых с определёнными.
        undefined = mentioned_processes.difference(defined_processes)
        assert not undefined, \
            _('Скрипты %r не определены.') % ', '.join(map(str, undefined))

        # TODO: Сделать проверку `mentioned_var_processes`.

        if 'constants' in scheme:
            assert isinstance(scheme['constants'], dict), \
                _('Поле "constants" должно быть словарём.')

        if 'variables' in scheme:
            assert isinstance(scheme['variables'], dict), \
                _('Поле "variables" должно быть словарём.')

        if 'recognizer' in scheme:
            assert isinstance(scheme['recognizer'], dict), \
                _('Поле "recognizer" должно быть словарём.')

        if 'synthesizer' in scheme:
            assert isinstance(scheme['synthesizer'], dict), \
                _('Поле "synthesizer" должно быть словарём.')


settings = Settings()
