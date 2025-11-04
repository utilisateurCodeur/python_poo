import math  # Permet d'effectuer des calculs mathématiques avancés

# Utilisation d'une fonction du module `math`
print("Racine carrée de 25 :", math.sqrt(25))  # Affiche 5.0

from random import randint  # Importe uniquement `randint` du module `random`
# Utilisation de `randint()` pour générer un nombre aléatoire
print("Nombre aléatoire entre 1 et 10 :", randint(1, 10))

# Importation avec alias
import datetime as dt  # On donne un alias `dt` au module `datetime`

# Affichage de la date et de l'heure actuelles
print("Date et heure actuelles :", dt.datetime.now())

# Vérification des modules chargés
import sys
print("Modules chargés :", list(sys.modules.keys()))  # Affiche la liste des modules importés