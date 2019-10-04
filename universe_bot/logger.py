import os
import logging
import logging.config
from universe_bot.consts import LOGGER_CONFIG, LOG_FILE, PLUGIN_DIRS, CONF_FILE

CURRENT_LOGGER: logging.Logger


def ensure_dirs():
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))
    if not os.path.exists(PLUGIN_DIRS[1]):
        os.makedirs(PLUGIN_DIRS[1])
    if not os.path.exists(os.path.dirname(CONF_FILE)):
        os.makedirs(os.path.dirname(CONF_FILE))


def initialize_logger(debug=False):
    """ Initialize logger"""
    if debug:
        LOGGER_CONFIG['loggers']['root'] = LOGGER_CONFIG['loggers']['debug']
        LOGGER_CONFIG['loggers']['plugin'] = LOGGER_CONFIG['loggers']['plugin-d']
        LOGGER_CONFIG['loggers']['backend'] = LOGGER_CONFIG['loggers']['backend-d']
    else:
        LOGGER_CONFIG['loggers']['root'] = LOGGER_CONFIG['loggers']['uni']
        LOGGER_CONFIG['loggers']['plugin'] = LOGGER_CONFIG['loggers']['plugin-c']
        LOGGER_CONFIG['loggers']['backend'] = LOGGER_CONFIG['loggers']['backend-c']
    logging.config.dictConfig(LOGGER_CONFIG)


def logger(_logger='root'):
    return logging.getLogger(_logger)
