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
