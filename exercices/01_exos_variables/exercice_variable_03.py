# Exercice :
# Écrire un programme, qui, à partir de la saisie d'un nom et prénom,
# affiche le message suivant :
# Bonjour M. Ou Mme {Prénom} {Nom}
# Il peut être utile de regarder les méthodes lower, upper,
# capitalize pour forcer la casse.


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

nom = input("Votre Nom ? ")
nom = nom.upper()
prenom = input("Votre Prénom ? ")
prenom = prenom.title()
# affichage = f"Bonjour M. ou Mme. \"{prenom}\" \"{nom}\"."
affichage = f'Bonjour M. ou Mme. "{prenom}" "{nom}".'
print(affichage)