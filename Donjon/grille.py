import random
from .salle import Salle

class Grille:
    def __init__(self, nbSalles):
        self.nbSalles = nbSalles
        self.salles = []
        

def creationGrille():
    nbSalle = random.randint(1, 9)
    listeSalle = []

    listeSalle.append(Salle(0, 0, 1))

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while len(listeSalle) < nbSalle:
        salleExistante = random.choice(listeSalle)

        random.shuffle(directions)
        
        for dx, dy in directions:
            newX = salleExistante.coordX + dx
            newY = salleExistante.coordY + dy

            if -1 <= newX <= 1 and -1 <= newY <= 1:
                if not any(salle.coordX == newX and salle.coordY == newY for salle in listeSalle):
                    typeSalle = random.randint(1, 3)
                    listeSalle.append(Salle(newX, newY, typeSalle))
                    break 

    return listeSalle