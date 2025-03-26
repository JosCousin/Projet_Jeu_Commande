from Deplacement.Mouvement.IMouvement import IMouvement

class NordMouvement(IMouvement):
    def move(self, personnage):
        personnage.coordX += 0
        personnage.coordY += 1