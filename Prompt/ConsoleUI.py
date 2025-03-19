from Prompt.IUserInterface import IUserInterface

class ConsoleUI(IUserInterface):
    def display(self, message: str):
        print(message)

    def get_input(self, prompt: str) -> str:
        return input(prompt)