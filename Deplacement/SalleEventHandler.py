from Donjon.Grille import creationGrille
from Combat.CombatEngine import CombatEngine

class SalleEventHandler:
    def __init__(self, ui):
        self.ui = ui

    def onSalleVide(self, personnage):
        self.ui.display("Vous êtes dans une salle vide.")

    def onMonstre(self, personnage, salle):
        self.ui.display("Vous êtes dans une salle avec un monstre.")
        combat_engine = CombatEngine(self.ui)
        combat_engine.start_combat(personnage, salle)

    def onTresor(self, personnage):
        self.ui.display("Vous êtes dans une salle avec un trésor.")

    def onMur(self, personnage, original_x, original_y):
        self.ui.display("Il y a un mur, vous ne pouvez pas y aller.")
        personnage.coordX, personnage.coordY = original_x, original_y

    def onPorte(self, personnage):
        self.ui.display("Vous avez trouvé une porte, continuer ? (Oui/Non).")
        choix = self.ui.get_input("Votre choix : ").lower()
        if choix == "non":
            self.ui.display("Vous avez quitté le jeu.")
            exit()
        elif choix == "oui":
            self.ui.display("Vous changez de grille !")
            personnage.coordX = 0
            personnage.coordY = 0
            return creationGrille()
        return None