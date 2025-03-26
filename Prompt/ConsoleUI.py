from Prompt.IUserInterface import IUserInterface

class ConsoleUI(IUserInterface):
    def display(self, message):
        print(message)

    def get_input(self, prompt) -> str:
        return input(prompt)