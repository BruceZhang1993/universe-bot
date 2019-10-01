from universe_bot.logger import logger

from universe_bot.config import Config

from universe_bot.backend import available_backends


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


def connection(name=None, c: dict = None):
    if c and c.get('backend'):
        backend_module = None
        try:
            backend_module = available_backends[c['backend']]
            params = Config().get('connections.' + name)
            Connector(name, backend_module, params=params).start()
        except KeyError:
            logger().warning(c['backend'] + ' backend is not supported.')
    return None
