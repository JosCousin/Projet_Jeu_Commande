class ChoixNom :
    def __init__(self):
        pass

    def choixNom(self):
        nom = input("Entrez le nom de votre personnage (max 10 caractères, min 3 caractères) : ")
        if (len(nom) < 3):
            print("Nom trop court, recommencez.\n")
            self.choixNom()
        elif (len(nom) > 10):
            print("Nom trop long, recommencez.\n")
            self.choixNom()
        return nom