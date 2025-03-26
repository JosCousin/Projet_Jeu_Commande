from enum import Enum
from Personnage.Stats import Stats

class Classe(Enum):
    Guerrier = 1 , "Guerrier", Stats(PV = 150, PM = 50, force = 15, intelligence = 5, defPhysique = 12, defMagique = 6, agilite = 8, chance = 5, endurance = 10, esprit = 4, coordX = 0, coordY = 0,)
    
    Mage = 2 , "Mage", Stats(PV = 90, PM = 150, force = 4, intelligence = 15, defPhysique = 5, defMagique = 12, agilite = 7, chance = 6, endurance = 5, esprit = 10, coordX = 0, coordY = 0)

    Voleur = 3 , "Voleur", Stats(PV = 110, PM = 70, force = 10, intelligence = 7, defPhysique = 8, defMagique = 7, agilite = 15, chance = 12, endurance = 7, esprit = 6, coordX = 0, coordY = 0)