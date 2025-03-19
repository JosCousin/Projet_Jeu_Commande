from abc import ABC, abstractmethod

class IUserInterface(ABC):
    @abstractmethod
    def display(self, message: str):
        pass

    @abstractmethod
    def get_input(self, prompt: str) -> str:
        pass