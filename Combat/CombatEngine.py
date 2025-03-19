from Combat.Combat import combat

class CombatEngine:
    def __init__(self, ui):
        self.ui = ui

    def start_combat(self, personnage, salle):
        self.ui.display("Début du combat contre un monstre !")
        combat(personnage)
        salle.typeSalle = 1
        self.ui.display("Combat terminé. Le monstre est vaincu.")