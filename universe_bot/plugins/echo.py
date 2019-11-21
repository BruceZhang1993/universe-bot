from universe_bot.core.plugin import log

__name__ = 'echo'
__alias__ = 'Echo Plugin'
__version__ = '0.0.1'
__description__ = 'Simple Echo Plugin'
__author__ = 'Bruce Zhang'
__license__ = 'MIT'


def register():
    log().info('plugin register')


def unregister():
    log().info('plugin unregister')
