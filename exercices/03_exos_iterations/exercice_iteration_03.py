# Exercice :
# Écrire un algorithme permettant d'afficher la table de multiplication par 9.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Affichage de la table de multiplication par 9
print("Table de multiplication par 9 :")
for i in range(1, 11):
    print(f"9 x {i} = {9 * i}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Affichage de la table de multiplication par 9 avec while
print("Table de multiplication par 9 :")
i = 1
while i <= 10:
    print(f"9 x {i} = {9 * i}")
    i += 1