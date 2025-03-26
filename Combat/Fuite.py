class Fuite:
    def __init__(self, personnage, monstre=None):
        self.personnage = personnage

    def execute(self):
        if self.personnage.PV <= 15:
            print("Vous n'avez pas assez de points de vie pour fuir le combat.")
            print("Vous êtes vaincu par le monstre.")
        else:
            print("Vous avez fui le combat.")
            self.personnage.PV -= 15
            print(f"Vous avez maintenant {self.personnage.PV} points de vie.")
