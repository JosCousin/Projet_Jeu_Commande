from Donjon.Grille import creationGrille
from Deplacement.SalleEvenement import SalleEvenement

class VerifTypeSalle:
    def __init__(self, ui):
        self.ui = ui
        self.evenement = SalleEvenement(ui)

    def verifTypeSalle(self, personnage, listeSalles, original_x, original_y):
        for salle in listeSalles:
            if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
                if salle.typeSalle == 1:
                    self.evenement.onSalleVide(personnage)
                elif salle.typeSalle == 2:
                    self.evenement.onMonstre(personnage, salle)
                elif salle.typeSalle == 3:
                    self.evenement.onTresor(personnage)
                elif salle.typeSalle == 4:
                    self.evenement.onMur(personnage, original_x, original_y)
                elif salle.typeSalle == 5:
                    newGrille = self.evenement.onPorte(personnage)
                    if newGrille is not None:
                        return newGrille
                break

        return None