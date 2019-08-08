import yaml
from shutil import copyfile
from universe_bot.utils import singleton, get_config, set_config


@singleton
class Config:
    conf_file = None
    config = {}

    def __init__(self, conf_file = None):
        self.conf_file = conf_file
        with open(self.conf_file, 'r') as file:
            self.config = yaml.safe_load(file)

    @property
    def all(self):
        return self.config

    def __getattribute__(self, key):
        return self.get(key)

    def get(self, key: string = None):
        if not key:
            return self.all
        else:
            return get_config(self.config, key)

    def set(self, key: string, val, save=False):
        self.config = set_config(self.config, key, val)
        return self.config

    def save(self, backup=True):
        if backup:
            copyfile(self.conf_file, self.conf_file + '.orig')
        with open(self.conf_file, 'w') as file:
            yaml.dump(self.config, file)
