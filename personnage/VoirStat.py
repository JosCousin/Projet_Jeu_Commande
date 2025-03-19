class VoirStat:
    def __init__(self):
        pass

    @staticmethod
    def voirStats(personnage):
        print("Voulez-vous voir les stats de votre personnage ?")
        choix = input("Oui/Non : ")
        if choix == "Oui" or choix == "oui" or choix == "O" or choix == "o":
            print("Nom :", personnage.nom)
            print("Voici les stats :")
            print("Points de Vie :", personnage.stats.PV)
            print("Points de Mana :", personnage.stats.PM)
            print("Force :", personnage.stats.force)
            print("Intelligence :", personnage.stats.intelligence)
            print("Défense Physique :", personnage.stats.defPhysique)
            print("Défense Magique :", personnage.stats.defMagique)
            print("Agilité :", personnage.stats.agilite)
            print("Chance :", personnage.stats.chance)
            print("Endurance :", personnage.stats.endurance)
            print("Esprit :", personnage.stats.esprit)
            print("Position :", personnage.stats.coordX, ",", personnage.stats.coordY)
            print("Très bien, bonne aventure !")

        else:
            print("Très bien, bonne aventure !")