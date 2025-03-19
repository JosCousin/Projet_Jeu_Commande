from abc import ABC, abstractmethod

class IChoixNom(ABC):
    @abstractmethod
    def choixNom(self):
        pass