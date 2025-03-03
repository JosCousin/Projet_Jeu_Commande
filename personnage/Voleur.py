from personnage import Personnage

class Voleur(Personnage):
    def __init__(self, nom):
        PV = 110
        PM = 70
        force = 10
        intelligence = 7
        defPhysique = 8
        defMagique = 7
        agilite = 15
        chance = 12
        endurance = 7
        esprit = 6
        super().__init__(nom, PV, PM, force, intelligence, defPhysique, defMagique, agilite, chance, endurance, esprit, "voleur")