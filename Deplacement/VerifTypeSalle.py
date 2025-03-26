from Deplacement.SalleEvenement.OnMonstre import OnMonstre
from Deplacement.SalleEvenement.OnMur import OnMur
from Deplacement.SalleEvenement.OnPorte import OnPorte
from Deplacement.SalleEvenement.OnSalleVide import OnSalleVide
from Deplacement.SalleEvenement.OnTresor import OnTresor

class VerifTypeSalle:
    def __init__(self, ui):
        self.ui = ui

    def verifTypeSalle(self, personnage, listeSalles, original_x, original_y):
        for salle in listeSalles:
            if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
                if salle.typeSalle == 1:
                    OnSalleVide(self.ui).onSalleVide()
                elif salle.typeSalle == 2:
                    OnMonstre(self.ui).onMonstre(personnage, salle)
                elif salle.typeSalle == 3:
                    OnTresor(self.ui).onTresor()
                elif salle.typeSalle == 4:
                    OnMur(self.ui).onMur(personnage, original_x, original_y)
                elif salle.typeSalle == 5:
                    newGrille = OnPorte(self.ui).onPorte(personnage)
                    if newGrille is not None:
                        return newGrille
                break

        return None