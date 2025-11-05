# Une liste est une collection ordonnée et modifiable.

# Déclaration d'une liste
fruits = ["Pomme", "Banane", "Orange", "Mangue", "Ananas"]

# Les listes sont indexées, chaque élément a une position bien définie.
# En Python, les index commencent à 0 :
# Index :       0        1         2        3         4
# Liste :  ["Pomme", "Banane", "Orange", "Mangue", "Ananas"]

# Accès aux éléments avec un index positif
print(fruits[0])  # Affiche "Pomme"
print(fruits[2])  # Affiche "Orange"

# Accès aux éléments avec un index négatif
print(fruits[-1])  # Affiche "Ananas"
print(fruits[-3])  # Affiche "Orange"


# Modification d'un élément
fruits[1] = "Fraise"
print("Après modification :", fruits)

# Ajout d'éléments
fruits.append("Cerise")      # Ajoute à la fin
fruits.insert(2, "Kiwi")     # Insère à une position précise
print("Après ajouts :", fruits)

# Suppression d'éléments
fruits.remove("Mangue")      # Supprime la première occurrence
print("Après suppression :", fruits)

dernier_fruit = fruits.pop()  # Supprime et retourne le dernier élément
print("Dernier élément supprimé :", dernier_fruit)
print("Après pop :", fruits)

# Extension d'une liste avec extend()
autres_fruits = ["Framboise", "Myrtille"]
fruits.extend(autres_fruits)
print("Après extension :", fruits)

# Comptage d'un élément avec count()
fruits.append("Pomme")  # Ajout d'un doublon
nombre_de_pommes = fruits.count("Pomme")
print("Nombre de 'Pomme' dans la liste :", nombre_de_pommes)

# Extraction d'une sous-liste avec slicing (tranches)
print(fruits[1:4])   # Affiche ['Fraise', 'Kiwi', 'Orange']
print(fruits[:3])    # Affiche ['Pomme', 'Fraise', 'Kiwi']
print(fruits[::2])   # Affiche un élément sur deux

# Inverser une liste avec slicing
print(fruits[::-1])  # Liste inversée

# Vérification de la présence d'un élément
if "Pomme" in fruits:
    print("La Pomme est dans la liste")

# Longueur de la liste
print("Nombre total d'éléments :", len(fruits))
print("Nombre total d'éléments :", len("to to"))

# Trier une liste
fruits.sort()
print("Liste triée :", fruits)

# Effacer tous les éléments d'une liste
fruits.clear()
print("Liste après effacement :", fruits)

# ---------------------------------------------------------------------
# Exemple : une liste peut contenir différents types de données
# ---------------------------------------------------------------------

melange = [42, "Bonjour", 3.14, True, None]
print("Liste mixte :", melange)
print("Longueur de la liste mixte :", len(melange))

# Parcourir une liste
for element in melange:
    print("Élément :", element)

for i in range(len(melange)):
    print("Élément :", melange[i])

# ---------------------------------------------------------------------
#  Différences entre Liste, Tuple et Dictionnaire
# ---------------------------------------------------------------------

# Listes (list)
# - Ordonnées
# - Modifiables
# - Peuvent contenir des doublons

# Tuples (tuple)
# - Ordonnés
# - Immutables (non modifiables)
# - Peuvent contenir des doublons

# Dictionnaires (dict)
# - Modifiables
# - Stockent des paires clé-valeur uniques
# - Ordonnés depuis Python 3.7

# ---------------------------------------------------------------------
#  Bonnes Pratiques
# ---------------------------------------------------------------------

# - Utiliser une liste lorsque les données doivent être modifiées.
# - Utiliser un tuple lorsque les données ne doivent pas être modifiées.
# - Utiliser un dictionnaire pour stocker des informations sous forme clé-valeur.

# Fin du cours sur les conteneurs en Python