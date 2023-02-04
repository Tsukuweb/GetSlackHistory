import yaml


class DotDict(dict):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.__dict__ = self


def load_config(config_path):

    with open(config_path,encoding="utf8") as f:
        config = DotDict(yaml.safe_load(f)['config'])
    
    return config