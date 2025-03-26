from Deplacement.VerifCoordonnnees import VerifCoordonnees

class ValidationMouvement:
    def __init__(self, ui):
        self.ui = ui

    def validate(self, personnage, listeSalles, original_x, original_y):
        valide, nouvelle_grille = VerifCoordonnees.verifCoordonnees(
            personnage, listeSalles, original_x, original_y, self.ui
        )
        if not valide:
            personnage.coordX, personnage.coordY = original_x, original_y
            self.ui.display(
                f"Le déplacement a été annulé. Vous êtes toujours à "
                f"({personnage.coordX}, {personnage.coordY})."
            )
        return valide, nouvelle_grille