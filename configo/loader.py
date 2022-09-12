from typing import Dict
from abc import ABC, abstractmethod

import yaml
from yaml.loader import SafeLoader

class BaseLoader(ABC):

    @abstractmethod
    def load(self)->Dict:
        pass

class YamlLoader(BaseLoader):

    EXTENSION = "YAML"

    def __init__(self, path:str) -> None:
        self.path = path
    
    def load(self):
        with open(self.path) as file:
            data = yaml.load(file, Loader=SafeLoader)
        return data
