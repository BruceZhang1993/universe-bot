import os
import pathlib
from time import strftime
from appdirs import user_config_dir, user_log_dir, user_data_dir

APPNAME = 'UniverseBot'

LOG_FILE = pathlib.Path(user_log_dir(APPNAME)) / (strftime('%Y-%m-%d') + '.log')

CONF_FILE = pathlib.Path(user_config_dir(APPNAME)) / 'config.yml'

PLUGIN_DIRS = [
    pathlib.Path(os.path.abspath(os.path.dirname(__file__))) / 'plugins',
    pathlib.Path(pathlib.Path(user_data_dir(APPNAME))) / 'plugins',
]

LOGGER_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'default': {
            'format': "[%(levelname)s] %(message)s (%(filename)s::%(funcName)s::%(lineno)d) -- %(asctime)s",
        },
        'console': {
            'format': "[%(levelname)s] %(message)s",
        },
        'default-backend': {
            'format': "[BACKEND] [%(levelname)s] %(message)s (%(filename)s::%(funcName)s::%(lineno)d) -- %(asctime)s",
        },
        'console-backend': {
            'format': "[BACKEND] [%(levelname)s] %(message)s",
        },
        'default-plugin': {
            'format': "[PLUGIN] [%(levelname)s] %(message)s (%(filename)s::%(funcName)s::%(lineno)d) -- %(asctime)s",
        },
        'console-plugin': {
            'format': "[PLUGIN] [%(levelname)s] %(message)s",
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'formatter': 'console',
            'class': 'logging.StreamHandler'
        },
        'console_backend': {
            'level': 'INFO',
            'formatter': 'console-backend',
            'class': 'logging.StreamHandler'
        },
        'console_plugin': {
            'level': 'INFO',
            'formatter': 'console-plugin',
            'class': 'logging.StreamHandler'
        },
        'console_debug': {
            'level': 'DEBUG',
            'formatter': 'default',
            'class': 'logging.StreamHandler'
        },
        'console_debug_backend': {
            'level': 'DEBUG',
            'formatter': 'default-backend',
            'class': 'logging.StreamHandler'
        },
        'console_debug_plugin': {
            'level': 'DEBUG',
            'formatter': 'default-plugin',
            'class': 'logging.StreamHandler'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'default',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a'
        },
        'file-backend': {
            'level': 'INFO',
            'formatter': 'default-backend',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a'
        },
        'file-plugin': {
            'level': 'INFO',
            'formatter': 'default-plugin',
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
        'file_debug_backend': {
            'level': 'DEBUG',
            'formatter': 'default-backend',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'mode': 'a'
        },
        'file_debug_plugin': {
            'level': 'DEBUG',
            'formatter': 'default-plugin',
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
        },
        'plugin-c': {
            'handlers': ['file_debug_plugin', 'console_plugin'],
            'level': 'DEBUG',
        },
        'plugin-f': {
            'handlers': ['file_debug_plugin'],
            'level': 'DEBUG',
        },
        'plugin-d': {
            'handlers': ['file_debug_plugin', 'console_debug_plugin'],
            'level': 'DEBUG',
        },
        'backend-c': {
            'handlers': ['file_debug_backend', 'console_backend'],
            'level': 'DEBUG',
        },
        'backend-f': {
            'handlers': ['file_debug_backend'],
            'level': 'DEBUG',
        },
        'backend-d': {
            'handlers': ['file_debug_backend', 'console_debug_backend'],
            'level': 'DEBUG',
        },
    },
}
