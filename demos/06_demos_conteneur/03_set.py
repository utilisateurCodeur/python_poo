# 2. Déclaration et propriétés de base

# Déclaration d'un ensemble
fruits = {"Pomme", "Banane", "Orange", "Ananas"}

print("Contenu de l'ensemble :", fruits)
print("Type :", type(fruits))
print("Nombre d'éléments :", len(fruits))

# Tentative d’ajout d’un doublon (n’aura aucun effet)
fruits.add("Pomme")
print("Après ajout d'un doublon :", fruits)

# Ajout d’un nouvel élément
fruits.add("Mangue")
print("Après ajout :", fruits)

# Suppression d’un élément existant
fruits.remove("Banane")
print("Après suppression :", fruits)

# Suppression sécurisée (sans erreur si l’élément n’existe pas)
fruits.discard("Cerise")
print("Après discard (élément inexistant) :", fruits)

# Supprimer et retourner un élément aléatoire
retire = fruits.pop()
print("Élément retiré :", retire)
print("Ensemble après pop() :", fruits)

# Effacer tous les éléments
fruits.clear()
print("Ensemble vidé :", fruits)

#  Création à partir d’autres structures
# Conversion d’une liste ou d’un tuple en set (utile pour supprimer les doublons)
liste_avec_doublons = ["Python", "Java", "Python", "C", "Java"]
ensemble_langages = set(liste_avec_doublons)
print("Ensemble sans doublons :", ensemble_langages)

# Conversion inverse (set → list)
liste_sans_doublons = list(ensemble_langages)
print("Liste obtenue :", liste_sans_doublons)