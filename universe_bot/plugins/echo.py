from universe_bot.core import get_logger

__name__ = 'echo'
__alias__ = 'Echo Plugin'
__version__ = '0.0.1'
__description__ = 'Simple Echo Plugin'
__author__ = 'Bruce Zhang'
__license__ = 'MIT'

logger = get_logger()


def register():
    logger.info('plugin register')

def unregister():
    logger.info('plugin unregister')
