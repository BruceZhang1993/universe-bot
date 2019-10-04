from universe_bot_telegram.main import UnibotTelegram

__name__ = 'Telegram Backend'
__version__ = '0.0.1'
__url__ = 'https://github.com/BruceZhang1993/universe-bot'
__author__ = 'Bruce Zhang (BruceZhang1993)'
__license__ = 'GPL3'
__email__ = 'zttt183525594@gmail.com'
__description__ = 'Telegram backend for unibot.'
__instance__ = {}


def __start__(name, params):
    global __instance__
    __instance__[name] = UnibotTelegram(name, params)
    __instance__[name].run()


def __stop__(name, _):
    global __instance__
    __instance__[name].stop()
