# Exercice :
# Écrire un algorithme qui demande successivement 6 nombres à l'utilisateur,
# et qui lui dit ensuite quel était le plus grand parmi ces 6 nombres.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande du premier nombre pour initialiser la comparaison
# max_nombre = float(input("Entrez un nombre : "))

# # Boucle pour demander les 5 nombres restants
# for _ in range(5):
#     nombre = float(input("Entrez un nombre : "))
#     # Mise à jour du maximum si le nombre saisi est plus grand
#     if nombre > max_nombre:
#         max_nombre = nombre

# # Affichage du plus grand nombre
# print(f"Le plus grand nombre saisi est : {max_nombre}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande du premier nombre pour initialiser la comparaison
# max_nombre = float(input("Entrez un nombre : "))

# # Initialisation du compteur
# compteur = 1

# # Boucle pour demander les 5 autres nombres
# while compteur < 6:
#     nombre = float(input("Entrez un nombre : "))
    
#     # Mise à jour du maximum
#     if nombre > max_nombre:
#         max_nombre = nombre
    
#     compteur += 1  # Incrémentation du compteur

# # Affichage du plus grand nombre
# print(f"Le plus grand nombre saisi est : {max_nombre}")

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

max_nombre = max(float(input("Entrez un nombre : ")) for _ in range(6))


# Affichage du résultat
print(f"Le plus grand nombre saisi est : {max_nombre}")