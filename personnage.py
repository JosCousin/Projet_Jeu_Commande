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

def choixNom():
    nom = input("Entrez le nom de votre personnage (max 10 caractères, min 3 caractères) : ")
    if (len(nom) < 3):
        print("Nom trop court, recommencez.\n")
        choixNom()
    elif (len(nom) > 10):
        print("Nom trop long, recommencez.\n")
        choixNom()
    return nom
