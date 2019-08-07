from functools import wraps
from universe_bot.logger import logger
import inspect

LOG = logger()


def load(func):
    @wraps(func)
    def _wrapper(*args, **kwargs):
        LOG.debug('Loading function: ' + func.__name__)
        func(*args, **kwargs)
        LOG.debug('Loaded function: ' + func.__name__)

    return _wrapper
