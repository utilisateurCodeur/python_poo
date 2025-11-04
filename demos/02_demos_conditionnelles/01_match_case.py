# La structure 'match-case' est une alternative plus lisible aux chaînes de if-elif-else.
# Introduite dans Python 3.10, elle permet d'effectuer un filtrage de motifs (pattern matching).


# 1. Utilisation de match-case de base
# Exécutons un cas simple avec une valeur donnée.

day = "mardi"
match day:
    case "lundi":
        print("Début de la semaine !")
    case "mardi":
        print("Deuxième jour de travail.")
    case "samedi" | "dimanche":  # Plusieurs valeurs pour un même cas
        print("C'est le week-end !")
    case _:
        print("Jour non reconnu.")  # Le cas '_' sert de valeur par défaut (équivalent à else)


# 2. Utilisation avec des types et motifs variés
# On peut tester plusieurs types de valeurs avec 'match'.

valeur = "42.0"
match valeur:
    case int():  # Vérifie si c'est un entier
        print("C'est un nombre entier.")
    case float():
        print("C'est un nombre flottant.")
    case str():
        print("C'est une chaîne de caractères.")
    case _:
        print("Type inconnu.")


# 3. Filtrage avec conditions supplémentaires (garde 'if')
# On peut ajouter une condition après un cas.

nombre = 14
match nombre:
    case x if x % 2 == 0:
        print(f"{x} est un nombre pair.")
    case x if x % 2 != 0:
        print(f"{x} est un nombre impair.")
    case _:
        print("Valeur inconnue.")