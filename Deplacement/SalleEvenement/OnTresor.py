class OnTresor:
    def __init__(self, ui):
        self.ui = ui


    def action(self, personnage, salle, original_x, original_y):
        self.ui.display("Vous êtes dans une salle avec un trésor.")