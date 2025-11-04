# Exercice :
# Écrire un algorithme qui demande l'âge d'un enfant à l'utilisateur,
# ensuite, il l'informe de sa catégorie pour une licence sportive :
# - 'Baby' entre 3 et 6 ans.
# - 'Poussin' entre 7 et 8 ans.
# - 'Pupille' entre 9 et 10 ans.
# - 'Minime' entre 11 et 12 ans.
# - 'Cadet' à partir de 13 ans.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande de l'âge à l'utilisateur
age = int(input("Entrez l'âge de l'enfant : "))

# Détermination de la catégorie
if 3 <= age <= 6:
    categorie = "Baby"
elif 7 <= age <= 8:
    categorie = "Poussin"
elif 9 <= age <= 10:
    categorie = "Pupille"
elif 11 <= age <= 12:
    categorie = "Minime"
elif age >= 13:
    categorie = "Cadet"
else:
    categorie = "Âge non valide pour une catégorie sportive"

# Affichage du résultat
print(f"L'enfant appartient à la catégorie : {categorie}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande de l'âge à l'utilisateur
age = int(input("Entrez l'âge de l'enfant : "))

# Détermination de la catégorie avec match-case
match age:
    case n if 3 <= n <= 6:
        categorie = "Baby"
    case n if 7 <= n <= 8:
        categorie = "Poussin"
    case n if 9 <= n <= 10:
        categorie = "Pupille"
    case n if 11 <= n <= 12:
        categorie = "Minime"
    case n if n >= 13:
        categorie = "Cadet"
    case _:
        categorie = "Âge non valide pour une catégorie sportive"

# Affichage du résultat
print(f"L'enfant appartient à la catégorie : {categorie}")