# Commentaire en Python
# Un commentaire est un texte ignoré par l'interpreteur python
# Il commence par le symbloe #

# print("coucou") # ceci est un coucou

"""
Ceci est il un commentaire ? Non c'est une DocString
sur plusieur lignes
"""

# Règles de bonnes pratiques en Python
# 1. Utiliser des noms de variables explicites (éviter x, y, z sauf pour les maths).
# 2. Respecter la convention de nommage :
#    - snake_case pour les variables et fonctions : exemple_variable
#    - PascalCase pour les classes : ExempleClasse
#    - CONSTANTES en majuscules : EXEMPLE_CONSTANTE
# 3. Ajouter des commentaires clairs mais éviter d'en abuser.
# 4. Respecter la PEP 8 (guide de style de Python).


# Une variable est un conteneur qui stocke une valeur.
# En Python, une variable est créée dès qu'on lui assigne une valeur.

# Déclaration et affectation de variables
nom = "Alice"  # Variable de type chaîne de caractères (str)
age = 25       # Variable de type entier (int)
taille = 1.75  # Variable de type flottant (float)
est_majeur = True  # Variable de type booléen (bool)

# Affichage des variables
print("Mon nom est :",nom," et ma taille est :",taille,"m")
print(f"Mon nom est : {nom} et ma taille est {taille}m")
print(f"Nom : {nom}")
print(f"Âge : {age}")
print(f"Taille : {taille}m")
print(f"Majeur : {est_majeur}")

# La fonction type()
# La fonction type() permet de connaître le type d'une variable.
# C'est utile pour vérifier si une variable contient bien le type attendu.
print(type("Bonjour"))  # Affichera <class 'str'>
print(type(42))          # Affichera <class 'int'>
print(type(3.14))        # Affichera <class 'float'>
print(type(True))        # Affichera <class 'bool'>

# Vérification du type d'une variable avec type()
print(f"Type de nom : {type(nom)}")
print(f"Type de age : {type(age)}")
print(f"Type de taille : {type(taille)}")
print(f"Type de est_majeur : {type(est_majeur)}")

# Changement de valeur d'une variable
nom = "Bob"
print(f"Nouveau nom : {nom}")

# Assignation multiple (affectation simultanée)
x, y, z = 10, 20, "toto"
print(f"x = {x}, y = {y}, z = {z}")

# Échange de valeurs entre deux variables
x, y = y, x
print(f"Après échange : x = {x}, y = {y}")

# Concaténation de chaînes de caractères
message = "Bonjour " + nom + " !"
print(message)

# Conversion de types (casting)
# recuperation = "42"
# calcul = int(recuperation) + 10
# print(f"ma recuperation + 10 est = : {calcul}")
# # recuperation= input("Saisir un nombre :")
# # recuperation = float(recuperation)
# recuperation = int(input("Saisir un nombre :"))
# print(type(recuperation))
# print(recuperation)

prenom: str = "42"
print(prenom)

variable = 55.2091
print(f"{variable:^7.2f}") # 55.21

valeur1 = 0
valeur2 = ""
valeur3 = False
valeur4 = None

print(f"Conversion de {valeur1} en booléen : {bool(valeur1)}")  # False
print(f"Conversion de '{valeur2}' en booléen : {bool(valeur2)}") # False
print(f"Conversion de {valeur3} en booléen : {bool(valeur3)}") # False
print(f"Conversion de {valeur4} en booléen : {bool(valeur4)}") # False



