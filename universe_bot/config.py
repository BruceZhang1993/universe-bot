import yaml
from shutil import copyfile
from universe_bot.utils import singleton, get_config, set_config
from universe_bot.consts import CONF_FILE
from universe_bot.logger import logger


@singleton
class Config:
    conf_file = None
    config = {}

    def __init__(self, conf_file = None):
        if not conf_file:
            conf_file = CONF_FILE
        self.conf_file = conf_file
        with open(self.conf_file, 'r') as file:
            self.config = yaml.safe_load(file)

    def reload(self):
        with open(self.conf_file, 'r') as file:
            self.config = yaml.safe_load(file)

    @property
    def all(self):
        return self.config

    def get(self, key: str = None):
        if not key:
            return None
        else:
            return get_config(self.config, key)

    def set(self, key: str, val, save=False):
        self.config = set_config(self.config, key, val)
        return self.config

    def save(self, backup=True):
        try:
            if backup:
                copyfile(self.conf_file, str(self.conf_file.resolve()) + '.orig')
            with open(self.conf_file, 'w') as file:
                yaml.dump(self.config, file)
            return True
        except:
            logger().warning('Error saving config file')
            return False
