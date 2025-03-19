from Personnage.IChoixNom import IChoixNom

class ChoixNom(IChoixNom):
    def __init__(self, ui):
        self.ui = ui

    def choixNom(self):
        nom = self.ui.get_input("Entrez le nom de votre personnage (max 10 caractères, min 3 caractères) : ")
        if len(nom) < 3:
            self.ui.display("Nom trop court, recommencez.\n")
            return self.choixNom()
        elif len(nom) > 10:
            self.ui.display("Nom trop long, recommencez.\n")
            return self.choixNom()
        return nom