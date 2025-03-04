def verifTypeSalle(personnage, listeSalles):
    from Donjon.combat import combat
    for salle in listeSalles:
        if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
            if salle.typeSalle == 1:
                print("Vous êtes dans une salle vide.")
            elif salle.typeSalle == 2:
                print("Vous êtes dans une salle avec un monstre.")
                combat(personnage)
            elif salle.typeSalle == 3:
                print("Vous êtes dans une salle avec un trésor.")
            break



def verifCoordonnees(personnage, listeSalles):
    if any(salle.coordX == personnage.coordX and salle.coordY == personnage.coordY for salle in listeSalles):
        print(f"Vous êtes actuellement dans une Salle en position ({personnage.coordX}, {personnage.coordY}).")
        verifTypeSalle(personnage, listeSalles)
        return True
    else:
        print("Il n'y a pas de salle en position.")
        return False

def deplacement(personnage, listeSalles):
    action = input("Entrez une commande (N/S/E/O/Q) : ").lower()

    original_x, original_y = personnage.coordX, personnage.coordY

    if action == "n":
        personnage.coordY += 1
    elif action == "s":
        personnage.coordY -= 1
    elif action == "e":
        personnage.coordX += 1
    elif action == "o":
        personnage.coordX -= 1
    elif action == "q":
        print("Vous avez quitté le jeu.")
        return
    else:
        print("Commande invalide. Veuillez réessayer.")
        deplacement(personnage, listeSalles)

    if not verifCoordonnees(personnage, listeSalles):
        personnage.coordX, personnage.coordY = original_x, original_y
        print(f"Le déplacement a été annulé. Vous êtes toujours à ({personnage.coordX}, {personnage.coordY}).")
        deplacement(personnage, listeSalles)
    else:
        deplacement(personnage, listeSalles)
