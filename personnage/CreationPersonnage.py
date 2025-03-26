from Personnage.Personnage import Personnage

class CreationPersonnage:
    def __init__(self, choixNom, choixClasse, ui):
        self.choixNom = choixNom
        self.choixClasse = choixClasse
        self.ui = ui

    def creer_personnage(self):
        self.ui.display("Créez votre personnage :")
        nom = self.choixNom.choixNom()
        
        classe = self.choixClasse.choixClasse()
        personnage = Personnage(nom, classe)
        self.ui.display(f"Personnage créé : {nom}, classe : {classe.PV}")
        return personnage