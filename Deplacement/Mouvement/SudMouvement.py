from Deplacement.Mouvement.IMouvement import IMouvement

class SudMouvement(IMouvement):
    def move(self, personnage):
        personnage.coordX += 0
        personnage.coordY += -1