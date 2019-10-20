from abc import ABC, abstractmethod
from universe_bot.logger import logger


def log():
    return logger('backend')


class BaseBackend(ABC):
    name: str
    params: dict

    def __repr__(self):
        return 'Base class of all backends'

    def __init__(self, name, params):
        self.name = name
        self.params = params

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass
