class Attaque:
    def __init__(self, personnage, monstre):
        self.personnage = personnage
        self.monstre = monstre

    def execute(self):
        print("Vous attaquez le monstre !")
        self.monstre.PV -= self.personnage.force
        print(f"Le {self.monstre.nom} a maintenant {self.monstre.PV} points de vie.")
        if self.monstre.PV <= 0:
            print("Vous avez vaincu le monstre !")
        else:
            print("Le monstre vous attaque !")
            self.personnage.PV -= self.monstre.force
            print(f"Vous avez maintenant {self.personnage.PV} points de vie.")
            if self.personnage.PV <= 0:
                print("Vous avez été vaincu par le monstre.")