from Guerrier import Guerrier
from Mage import Mage
from Voleur import Voleur

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

