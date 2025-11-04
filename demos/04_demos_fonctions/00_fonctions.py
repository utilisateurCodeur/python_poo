# En Python, une fonction est définie avec le mot-clé `def`, suivi :
#  - d'un NOM de fonction
#  - de PARENTHESES `()` contenant éventuellement des PARAMÈTRES
#  - d'un DEUX-POINTS `:` pour indiquer le début du bloc d'instructions
#  - d'un INDENTATION (espace ou tabulation) pour écrire les instructions de la fonction
#  - éventuellement d'un `return` pour renvoyer une valeur

# Fonction sans paramètre ni valeur de retour
def saluer():
    """
    Affiche un message de salutation
    (infos dans les docstings)
    """
    print("Bonjour tout le monde !")

# Appel de la fonction
saluer()  # Affiche "Bonjour tout le monde !"

# Fonction avec paramètres

def saluer_personne(nom: str):
    """
    Affiche un message de bienvenue personnalisé avec un nom
    """
    print(f"Bonjour, {nom} !")

saluer_personne("toto")
saluer_personne("tata")
# saluer_personne(input("saisir un nom :"))

# Fonction avec retour de valeur

def addition(a: int, b:int) -> int:
    """
    Retourne la somme de deux nombres
    """
    return a + b

# Stocker et afficher le résultat
resultat = addition(5,3)
print(f"Résultat de l'addition : {resultat}")

# Paramètres avec valeurs par défaut

def bienvenue(nom:str = "Invité"):
    # Affiche un message de bienvenue avec un nom par défaut
    print(f"Bienvenue, {nom} !")

# Appels de la fonction avec et sans argument
bienvenue("Bob")      # Affiche "Bienvenue, Bob !"
bienvenue()           # Affiche "Bienvenue, Invité !"

# Syntaxe d'une fonction lambda :
# lambda paramètres: expression

# Exemple classique d'une fonction normale pour additionner deux nombres :
def addition_normale(x, y):
    return x + y

# Équivalent avec une fonction lambda :
addition_lambda = lambda x,y: x+y

# Appels des fonctions
print(addition_normale(2, 3))  # Affiche 5
print(addition_lambda(2, 3))   # Affiche 5
print(addition_lambda(6, 6))
print(2 * addition_lambda(2,2))
print(addition_lambda)

# Fonction lambda utilisée directement dans `print`
print((lambda a, b: a * b)(3, 4))  # Affiche 12

# Documentation des Fonctions (Docstring)

def greet(name):
    """
    Cette fonction prend un nom en entrée et affiche un message de bienvenue.
    :param name: str, le nom de la personne à saluer
    :return: str, le message de bienvenue
    """
    return f"Bonjour, {name} !"

import math

print(greet.__doc__)
print(help(greet))
print(help(math))