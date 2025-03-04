def verifCoordonnees(personnage, listeSalles):
    if any(salle.coordX == personnage.coordX and salle.coordY == personnage.coordY for salle in listeSalles):
        print(f"Vous êtes actuellement dans une Salle en position ({personnage.coordX}, {personnage.coordY}).")
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
        return

    if not verifCoordonnees(personnage, listeSalles):
        personnage.coordX, personnage.coordY = original_x, original_y
        print(f"Le déplacement a été annulé. Vous êtes toujours à ({personnage.coordX}, {personnage.coordY}).")
        deplacement(personnage, listeSalles)
    else:
        deplacement(personnage, listeSalles)
