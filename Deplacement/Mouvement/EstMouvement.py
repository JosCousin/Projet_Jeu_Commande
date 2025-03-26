from Deplacement.Mouvement.IMouvement import IMouvement

class EstMouvement(IMouvement):
    def move(self, personnage):
        personnage.coordX += 1
        personnage.coordY += 0