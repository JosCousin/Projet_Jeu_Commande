from Donjon.Grille import creationGrille

class OnPorte:
    def __init__(self, ui):
        self.ui = ui

    def onPorte(self, personnage):
            self.ui.display("Vous avez trouvé une porte, continuer ? (Oui/Non).")
            choix = self.ui.get_input("Votre choix : ").lower()
            if choix == "non":
                self.ui.display("Vous avez quitté le jeu.")
                exit()
            elif choix == "oui":
                self.ui.display("Vous changez de grille !")
                personnage.coordX = 0
                personnage.coordY = 0
                return creationGrille()
            return None