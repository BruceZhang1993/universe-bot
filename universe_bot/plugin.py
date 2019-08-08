import os
import pathlib
import importlib.util
from universe_bot.consts import PLUGIN_DIRS

LOADED_PLUGINS = {}


def find_all_plugins():
    plugins = []
    for dir in PLUGIN_DIRS:
        plugins.extend(list(map(lambda path: {'name':path.name.rstrip('.py'),'path':path}, map(lambda f: pathlib.Path(dir) / f,
                filter(lambda f: f.endswith('.py') and f != '__init__.py', os.listdir(dir))))))
    return plugins


def register_all_plugins():
    for plugin in find_all_plugins():   
        spec = importlib.util.spec_from_file_location("unibot.plugin." + plugin['name'], plugin['path'])
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        LOADED_PLUGINS[plugin['name']] = foo
    return LOADED_PLUGINS
