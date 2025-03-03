from personnage import Personnage
class Guerrier(Personnage):
    def __init__(self, nom):
        PV = 150
        PM = 50
        force = 15
        intelligence = 5
        defPhysique = 12
        defMagique = 6
        agilite = 8
        chance = 5
        endurance = 10
        esprit = 4
        super().__init__(nom, PV, PM, force, intelligence, defPhysique, defMagique, agilite, chance, endurance, esprit, "guerrier")