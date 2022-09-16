from typing import Dict, List

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

def get_config_filepath_from_dir(path: str) -> List[str]:
    extensions = _READERS.keys()
    files = get_file_list_from_dir(path)
    config_files = [x for x in files if get_file_extension(x) in extensions]
    return config_files
    
  
class Loader:

    def __init__(self, path: str) -> None:
        self.path = path
        self.extension = get_file_extension(path)
    
    def load(self):
        return _READERS[self.extension](self.path)
