from Prompt.ConsoleUI import ConsoleUI
from Personnage.ChoixNom import ChoixNom
from Personnage.ChoixClasse import ChoixClasse
from Personnage.VoirStat import VoirStat
from Personnage.CreationPersonnage import CreationPersonnage
from Prompt.Decision import Decision
from Donjon.Grille import creationGrille
from Deplacement.Deplacement import Deplacement

class Jeu:
    def __init__(self):
        self.ui = ConsoleUI()
        self.choixNom = ChoixNom(self.ui)
        self.choixClasse = ChoixClasse(self.ui)
        self.decisionVoirStat = Decision(self.ui)
        self.voirStats = VoirStat(self.ui, self.decisionVoirStat)
        self.creationPersonnage = CreationPersonnage(self.choixNom, self.choixClasse, self.ui)

    def start(self):
        self.afficher_bienvenue()
        personnage = self.creer_personnage()
        self.afficher_stats_personnage(personnage)
        donjon = self.charger_donjon()
        self.gestion_deplacement(personnage, donjon)

    def afficher_bienvenue(self):
        self.ui.display("Bienvenue dans le jeu de combat !")

    def creer_personnage(self):
        return self.creationPersonnage.creer_personnage()

    def afficher_stats_personnage(self, personnage):
        self.voirStats.voirStats(personnage)

    def charger_donjon(self):
        self.ui.display("Chargement de la carte...")
        donjon = creationGrille()
        self.ui.display("Grilles chargées !")
        return donjon

    def gestion_deplacement(self, personnage, donjon):
        deplacement = Deplacement(personnage, donjon, self.ui)
        while True:
            nouvelle_grille = deplacement.deplacement()
            if nouvelle_grille is not None:
                donjon = nouvelle_grille
                deplacement = Deplacement(personnage, donjon, self.ui)