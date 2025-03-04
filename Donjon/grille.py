import random
from .salle import Salle

class Grille:
    def __init__(self, grilleX, grilleY):
        self.grilleX = grilleX
        self.grilleY = grilleY
        self.listeSalle = []
        self.listePorte = []
        

def creationGrille(grilleX, grilleY):
    grille = Grille(grilleX, grilleY)
    nbSalle = 9

    for x in range(-1, 2):
        for y in range(-1, 2):
            type = random.randint(1, 3)
            grille.listeSalle.append(Salle(x, y, type)) 
    return grille