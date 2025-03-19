from Deplacement.VerifCoordonnnees import VerifCoordonnees

class Deplacement:
    def __init__(self, personnage, donjon):
        self.personnage = personnage.stats
        self.listeSalles = donjon.listeSalle

    def deplacement(self):
        action = input("Entrez une commande (N/S/E/O/Q) : ").lower()

        original_x, original_y = self.personnage.coordX, self.personnage.coordY

        if action == "n":
            self.personnage.coordY += 1
        elif action == "s":
            self.personnage.coordY -= 1
        elif action == "e":
            self.personnage.coordX += 1
        elif action == "o":
            self.personnage.coordX -= 1
        elif action == "q":
            print("Vous avez quitté le jeu.")
            exit()
        else:
            print("Commande invalide. Veuillez réessayer.")
            self.deplacement() 

        valide, nouvelle_grille = VerifCoordonnees.verifCoordonnees(self.personnage, self.listeSalles, original_x, original_y)
        if not valide:
            self.personnage.coordX, self.personnage.coordY = original_x, original_y
            print(f"Le déplacement a été annulé. Vous êtes toujours à ({self.personnage.coordX}, {self.personnage.coordY}).")
            self.deplacement()
        elif nouvelle_grille is not None:
            return nouvelle_grille
        else:
            self.deplacement()