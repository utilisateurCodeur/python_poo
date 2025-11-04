# Exercice :
# Nous devons écrire un algorithme qui demande à l'utilisateur de
# saisir un nombre compris entre 1 et 3, et qui répète cette demande
# tant que la réponse de l'utilisateur n'est pas valide.


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande de saisie à l'utilisateur
# nombre = int(input("Entrez un nombre entre 1 et 3 : "))

# # Boucle tant que la saisie est invalide
# while nombre < 1 or nombre > 3:
#     print("Entrée invalide. Veuillez recommencer.")
#     nombre = int(input("Entrez un nombre entre 1 et 3 : "))

# # Affichage du nombre valide
# print(f"Vous avez saisi le nombre valide : {nombre}")


# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 


while True:
    nombre = input("Entrez un nombre entre 1 et 3 : ")
    
    # Vérifie si l'entrée est un nombre
    if nombre.isdigit():  
        nombre = int(nombre)
        if 1 <= nombre <= 3:
            break  # Sort de la boucle si le nombre est valide
    
    print("Entrée invalide. Veuillez recommencer.")

# Affichage du nombre valide
print(f"Vous avez saisi le nombre valide : {nombre}")