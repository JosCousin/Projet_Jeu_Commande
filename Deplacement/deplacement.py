from Deplacement.VerifCoordonnnees import VerifCoordonnees

class Deplacement:
    def __init__(self, personnage, donjon, ui):
        self.personnage = personnage.stats
        self.listeSalles = donjon.listeSalle
        self.ui = ui

    def deplacement(self):
        action = input("Entrez une commande (N/S/E/O/Q) : ").lower()

        original_x, original_y = self.personnage.coordX, self.personnage.coordY

        mouvements = {
            "n": (0,  1),
            "s": (0, -1),
            "e": (1,  0),
            "o": (-1, 0)
        }

        if action == "q":
            print("Vous avez quitté le jeu.")
            exit()
        elif action in mouvements:
            dx, dy = mouvements[action]
            self.personnage.coordX += dx
            self.personnage.coordY += dy
        else:
            print("Commande invalide. Veuillez réessayer.")
            return self.deplacement()

        # Passage de self.ui afin que VerifCoordonnees ait accès à l'interface utilisateur.
        valide, nouvelle_grille = VerifCoordonnees.verifCoordonnees(
            self.personnage, self.listeSalles, original_x, original_y, self.ui
        )
        if not valide:
            self.personnage.coordX, self.personnage.coordY = original_x, original_y
            print(
                f"Le déplacement a été annulé. Vous êtes toujours à "
                f"({self.personnage.coordX}, {self.personnage.coordY})."
            )
            return self.deplacement()
        elif nouvelle_grille is not None:
            print("Changement de grille.")
            return nouvelle_grille
        else:
            return self.deplacement()