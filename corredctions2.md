# Infractions aux Principes SOLID

## Single Responsibility Principle (SRP)

1. **Classe Jeu** (`Jeu/jeu.py`)
   ```python
   class Jeu:
       def __init__(self, choixNom, choixClasse, voirStats, ui):
           self.choixNom = choixNom
           self.choixClasse = choixClasse
           self.voirStats = voirStats
           self.ui = ui

       def start(self):  # Trop de responsabilités dans une seule méthode
           self.ui.display("Bienvenue dans le jeu de combat !")
           self.ui.display("Créez votre personnage :")
           nom = self.choixNom.choixNom()
           classe = self.choixClasse.choixClasse()
           personnage = Personnage(nom, classe)
           self.voirStats.voirStats(personnage)
           self.ui.display("Chargement de la carte...")
           donjon = creationGrille()
           self.ui.display("Grilles chargées !")
           deplacement = Deplacement(personnage, donjon, self.ui)
           # ... gestion du jeu
   ```

2. **Classe Deplacement** (`Deplacement/Deplacement.py`)
   ```python
   class Deplacement:
       def __init__(self, personnage, donjon, ui):
           self.personnage = personnage.stats
           self.listeSalles = donjon.listeSalle
           self.ui = ui

       def deplacement(self):  # Responsabilité d'interface utilisateur et de logique
           action = input("Entrez une commande (N/S/E/O/Q) : ").lower()
           # ... logique de déplacement
   ```

## Open/Closed Principle (OCP)

1. **Gestion des Mouvements** (`Deplacement/Deplacement.py`)
   ```python
   def deplacement(self):
       mouvements = {
           "n": (0,  1),
           "s": (0, -1),
           "e": (1,  0),
           "o": (-1, 0)
       }
   # Modification nécessaire pour ajouter de nouveaux types de mouvements
   ```

2. **Gestion du Combat** (`Combat/Combat.py`)
   ```python
   def combat(personnage):
       if input().lower() == "a":
           print("Vous attaquez le monstre !")
           monstre.PV -= personnage.force
           # ...
       else:
           if personnage.PV <= 15:
               print("Vous n'avez pas assez de points de vie pour fuir le combat.")
   # Modification nécessaire pour ajouter de nouvelles actions de combat
   ```

3. **Gestion des Salles** (`Donjon/Grille.py`)
   ```python
   def creationGrille():
       # ...
       type_salle = random.randint(1, 4)
       # ...
       if salle.coordX == 0 and salle.coordY == 0:
           salle.typeSalle = 1
       # ...
       random.choice(salles_autre_centre).typeSalle = 5
   # Modification nécessaire pour ajouter de nouveaux types de salles
   ```

4. **Vérification des Types de Salles** (`Deplacement/VerifTypeSalle.py`)
   ```python
   def verifTypeSalle(self, personnage, listeSalles, original_x, original_y):
       for salle in listeSalles:
           if salle.coordX == personnage.coordX and salle.coordY == personnage.coordY:
               if salle.typeSalle == 1:
                   OnSalleVide(self.ui).onSalleVide()
               elif salle.typeSalle == 2:
                   OnMonstre(self.ui).onMonstre(personnage, salle)
               elif salle.typeSalle == 3:
                   OnTresor(self.ui).onTresor()
               elif salle.typeSalle == 4:
                   OnMur(self.ui).onMur(personnage, original_x, original_y)
               elif salle.typeSalle == 5:
                   newGrille = OnPorte(self.ui).onPorte(personnage)
   # Modification nécessaire pour ajouter de nouveaux types de salles
   ```

5. **Gestion des Classes** (`personnage/classes.py`)
   ```python
   class Classe(Enum):
       Guerrier = 1, Stats(...)
       Mage = 2, Stats(...)
       Voleur = 3, Stats(...)
   # Modification nécessaire pour ajouter de nouvelles classes
   ```

6. **Choix des Classes** (`personnage/ChoixClasse.py`)
   ```python
   def __init__(self, ui):
       self.ui = ui
       self.options = {
           1: Classe.Guerrier,
           2: Classe.Mage,
           3: Classe.Voleur
       }
   # Modification nécessaire pour ajouter de nouvelles classes
   ```

7. **Gestion des Armes** (`Donjon/Objet/Epee.py`)
   ```python
   class Epee():
       def __init__(self, nom):
           self.nom = nom
           self.degats = 20
   # Modification nécessaire pour ajouter de nouveaux types d'armes
   ```

## Liskov Substitution Principle (LSP)

1. **Gestion des Personnages** (`Personnage/Personnage.py`)
   ```python
   class Personnage:
       def __init__(self, nom, stats):
           self.nom = nom
           self.stats = stats
   # Les sous-classes ne peuvent pas modifier le comportement des stats
   ```

2. **Gestion des Déplacements** (`Deplacement/Deplacement.py`)
   ```python
   def deplacement(self):
       if action == "q":
           print("Vous avez quitté le jeu.")
           exit()
       elif action in mouvements:
           dx, dy = mouvements[action]
           self.personnage.coordX += dx
           self.personnage.coordY += dy
   # Les sous-classes ne peuvent pas modifier le comportement du déplacement
   ```

## Interface Segregation Principle (ISP)

1. **Classe Jeu** (`Jeu/jeu.py`)
   ```python
   def __init__(self, choixNom, choixClasse, voirStats, ui):
       self.choixNom = choixNom
       self.choixClasse = choixClasse
       self.voirStats = voirStats
       self.ui = ui
   # Trop de dépendances forcées
   ```

2. **Classe Deplacement** (`Deplacement/Deplacement.py`)
   ```python
   def __init__(self, personnage, donjon, ui):
       self.personnage = personnage.stats
       self.listeSalles = donjon.listeSalle
       self.ui = ui
   # Trop de dépendances forcées
   ```

## Dependency Inversion Principle (DIP)

1. **Dépendances Concrètes** (`Jeu/jeu.py`)
   ```python
   def start(self):
       nom = self.choixNom.choixNom()
       classe = self.choixClasse.choixClasse()
       personnage = Personnage(nom, classe)
       donjon = creationGrille()
   # Dépendances directes vers les implémentations
   ```

2. **Injection de Dépendances** (`Deplacement/Deplacement.py`)
   ```python
   def __init__(self, personnage, donjon, ui):
       self.personnage = personnage.stats
       self.listeSalles = donjon.listeSalle
       self.ui = ui
   # Dépendances directes vers les implémentations
   ``` 
