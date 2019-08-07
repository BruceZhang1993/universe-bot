import pathlib
from time import strftime
from appdirs import user_config_dir, user_log_dir

APPNAME = 'UniverseBot'

LOG_FILE = pathlib.Path(user_log_dir(APPNAME)) / (strftime('%Y-%m-%d') + '.log')

LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': "[%(levelname)s] %(message)s (%(filename)s::%(funcName)s::%(lineno)d) -- %(asctime)s",
        },
        'console': {
            'format': "[%(levelname)s] %(message)s",
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'console',
            'class': 'logging.StreamHandler'
        },
        'console_debug': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a'
        },
        'file_debug': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a'
        },
    },
    'loggers': {
        'uni': {
            'handlers': ['file_debug', 'console'],
            'level': 'DEBUG',
        },
        'uni-file': {
            'handlers': ['file_debug'],
            'level': 'DEBUG',
        },
        'debug': {
            'handlers': ['file_debug', 'console_debug'],
            'level': 'DEBUG',
        }
    },
}