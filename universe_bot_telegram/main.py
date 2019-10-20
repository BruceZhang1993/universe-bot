import time

from universe_bot.core.backend import log, BaseBackend
from universe_bot_telegram import __name__ as mod_name


class UnibotTelegram(BaseBackend):
    loop = True

    def __repr__(self):
        return mod_name

    def __init__(self, name, params):
        super().__init__(name, params)
        log().info('Telegram backend {} loaded.'.format(self.name))

    def run(self):
        print(self.name, self.params)
        while self.loop:
            time.sleep(1)

    def stop(self):
        self.loop = False
        log().info('Telegram backend {} is quitting.'.format(self.name))
