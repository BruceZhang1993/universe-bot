from threading import Thread
from universe_bot.backend import available_backends


def connection(backend=None, name=None):
    if backend:
        backend_module = None
        try:
            backend_module = available_backends[backend]
        except KeyError:
            pass
        return 'Connection: ' + name + ' Backend: ' + backend + ' Module: ' + str(backend_module)
    return None
