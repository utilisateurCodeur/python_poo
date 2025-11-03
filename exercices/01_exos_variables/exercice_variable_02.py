# Exercice :
# Écrire un algorithme permettant d'échanger les valeurs de deux variables `a` et `b`.

a = 1
b = 2

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

print("Valeur de a avant échange:", a)
print("Valeur de b avant échange:", b)

# Échange avec une variable temporaire
temp = a
a = b
b = temp

# Affichage des valeurs échangées
print("Valeur de a après échange:", a)
print("Valeur de b après échange:", b)

# Correction 2
print()# saut de ligne 
print("Solution 2 :")
print()# saut de ligne 

# Re-Initialisation des variables
a = 1
b = 2

print("Valeur de a avant échange:", a)
print("Valeur de b avant échange:", b)

# Échange Pythonique avec unpacking
a,b = b,a

# Affichage des valeurs échangées
print("Valeur de a après échange:", a)
print("Valeur de b après échange:", b)

