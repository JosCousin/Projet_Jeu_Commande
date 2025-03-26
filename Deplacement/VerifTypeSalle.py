from Deplacement.ActionTypeSalle import ActionTypeSalle
from Donjon.TypeSalle import TypeSalle

class VerifTypeSalle:
    def __init__(self, ui):
        self.ui = ui

    def verifTypeSalle(self, personnage, listeSalles, original_x, original_y):
        for salle in listeSalles:
            if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
                salle_type = TypeSalle(salle.typeSalle)
                action_class = ActionTypeSalle[salle_type.name].value
                action = action_class(self.ui)
                newGrille = action.action(personnage, salle, original_x, original_y)
                if newGrille is not None:
                    return newGrille
                

        return None