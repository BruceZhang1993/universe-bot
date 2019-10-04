import universe_bot

from universe_bot.logger import logger
from universe_bot.config import Config
from universe_bot.backend import available_backends
from universe_bot import app


class Connector(object):
    def __init__(self, name, backend, params=None):
        self.name = name
        self.backend = backend
        self.params = params

    def start(self):
        try:
            self.backend.__start__(self.name, self.params)
        except BaseException as e:
            logger().warning(e)

    def stop(self):
        try:
            self.backend.__stop__(self.name, self.params)
        except BaseException as e:
            logger().warning(e)

    def __str__(self):
        return 'Telegram backend: {}'.format(self.name)


def connection(name=None, c: dict = None):
    conn: Connector
    if c and c.get('backend'):
        backend_module = None
        try:
            backend_module = available_backends[c['backend']]
            params = Config().get('connections.' + name)
            conn = Connector(name, backend_module, params=params)
            app.STARTED_CONNECTIONS.append(conn)
            conn.start()
        except KeyError:
            logger().warning(c['backend'] + ' backend is not supported.')
    return None
