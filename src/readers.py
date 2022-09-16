from typing import Dict

import yaml
from yaml.loader import SafeLoader
import json

from .utils import *


def read_yaml(path:str)->Dict:
    with open(path) as file:
        data = yaml.load(file, Loader=SafeLoader)
        return data

def read_json(path:str)->Dict:
    with open(path) as file:
        data = json.load(file)
    return data

_READERS = {".yaml": read_yaml, ".json": read_json}