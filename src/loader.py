from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Dict, List, Sequence, Union

from .utils import *

def get_config_file_from_dir(path: str) -> List[str]:
    extensions = _READERS.keys()
    files = get_file_list_from_dir(path)
    config_files = [x for x in files if get_file_extension(x) in extensions]
    return config_files

class BaseLoader(ABC):

    @abstractmethod
    def _read(self) -> None:
        pass

    @abstractproperty
    def data(self) -> Any:
        pass
    
class ConfigLoader(BaseLoader):

    def __init__(self, path: str) -> None:
        self._path = path
        self._data = None
        self._extension = get_file_extension(path)
    
    def _load(self) -> None:
        self._data = _READERS[self._extension](self._path)
    
    @property
    def data(self):
        if not self._data:
            self._load()
        return self._data
    

    

