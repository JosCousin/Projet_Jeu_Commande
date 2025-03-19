class VoirStat:
    def __init__(self, ui):
        self.ui = ui

    def voirStats(self, personnage):
        self.ui.display("Voulez-vous voir les stats de votre personnage ?")
        choix = self.ui.get_input("Oui/Non : ")
        if choix.lower() in ["oui", "o"]:
            self.ui.display("Nom : " + personnage.nom)
            self.ui.display("Voici les stats :")
            self.ui.display("Points de Vie : " + str(personnage.stats.PV))
            self.ui.display("Points de Mana : " + str(personnage.stats.PM))
            self.ui.display("Force : " + str(personnage.stats.force))
            self.ui.display("Intelligence : " + str(personnage.stats.intelligence))
            self.ui.display("Défense Physique : " + str(personnage.stats.defPhysique))
            self.ui.display("Défense Magique : " + str(personnage.stats.defMagique))
            self.ui.display("Agilité : " + str(personnage.stats.agilite))
            self.ui.display("Chance : " + str(personnage.stats.chance))
            self.ui.display("Endurance : " + str(personnage.stats.endurance))
            self.ui.display("Esprit : " + str(personnage.stats.esprit))
            self.ui.display("Position : " + str(personnage.stats.coordX) + ", " + str(personnage.stats.coordY))
            self.ui.display("Très bien, bonne aventure !")
        else:
            self.ui.display("Très bien, bonne aventure !")