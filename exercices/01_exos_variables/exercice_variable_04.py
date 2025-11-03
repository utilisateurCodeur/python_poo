# Exercice :
# Écrire un programme qui, à partir de la saisie d'un rayon et d'une
# hauteur, calcule le volume d'un cône droit.
#
# Rappel : La formule du volume d'un cône droit est :
# V = (1/3) * π * r^2 * h
# où `r` est le rayon de la base et `h` est la hauteur du cône.


# Correction 1
print("Solution 1 :")
print() # saut de ligne 


# Demande de saisie à l'utilisateur
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Approximation de π
pi_approx = 3.141592653589793

# Calcul du volume du cône
volume = (1/3) * pi_approx * (rayon ** 2) * hauteur

# Affichage du résultat
print(f"Le volume du cône est : {volume}")
print(f"Le volume du cône est : {volume:.2f}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 


import math

# Demande de saisie à l'utilisateur
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume du cône
volume = (1/3) * math.pi * (rayon ** 2) * hauteur

# Affichage du résultat
print(f"Le volume du cône est : {volume:.2f}")