import random
from Donjon.Salle import Salle
from Donjon.TypeSalle import TypeSalle

class Grille:
    def __init__(self):
        self.listeSalle = []

def creationGrille():
    grille = Grille()

    types_salles_disponibles = [t for t in TypeSalle if t != TypeSalle.SALLE_PORTE]

    for x in range(-2, 3):
        for y in range(-2, 3):
            type_salle = random.choice(types_salles_disponibles)
            grille.listeSalle.append(Salle(x, y, type_salle.value))

    for salle in grille.listeSalle:
        if salle.coordX == 0 and salle.coordY == 0:
            salle.typeSalle = TypeSalle.SALLE_VIDE.value
            break

    salles_autre_centre = [salle for salle in grille.listeSalle if not (salle.coordX == 0 and salle.coordY == 0)]
    random.choice(salles_autre_centre).typeSalle = TypeSalle.SALLE_PORTE.value

    return grille