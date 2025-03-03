import random

class Salle():
    def __init__(self, coordX, coordY, typeSalle):
        self.coordX = coordX
        self.coordY = coordY
        self.typeSalle = typeSalle

def creationSalle():
    nbSalle = random.randint(1, 9)
    listeSalle = []

    listeSalle.append(Salle(0, 0, 1))

    if nbSalle > 1:
        nbSalle -= 1
        for i in range(nbSalle):
            while True:
                cordX = random.randint(-1, 1)
                cordY = random.randint(-1, 1)
                if not any(salle.coordX == cordX and salle.coordY == cordY for salle in listeSalle):
                    break
            typeSalle = random.randint(1, 3)
            listeSalle.append(Salle(cordX, cordY, typeSalle))
    return listeSalle