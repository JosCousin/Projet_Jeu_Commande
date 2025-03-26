from Deplacement.Mouvement.NordMouvement import NordMouvement
from Deplacement.Mouvement.SudMouvement import SudMouvement
from Deplacement.Mouvement.EstMouvement import EstMouvement
from Deplacement.Mouvement.OuestMouvement import OuestMouvement
from Deplacement.ValidationMouvement import ValidationMouvement

class Deplacement:
    def __init__(self, personnage, donjon, ui):
        self.personnage = personnage.stats
        self.listeSalles = donjon.listeSalle
        self.ui = ui
        self.validator = ValidationMouvement(ui)
        self.mouvements = {
            "n": NordMouvement(),
            "s": SudMouvement(),
            "e": EstMouvement(),
            "o": OuestMouvement()
        }

    def deplacement(self):
        action = self.ui.get_input("Entrez une commande (N/S/E/O/Q) : ").lower()

        original_x, original_y = self.personnage.coordX, self.personnage.coordY

        if action == "q":
            self.ui.display("Vous avez quitté le jeu.")
            exit()
        elif action in self.mouvements:
            self.mouvements[action].move(self.personnage)
        else:
            self.ui.display("Commande invalide. Veuillez réessayer.")
            return self.deplacement()

        valide, nouvelle_grille = self.validator.validate(
            self.personnage, self.listeSalles, original_x, original_y
        )
        if nouvelle_grille is not None:
            self.ui.display("Changement de grille.")
            return nouvelle_grille
        elif not valide:
            return self.deplacement()