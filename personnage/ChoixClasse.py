from Personnage.Classes import Classe

class ChoixClasse:
    def __init__(self, ui):
        self.ui = ui
        self.options = {
            1: Classe.Guerrier,
            2: Classe.Mage,
            3: Classe.Voleur
        }

    def choixClasse(self):
        while True:
            self.ui.display("Choisissez votre classe :")
            for num, classe in self.options.items():
                self.ui.display(f"{num}. {classe.name}")
            try:
                choix = int(self.ui.get_input("Entrez le numéro de la classe choisie : "))
                if choix in self.options:
                    return self.options[choix].value[1]
            except ValueError:
                pass
            self.ui.display("Choix invalide. Veuillez réessayer.")