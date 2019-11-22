import functools

from universe_bot.logger import logger


def log():
    return logger('plugin')


def command(cmd):
    def inner(func):
        @functools.wraps(command)
        def wrapper(source, target, arguments):
            log().debug('Received: {}'.format(arguments))
            func(source, target, arguments)
        wrapper.__cmd__ = cmd
        return wrapper
    return inner
