class OnMur:
    def __init__(self, ui):
        self.ui = ui


    def onMur(self, personnage, original_x, original_y):
        self.ui.display("Il y a un mur, vous ne pouvez pas y aller.")
        personnage.coordX, personnage.coordY = original_x, original_y