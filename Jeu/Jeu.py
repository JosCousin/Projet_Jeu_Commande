from Personnage.Personnage import Personnage
from Donjon.Grille import creationGrille
from Deplacement.Deplacement import Deplacement

class Jeu:
    def __init__(self, choixNom, choixClasse, voirStats, ui):
        self.choixNom = choixNom
        self.choixClasse = choixClasse
        self.voirStats = voirStats
        self.ui = ui

    def start(self):
        self.ui.display("Bienvenue dans le jeu de combat !")
        self.ui.display("Créez votre personnage :")
    
        nom = self.choixNom.choixNom()
        classe = self.choixClasse.choixClasse()
        personnage = Personnage(nom, classe)
    
        self.voirStats.voirStats(personnage)
    
        self.ui.display("Chargement de la carte...")
        donjon = creationGrille()
        self.ui.display("Grilles chargées !")
    
        deplacement = Deplacement(personnage, donjon, self.ui)
        while True:
            nouvelle_grille = deplacement.deplacement()
            if nouvelle_grille is not None:
                donjon = nouvelle_grille
                deplacement = Deplacement(personnage, donjon, self.ui)