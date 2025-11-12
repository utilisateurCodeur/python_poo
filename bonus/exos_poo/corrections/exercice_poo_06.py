# Exercice : Système de Personnages pour un Jeu Vidéo

# Objectif :
# - Créer une hiérarchie de personnages dans un jeu vidéo en utilisant l'héritage.
#
# Étapes :
# 1. Créer une classe `Personnage` avec les attributs `nom` et `points_vie`.
# 2. Créer trois sous-classes `Guerrier`, `Mage`, et `Archer` héritant de `Personnage`.
#    - Chaque classe ajoute une compétence spéciale.
# 3. Ajouter une méthode `attaquer()` dans `Personnage` et la redéfinir dans les sous-classes avec des attaques spécifiques.

class Personnage:
    """
    Classe de base représentant un personnage dans un jeu vidéo.
    """
    def __init__(self, nom: str, points_vie: int):
        """
        Initialise un personnage avec un nom et des points de vie.
        """
        self.nom = nom
        self.points_vie = points_vie
    
    def attaquer(self):
        """
        Méthode générique d'attaque, à redéfinir dans les sous-classes.
        """
        raise NotImplementedError("Cette méthode doit être redéfinie dans une sous-classe.")
    
    def afficher_infos(self):
        """
        Affiche les informations du personnage.
        """
        print(f"Personnage : {self.nom}, Points de vie : {self.points_vie}")


class Guerrier(Personnage):
    """
    Classe représentant un guerrier, héritant de Personnage.
    """
    def __init__(self, nom: str):
        super().__init__(nom, points_vie=150)
    
    def attaquer(self):
        print(f"{self.nom} attaque avec son épée !")


class Mage(Personnage):
    """
    Classe représentant un mage, héritant de Personnage.
    """
    def __init__(self, nom: str):
        super().__init__(nom, points_vie=100)
    
    def attaquer(self):
        print(f"{self.nom} lance un sort de feu !")


class Archer(Personnage):
    """
    Classe représentant un archer, héritant de Personnage.
    """
    def __init__(self, nom: str):
        super().__init__(nom, points_vie=120)
    
    def attaquer(self):
        print(f"{self.nom} tire une flèche précise !")


# Exemple d'utilisation
if __name__ == "__main__":
    guerrier = Guerrier("Thor")
    mage = Mage("Merlin")
    archer = Archer("Legolas")
    
    guerrier.afficher_infos()
    guerrier.attaquer()
    
    mage.afficher_infos()
    mage.attaquer()
    
    archer.afficher_infos()
    archer.attaquer()