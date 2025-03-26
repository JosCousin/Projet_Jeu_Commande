from Donjon.Monstre import Monstre
from Combat.Action import Action

def combat(personnage):
    monstre = Monstre()

    print(f"Vous êtes attaqué par un {monstre.nom} !")
    print(f"Le {monstre.nom} a {monstre.PV} points de vie.")
    print("Actions disponibles :")
    for action in Action:
        print(f"{action.name} - {action.value.__name__}")

    while monstre.PV > 0 and personnage.PV > 0:
        action_input = input("Choisissez une action : ").upper()
        if action_input in Action.__members__:
            action_class = Action[action_input].value
            action = action_class(personnage, monstre)
            action.execute()
            if action_input == "F": 
                print("Vous avez quitté le combat.")
                break
        else:
            print("Action invalide. Veuillez réessayer.")



