from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Dict

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

_CONF_READER_FUNCS = {".yaml": read_yaml, ".json": read_json}

class BaseReader(ABC):

    @abstractmethod
    def _load(self) -> None:
        pass

    @abstractproperty
    def data(sefl) -> Any:
        pass

class ConfigReader(BaseReader):

    def __init__(self, path: str) -> None:
        self._path = path
        self._data = None
        self._extension = get_file_extension(path)
    
    def _is_valid_extension(self):
        return self._extension in _CONF_READER_FUNCS.keys()
    
    def _load(self) -> None:
        if self._is_valid_extension():
            self._data = _CONF_READER_FUNCS[self._extension](self._path)
        else:
            raise ValueError(f"{self._path} is not a valid config file.")

    @property
    def data(self) -> Dict:
        if not self._data:
            self._load()
        return self._data
