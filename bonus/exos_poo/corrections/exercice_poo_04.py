# Exercice : Gestion des Employés

# Objectif :
# - Utiliser l'héritage pour modéliser une hiérarchie d'employés.
#
# Étapes :
# 1. Créer une classe `Employe` avec les attributs `nom` et `salaire_base`.
# 2. Créer deux sous-classes `Developpeur` et `Manager` qui héritent de `Employe`.
#    - `Developpeur` aura un attribut `langage_programmation`.
#    - `Manager` aura un attribut `nombre_personnes_supervisees`.
# 3. Ajouter une méthode `calculer_salaire()` dans `Employe` et la redéfinir dans les sous-classes pour ajouter des bonus spécifiques.

class Employe:
    """
    Classe de base représentant un employé.
    """
    def __init__(self, nom: str, salaire_base: float):
        """
        Initialise un employé avec un nom et un salaire de base.
        """
        self.nom = nom
        self.salaire_base = salaire_base

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire de base (sans bonus spécifique).
        """
        return self.salaire_base

    def afficher_infos(self):
        """
        Affiche les informations générales de l'employé.
        """
        print(f"Employé : {self.nom}, Salaire : {self.calculer_salaire():.2f}€")


class Developpeur(Employe):
    """
    Classe représentant un développeur, héritant de Employe.
    """
    def __init__(self, nom: str, salaire_base: float, langage_programmation: str):
        """
        Initialise un développeur avec son langage de programmation.
        """
        super().__init__(nom, salaire_base)
        self.langage_programmation = langage_programmation

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire avec un bonus de 10%.
        """
        return self.salaire_base * 1.10

    def afficher_infos(self):
        """
        Affiche les informations spécifiques au développeur.
        """
        print(f"Développeur : {self.nom}, Langage : {self.langage_programmation}, Salaire : {self.calculer_salaire():.2f}€")


class Manager(Employe):
    """
    Classe représentant un manager, héritant de Employe.
    """
    def __init__(self, nom: str, salaire_base: float, nombre_personnes_supervisees: int):
        """
        Initialise un manager avec son nombre de subordonnés.
        """
        super().__init__(nom, salaire_base)
        self.nombre_personnes_supervisees = nombre_personnes_supervisees

    def calculer_salaire(self) -> float:
        """
        Retourne le salaire avec un bonus de 5% par employé supervisé.
        """
        return self.salaire_base * (1 + 0.05 * self.nombre_personnes_supervisees)

    def afficher_infos(self):
        """
        Affiche les informations spécifiques au manager.
        """
        print(f"Manager : {self.nom}, Supervise {self.nombre_personnes_supervisees} personnes, Salaire : {self.calculer_salaire():.2f}€")


# Exemple d'utilisation
if __name__ == "__main__":
    dev = Developpeur("Alice", 3000, "Python")
    manager = Manager("Bob", 4000, 5)
    
    dev.afficher_infos()
    manager.afficher_infos()
