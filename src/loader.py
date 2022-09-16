from abc import ABC, abstractmethod
from typing import Any, Dict, List, Union

from .utils import *
from .readers import _READERS

def get_config_file_from_dir(path: str) -> List[str]:
    extensions = _READERS.keys()
    files = get_file_list_from_dir(path)
    config_files = [x for x in files if get_file_extension(x) in extensions]
    return config_files

class BaseLoader(ABC):

    @abstractmethod
    def load(self, path: Any) -> Dict:
        pass

    @abstractmethod
    def extension(self, path: Any) -> Any:
        pass
    
    @abstractmethod
    def data(self):
        pass

class SingleFileLoader(BaseLoader):

    def __init__(self) -> None:
        self._is_loaded = False
    
    def load(self, path: str) -> Dict:
        return super().load(path)

    def data(self, path: str):
        data = _READERS[self.extension(path)](path)
        return data
    
    def extension(self, path: str) -> str: 
        return get_file_extension(path)
