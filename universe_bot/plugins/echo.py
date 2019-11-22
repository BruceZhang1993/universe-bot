from universe_bot.core.plugin import log, command

__name__ = 'echo'
__alias__ = 'Echo Plugin'
__version__ = '0.0.1'
__description__ = 'Simple Echo Plugin'
__author__ = 'Bruce Zhang'
__license__ = 'MIT'


@command('echo')
def reply_same_text(source, target, arguments):
    pass
