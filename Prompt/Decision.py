class Decision:
    def __init__(self, ui):
        self.ui = ui

    def demandeVoirStats(self):
        choix = self.ui.get_input("Voulez-vous voir les stats de votre personnage ? (Oui/Non) : ")
        return choix.lower() in ["oui", "o"]