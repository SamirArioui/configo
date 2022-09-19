from abc import ABC, abstractmethod
from .utils import *

class BaseLoader(ABC):

    @abstractmethod
    def _load(self):
        pass