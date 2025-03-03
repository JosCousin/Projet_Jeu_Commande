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
        super().__init__(nom, PV, PM, force, intelligence, defPhysique, defMagique, agilite, chance, endurance, esprit, "mage")

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

def choixClasse():
    print("Choisissez votre classe :")
    print("1. Guerrier")
    print("2. Mage")
    print("3. Voleur")
    choix = input("Entrez le numéro de la classe choisie : ")
    if choix == "1":
        return Guerrier
    elif choix == "2":
        return Mage
    elif choix == "3":
        return Voleur
    else:
        print("Classe invalide, recommencez.")
        choixClasse()

def voirStats(personnage):
    print("Votre personnage est un", personnage.classe, "nommé", personnage.nom)
    print("Voici les stats :")
    print("Points de Vie :", personnage.PV)
    print("Points de Mana :", personnage.PM)
    print("Force :", personnage.force)
    print("Intelligence :", personnage.intelligence)
    print("Défense Physique :", personnage.defPhysique)
    print("Défense Magique :", personnage.defMagique)
    print("Agilité :", personnage.agilite)
    print("Chance :", personnage.chance)
    print("Endurance :", personnage.endurance)
    print("Esprit :", personnage.esprit)
    print("Position :", personnage.coordX, ",", personnage.coordY)
