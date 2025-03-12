class VoirStat:
    def __init__(self):
        pass

    @staticmethod
    def voirStats(personnage):
        print("Voulez-vous voir les stats de votre personnage ?")
        choix = input("Oui/Non : ")
        if choix == "Oui" or choix == "oui" or choix == "O" or choix == "o":
            print("Très bien, bonne aventure !")
            print("Nom :", personnage.nom, "Classe :", personnage.classe)
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
        else:
            print("Très bien, bonne aventure !")