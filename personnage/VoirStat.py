class VoirStat:
    def __init__(self, ui, decision):
        self.ui = ui
        self.decisionHelper = decision

    def voirStats(self, personnage):
        if self.decisionHelper.demandeVoirStats():
            self.ui.display("Nom : " + personnage.nom)
            self.ui.display("Voici les stats :")
            self.ui.display("Points de Vie : " + str(personnage._stats.PV))
            self.ui.display("Points de Mana : " + str(personnage._stats.PM))
            self.ui.display("Force : " + str(personnage._stats.force))
            self.ui.display("Intelligence : " + str(personnage._stats.intelligence))
            self.ui.display("Défense Physique : " + str(personnage._stats.defPhysique))
            self.ui.display("Défense Magique : " + str(personnage._stats.defMagique))
            self.ui.display("Agilité : " + str(personnage._stats.agilite))
            self.ui.display("Chance : " + str(personnage._stats.chance))
            self.ui.display("Endurance : " + str(personnage._stats.endurance))
            self.ui.display("Esprit : " + str(personnage._stats.esprit))
            self.ui.display("Position : " + str(personnage._stats.coordX) + ", " + str(personnage._stats.coordY))
            self.ui.display("Très bien, bonne aventure !")
        else:
            self.ui.display("Très bien, bonne aventure !")