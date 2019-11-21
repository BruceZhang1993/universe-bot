import time
from universe_bot.core.backend import log, BaseBackend
from universe_bot_telegram import __name__ as mod_name
from telegram.ext import Updater, CommandHandler


class UnibotTelegram(BaseBackend):
    loop = True
    updater: Updater = None

    def __repr__(self):
        return mod_name

    def __init__(self, name, params):
        super().__init__(name, params)
        self.updater = Updater(params['token'], use_context=True)
        self.updater.dispatcher.add_handler(CommandHandler('start', self.test))
        log().info('Telegram backend {} loaded.'.format(self.name))

    def test(self, update, context):
        update.message.reply_text('Hello, {}!'.format(update.message.from_user.first_name))

    def run(self):
        print(self.name, self.params)
        if self.updater:
            self.updater.start_polling()
        while self.loop:
            time.sleep(1)
        if self.updater:
            self.updater.stop()

    def stop(self):
        self.loop = False
        log().info('Telegram backend {} is quitting.'.format(self.name))
