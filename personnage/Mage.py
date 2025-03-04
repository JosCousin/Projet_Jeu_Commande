from .personnage import Personnage

class Mage(Personnage):
    def __init__(self, nom):
        PV = 90
        PM = 150
        force = 4
        intelligence = 15
        defPhysique = 5
        defMagique = 12
        agilite = 7
        chance = 6
        endurance = 5
        esprit = 10
        super().__init__(nom, PV, PM, force, intelligence, defPhysique, defMagique, agilite, chance, endurance, esprit, "Mage")