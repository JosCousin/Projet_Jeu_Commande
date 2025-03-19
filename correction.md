# Violations des principes SOLID

## 1. Single Responsibility Principle (SRP)

### Dans la classe Personnage
- La classe `Personnage` contient trop d'attributs et de responsabilités
- Elle gère à la fois les caractéristiques du personnage et sa position
- Elle ne respecte pas la responsabilité unique

### Dans la fonction voirStats
- Mélange l'affichage et la logique de décision
- Gère à la fois l'interface utilisateur et la logique métier

### Dans main.py
- Contient trop de responsabilités différentes
- Gère la création, l'affichage et la logique du jeu
- Ne respecte pas la séparation des préoccupations

## 2. Open/Closed Principle (OCP)

### Dans la fonction choixClasse
- N'est pas extensible pour ajouter de nouvelles classes
- Nécessite de modifier le code existant pour ajouter de nouvelles classes
- Utilise des conditions if/elif au lieu d'une structure extensible

## 3. Liskov Substitution Principle (LSP)

### Dans la hiérarchie des classes
- Les classes dérivées (Guerrier, Mage, Voleur) ne semblent pas correctement substituables
- La classe de base `Personnage` force l'implémentation de tous les attributs
- Pas de garantie que les classes dérivées respectent le contrat de la classe de base

## 4. Interface Segregation Principle (ISP)

### Dans la classe Personnage
- Force toutes les classes dérivées à implémenter tous les attributs
- Crée une interface trop large et non spécifique
- Les classes dérivées sont obligées d'implémenter des attributs qu'elles n'utilisent pas

## 5. Dependency Inversion Principle (DIP)

### Dans l'architecture globale
- Les dépendances sont directement instanciées dans le code
- Pas d'utilisation d'interfaces ou d'abstractions
- Fort couplage entre les composants
- Absence d'injection de dépendances 
