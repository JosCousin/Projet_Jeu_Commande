from Deplacement.ValidationMouvement import ValidationMouvement
from Deplacement.Direction import Direction

class Deplacement:
    def __init__(self, personnage, donjon, ui):
        self.personnage = personnage.stats
        self.listeSalles = donjon.listeSalle
        self.ui = ui
        self.validator = ValidationMouvement(ui)

    def deplacement(self):
        action = self.get_user_action()

        if action == "q":
            self.ui.display("Vous avez quitté le jeu.")
            exit()

        mouvements = self.get_mouvements()
        if action in mouvements:
            self.effectuer_deplacement(action, mouvements)
        else:
            self.ui.display("Commande invalide. Veuillez réessayer.")
            return self.deplacement()

    def get_user_action(self):
        return self.ui.get_input("Entrez une commande (N/S/E/O/Q) : ").lower()

    def get_mouvements(self):
        return {direction.name.lower(): direction.value for direction in Direction}

    def effectuer_deplacement(self, action, mouvements):
        original_x, original_y = self.personnage.coordX, self.personnage.coordY
        mouvements[action].move(self.personnage)

        valide, nouvelle_grille = self.validator.validate(
            self.personnage, self.listeSalles, original_x, original_y
        )
        if nouvelle_grille is not None:
            self.ui.display("Changement de grille.")
            return nouvelle_grille
        elif not valide:
            return self.deplacement()