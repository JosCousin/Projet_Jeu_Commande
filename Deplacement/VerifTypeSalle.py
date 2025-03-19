from Donjon.Grille import creationGrille
from Deplacement.SalleEventHandler import SalleEventHandler

class VerifTypeSalle:
    def __init__(self, ui):
        self.ui = ui
        self.eventHandler = SalleEventHandler(ui)

    def verifTypeSalle(self, personnage, listeSalles, original_x, original_y):
        for salle in listeSalles:
            if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
                if salle.typeSalle == 1:
                    self.eventHandler.onSalleVide(personnage)
                elif salle.typeSalle == 2:
                    self.eventHandler.onMonstre(personnage, salle)
                elif salle.typeSalle == 3:
                    self.eventHandler.onTresor(personnage)
                elif salle.typeSalle == 4:
                    self.eventHandler.onMur(personnage, original_x, original_y)
                elif salle.typeSalle == 5:
                    newGrille = self.eventHandler.onPorte(personnage)
                    if newGrille is not None:
                        return newGrille
                break

        return None