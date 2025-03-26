from Combat.CombatEngine import CombatEngine

class OnMonstre:
    def __init__(self, ui):
        self.ui = ui

    def action(self, personnage, salle, original_x, original_y):
        self.ui.display("Vous êtes dans une salle avec un monstre.")
        combat_engine = CombatEngine(self.ui)
        combat_engine.start_combat(personnage, salle)