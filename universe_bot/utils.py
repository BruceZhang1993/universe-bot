def get_config(config: dict, key: str):
    key_path = key.split('.')
    for key in key_path:
        if not key:
            continue
        if isinstance(config, dict):
            config = config.get(key)
        elif isinstance(config, list):
            try:
                config = config[int(key)]
            except IndexError:
                return None
        else:
            return None
    return config

def set_config(config: dict, key: str, val):
    tmp = config
    key_path = key.split('.')
    real_path = []
    for key in key_path:
        if not key:
            continue
        if isinstance(tmp, dict):
            tmp = tmp.get(key)
            real_path.append(key)
        elif isinstance(tmp, list):
            try:
                tmp = tmp[int(key)]
                real_path.append(int(key))
            except IndexError:
                return config
        else:
            return config
    real_path = ''.join(map(lambda s: "[" + s + "]" if isinstance(s, int) else "['" + s + "']", real_path))
    exec("config" + real_path + " = val")
    return config

def singleton(cls):
    _instance = {}

    def inner(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]
    return inner
