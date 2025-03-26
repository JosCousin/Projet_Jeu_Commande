import random
from Donjon.Salle import Salle

class Grille:
    def __init__(self):
        self.listeSalle = []

def creationGrille():
    grille = Grille()
    
    for x in range(-2, 3):
        for y in range(-2, 3):
            type_salle = random.randint(1, 4)
            grille.listeSalle.append(Salle(x, y, type_salle)) 

    for salle in grille.listeSalle:
        if salle.coordX == 0 and salle.coordY == 0:
            salle.typeSalle = 1
            break

    salles_autre_centre = [salle for salle in grille.listeSalle if not (salle.coordX == 0 and salle.coordY == 0)]
    random.choice(salles_autre_centre).typeSalle = 5

    return grille