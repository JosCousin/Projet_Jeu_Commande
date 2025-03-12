from Donjon.grille import creationGrille

class VerifTypeSalle:
    def __init__(self):
        pass

    @staticmethod
    def verifTypeSalle(personnage, listeSalles, original_x, original_y):
        from Donjon.combat import combat

        for salle in listeSalles:
            if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
                if salle.typeSalle == 1:
                    print("Vous êtes dans une salle vide.")
                elif salle.typeSalle == 2:
                    print("Vous êtes dans une salle avec un monstre.")
                    combat(personnage)
                    salle.typeSalle = 1
                elif salle.typeSalle == 3:
                    print("Vous êtes dans une salle avec un trésor.")
                elif salle.typeSalle == 4:
                    print("Il y a un mur, vous ne pouvez pas y aller.")
                    personnage.coordX, personnage.coordY = original_x, original_y
                elif salle.typeSalle == 5:
                    print("Vous avez trouvé une porte, continuer ? (Oui/Non).")
                    choix = input().lower()
                    if choix == "non":
                        print("Vous avez quitté le jeu.")
                    elif choix == "oui":
                        print("Vous changez de grille !")
                        personnage.coordX = 0
                        personnage.coordY = 0
                        return creationGrille()
                break
        
        return None
