# Exercice :
# Écrire un algorithme qui demande un nombre entier à l'utilisateur,
# puis qui teste et affiche s'il est divisible par 3. 
# Si le nombre est divisible par 3, affichez "Le nombre est divisible par 3".
# Sinon, affichez "Le nombre n'est pas divisible par 3".


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande de saisie à l'utilisateur
nombre = int(input("Entrez un nombre entier : "))

# Vérification de la divisibilité par 3
if nombre % 3 == 0:
    print("Le nombre est divisible par 3.")
else:
    print("Le nombre n'est pas divisible par 3.")

    # Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande de saisie à l'utilisateur
nombre = int(input("Entrez un nombre entier : "))

# Vérification avec opérateur ternaire
message = "Le nombre est divisible par 3." if nombre % 3 == 0 else "Le nombre n'est pas divisible par 3."

# Affichage du résultat
print(message)


# solution 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

print("Le nombre est divisible par 3." if int(input("Entrez un nombre entier : ")) % 3 == 0 else "Le nombre n'est pas divisible par 3.")