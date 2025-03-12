import random
from .salle import Salle

class Grille:
    def __init__(self):
        self.listeSalle = []

def creationGrille():
    grille = Grille()
    

    for x in range(-2, 3):
        for y in range(-2, 3):
            type = random.randint(1, 4)
            grille.listeSalle.append(Salle(x, y, type)) 

    random.choice(grille.listeSalle).typeSalle = 5
    grille.listeSalle[4].typeSalle = 1
    return grille