# Exercice : Gestion d'une Bibliothèque

# Objectif :
# - Implémenter un système de gestion de bibliothèque en appliquant les principes de la Programmation Orientée Objet.
# - Utiliser l'encapsulation, l'héritage, le polymorphisme et la composition.

# Étapes :

# 1️⃣ Création des classes de base
# - Créer une classe `Livre` représentant un livre avec les attributs :
#   - `titre` (str) : Titre du livre.
#   - `auteur` (str) : Auteur du livre.
#   - `isbn` (str) : Identifiant unique du livre.
#   - `disponible` (bool) : Indique si le livre est disponible (par défaut `True`).
# - Ajouter les méthodes suivantes :
#   - `emprunter()` : Change l'état de disponibilité du livre à `False`.
#   - `rendre()` : Change l'état de disponibilité du livre à `True`.

# 2️⃣ Encapsulation et héritage
# - Créer une classe `Personne` avec les attributs :
#   - `nom` (str) : Nom de la personne.
#   - `prenom` (str) : Prénom de la personne.
#
# - Créer une classe `Adherent` qui hérite de `Personne` et ajoute :
#   - `numero_adherent` (int) : Numéro unique de l'adhérent.
#   - `livres_empruntes` (list) : Liste des livres empruntés par l'adhérent.
# - Ajouter les méthodes suivantes :
#   - `emprunter_livre(livre: Livre)` : L'adhérent peut emprunter un livre s'il en a moins de 3.
#   - `rendre_livre(livre: Livre)` : L'adhérent peut rendre un livre.

# 3️⃣ Composition (Une classe contenant d'autres objets)
# - Créer une classe `Bibliotheque` qui gère les livres et les adhérents avec les attributs :
#   - `livres` (list) : Liste des livres disponibles dans la bibliothèque.
#   - `adherents` (list) : Liste des adhérents inscrits à la bibliothèque.
# - Ajouter les méthodes suivantes :
#   - `ajouter_livre(livre: Livre)` : Ajoute un livre à la bibliothèque.
#   - `ajouter_adherent(adherent: Adherent)` : Ajoute un adhérent à la bibliothèque.
#   - `rechercher_livre(titre: str) -> Livre` : Recherche un livre par son titre.
#   - `emprunter_livre(adherent: Adherent, livre: Livre)` : Gère l'emprunt d'un livre par un adhérent.
#   - `rendre_livre(adherent: Adherent, livre: Livre)` : Gère le retour d'un livre par un adhérent.

# 4️⃣ Polymorphisme
# - Ajouter une méthode `afficher_details()` dans chaque classe pour afficher les informations correspondantes.


class Livre:
    """
    Classe représentant un livre dans la bibliothèque.
    """
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
        
    def rendre(self):
        self.disponible = True
    
    def afficher_details(self):
        etat = "Disponible" if self.disponible else "Emprunté"
        print(f"Livre: {self.titre}, Auteur: {self.auteur}, ISBN: {self.isbn}, État: {etat}")


class Personne:
    """
    Classe de base représentant une personne.
    """
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom
    
    def afficher_details(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}")


class Adherent(Personne):
    """
    Classe représentant un adhérent de la bibliothèque.
    """
    def __init__(self, nom: str, prenom: str, numero_adherent: int):
        super().__init__(nom, prenom)
        self.numero_adherent = numero_adherent
        self.livres_empruntes = []
    
    def emprunter_livre(self, livre: Livre):
        if len(self.livres_empruntes) < 3 and livre.disponible:
            livre.emprunter()
            self.livres_empruntes.append(livre)
    
    def rendre_livre(self, livre: Livre):
        if livre in self.livres_empruntes:
            livre.rendre()
            self.livres_empruntes.remove(livre)
    
    def afficher_details(self):
        print(f"Adhérent N°{self.numero_adherent} - {self.nom} {self.prenom}, Livres empruntés: {len(self.livres_empruntes)}")


class Bibliotheque:
    """
    Classe représentant une bibliothèque.
    """
    def __init__(self):
        self.livres = []
        self.adherents = []
    
    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)
    
    def ajouter_adherent(self, adherent: Adherent):
        self.adherents.append(adherent)
    
    def rechercher_livre(self, titre: str) -> Livre:
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None
    
    def emprunter_livre(self, adherent: Adherent, livre: Livre):
        if adherent in self.adherents and livre in self.livres:
            adherent.emprunter_livre(livre)
    
    def rendre_livre(self, adherent: Adherent, livre: Livre):
        if adherent in self.adherents and livre in self.livres:
            adherent.rendre_livre(livre)
    
    def afficher_details(self):
        print("Bibliothèque :")
        print("Livres disponibles :")
        for livre in self.livres:
            if livre.disponible:
                livre.afficher_details()
        print("\nAdhérents inscrits :")
        for adherent in self.adherents:
            adherent.afficher_details()


# Exemple d'utilisation
if __name__ == "__main__":
    biblio = Bibliotheque()
    livre1 = Livre("1984", "George Orwell", "123456")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "789101")
    adherent1 = Adherent("Dupont", "Jean", 1)
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_adherent(adherent1)
    
    adherent1.emprunter_livre(livre1)
    biblio.afficher_details()
    adherent1.rendre_livre(livre1)
    biblio.afficher_details()
