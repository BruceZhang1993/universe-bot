import os
import logging
import logging.config
from universe_bot.consts import LOGGER_CONFIG, LOG_FILE


def ensure_dirs():
    if not os.path.exists(os.path.dirname(LOG_FILE)):
        os.makedirs(os.path.dirname(LOG_FILE))

def initialize_logger(debug=False):
    """ Initialize logger"""
    if debug:
        LOGGER_CONFIG['loggers'][''] = LOGGER_CONFIG['loggers']['debug']
    else:
        LOGGER_CONFIG['loggers'][''] = LOGGER_CONFIG['loggers']['uni']
    logging.config.dictConfig(LOGGER_CONFIG)

def logger(logger=''):
    return logging.getLogger(logger)