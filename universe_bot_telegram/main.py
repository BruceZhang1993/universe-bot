import time

from universe_bot.core.backend import log


class UnibotTelegram(object):
    loop = True

    def __init__(self, name, params):
        self.name = name
        self.params = params

    def run(self):
        print(self.name, self.params)
        while self.loop:
            time.sleep(1)

    def stop(self):
        self.loop = False
        log().info('Telegram backend {} is quitting.'.format(self.name))
