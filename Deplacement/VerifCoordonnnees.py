from .VerifTypeSalle import *

class VerifCoordonnees:
    def __init__(self):
        pass

    @staticmethod
    def verifCoordonnees(personnage, listeSalles, original_x, original_y):
        nouvelle_grille = None
        if any(salle.coordX == personnage.coordX and salle.coordY == personnage.coordY for salle in listeSalles):
            nouvelle_grille = VerifTypeSalle.verifTypeSalle(personnage, listeSalles, original_x, original_y)
            print(f"Vous êtes actuellement dans une Salle en position ({personnage.coordX}, {personnage.coordY}).")
            return True, nouvelle_grille
        else:
            print("Il n'y a pas de salle en position.")
            return False, None