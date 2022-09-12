from typing import Dict

import yaml
from yaml.loader import SafeLoader

def read_yaml(path:str)->Dict:
    with open(path) as file:
        data = yaml.load(file, Loader=SafeLoader)
        return data
