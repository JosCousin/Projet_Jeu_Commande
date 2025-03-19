import random
from .Monstre import Monstre

class Salle:
    def __init__(self, coordX, coordY, typeSalle):
        self.coordX = coordX
        self.coordY = coordY
        self.typeSalle = typeSalle

def verifSalle(salle, personnage):
    if salle.typeSalle == 2:
        print("Vous entrez dans une salle et un monstre vous attaque !")
        monstre = Monstre()
        print(f"Le monstre a {monstre.vie} points de vie.")
        print("Vous pouvez attaquer le monstre en tapant 'A' ou fuir en tapant 'F' mais vous perderez 5 PV.")
        if input().lower() == "a":
            print("Vous attaquez le monstre !")
            monstre.vie -= personnage.force
            print(f"Le monstre a maintenant {monstre.vie} points de vie.")
            if monstre.vie <= 0:
                print("Vous avez vaincu le monstre !")