import random
from .grille import creationGrille

class Donjon():
    def __init__(self, nbGrilles):
        self.nbGrilles = nbGrilles
        self.grilles = []

def creationDonjon():
    nbGrilles = 9

    donjon = Donjon(nbGrilles)

    for x in range(-1, 1):
        for y in range(-1, 1):
            donjon.grilles.append(creationGrille(x, y))

    return donjon