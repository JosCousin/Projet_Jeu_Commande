from abc import ABC, abstractmethod
from Personnage.Personnage import Personnage

class IMouvement(ABC):
    @abstractmethod
    def move(self, personnage: Personnage):
        pass