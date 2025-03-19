from Deplacement.VerifTypeSalle import VerifTypeSalle

class VerifCoordonnees:
    @staticmethod
    def verifCoordonnees(personnage, listeSalles, original_x, original_y, ui):
        verif = VerifTypeSalle(ui)
        if any(salle.coordX == personnage.coordX and salle.coordY == personnage.coordY for salle in listeSalles):
            nouvelle_grille = verif.verifTypeSalle(personnage, listeSalles, original_x, original_y)
            ui.display(f"Vous êtes actuellement dans une Salle en position ({personnage.coordX}, {personnage.coordY}).")
            return True, nouvelle_grille
        else:
            ui.display("Il n'y a pas de salle en position.")
            return False, None