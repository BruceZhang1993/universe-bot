import universe_bot

from universe_bot.logger import logger
from universe_bot.config import Config
from universe_bot.backend import available_backends
from universe_bot import app

RESERVED = ['__alias__', '__author__', '__builtins__', '__cached__', '__description__', '__doc__', '__file__',
            '__license__', '__loader__', '__name__', '__package__', '__spec__', '__version__', 'command', 'log']


class Connector(object):
    def __init__(self, name, backend, params=None, plugins=None):
        self.name = name
        self.backend = backend
        self.params = params
        self.plugins = plugins

    def start(self):
        self.register_plugins()
        try:
            self.backend.__start__(self.name, self.params)
        except BaseException as e:
            logger().warning(e)

    def register_plugins(self):
        names = list(filter(lambda x: x not in RESERVED, dir(self.plugins['echo'])))
        for name in names:
            print(getattr(self.plugins['echo'], name).__name__)
            print(getattr(self.plugins['echo'], name).__cmd__)
            getattr(self.plugins['echo'], name)('1', '2', '3')

    def stop(self):
        try:
            self.backend.__stop__(self.name, self.params)
        except BaseException as e:
            logger().warning(e)

    def __str__(self):
        return 'Telegram backend: {}'.format(self.name)


def connection(name=None, c: dict = None, plugins=None):
    conn: Connector
    if c and c.get('backend'):
        backend_module = None
        try:
            backend_module = available_backends[c['backend']]
            params = Config().get('connections.' + name)
            conn = Connector(name, backend_module, params=params, plugins=plugins)
            app.STARTED_CONNECTIONS.append(conn)
            conn.start()
        except KeyError:
            logger().warning(c['backend'] + ' backend is not supported.')
    return None
