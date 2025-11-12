# Exercice : Gestion des Véhicules

# Objectif :
# - Mettre en place l'héritage en créant une hiérarchie de classes représentant des véhicules.
#
# Étapes :
# 1. Créer une classe `Vehicule` avec les attributs : `marque`, `modele`, `annee`.
# 2. Créer deux sous-classes `Voiture` et `Moto` qui héritent de `Vehicule`.
#    - `Voiture` aura un attribut `nombre_portes`.
#    - `Moto` aura un attribut `cylindree`.
# 3. Ajouter une méthode `afficher_infos()` dans `Vehicule` et la redéfinir dans les sous-classes.

class Vehicule:
    """
    Classe de base représentant un véhicule.
    """
    def __init__(self, marque: str, modele: str, annee: int):
        """
        Initialise un véhicule avec une marque, un modèle et une année.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee

    def afficher_infos(self):
        """
        Affiche les informations générales du véhicule.
        """
        print(f"Véhicule : {self.marque} {self.modele}, Année : {self.annee}")


class Voiture(Vehicule):
    """
    Classe représentant une voiture, héritant de Vehicule.
    """
    def __init__(self, marque: str, modele: str, annee: int, nombre_portes: int):
        """
        Initialise une voiture avec son nombre de portes en plus des attributs de Vehicule.
        """
        super().__init__(marque, modele, annee)
        self.nombre_portes = nombre_portes

    def afficher_infos(self):
        """
        Affiche les informations spécifiques à une voiture.
        """
        print(f"Voiture : {self.marque} {self.modele}, Année : {self.annee}, Portes : {self.nombre_portes}")


class Moto(Vehicule):
    """
    Classe représentant une moto, héritant de Vehicule.
    """
    def __init__(self, marque: str, modele: str, annee: int, cylindree: int):
        """
        Initialise une moto avec sa cylindrée en plus des attributs de Vehicule.
        """
        super().__init__(marque, modele, annee)
        self.cylindree = cylindree

    def afficher_infos(self):
        """
        Affiche les informations spécifiques à une moto.
        """
        print(f"Moto : {self.marque} {self.modele}, Année : {self.annee}, Cylindrée : {self.cylindree}cc")


# Exemple d'utilisation
if __name__ == "__main__":
    voiture = Voiture("Toyota", "Corolla", 2020, 5)
    moto = Moto("Yamaha", "R1", 2022, 1000)
    
    voiture.afficher_infos()
    moto.afficher_infos()
