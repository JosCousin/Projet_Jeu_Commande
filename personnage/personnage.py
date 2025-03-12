class Personnage:
    def __init__(self, nom, PV, PM, force, intelligence, defPhysique, defMagique, agilite, chance, endurance, esprit, classe):
        self.nom = nom
        self.PV = PV
        self.PM = PM
        self.force = force
        self.intelligence = intelligence
        self.defPhysique = defPhysique
        self.defMagique = defMagique
        self.agilite = agilite
        self.chance = chance
        self.endurance = endurance
        self.esprit = esprit
        self.classe = classe
        self.coordX = 0
        self.coordY = 0
