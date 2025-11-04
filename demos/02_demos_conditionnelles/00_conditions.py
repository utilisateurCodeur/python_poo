# 1. Condition simple avec if
# La condition 'if' permet d'exécuter un bloc de code si une expression est vraie.
# Exemple : Vérifier si une personne est majeure
age = 20

# if age >= 18:  # Si la condition est vraie
#     print("Vous êtes majeur.")  # Ce bloc est exécuté
#     print("Vous pouvez voter")

# Si la condition est fausse, rien ne se passe.

# 2. Condition avec if et else
# L'instruction 'else' permet de définir un bloc de code exécuté si la condition est fausse.
# age = 80
# if age >= 18:
#     print("Vous êtes majeur.")  # Si la condition est vraie
#     if age >= 60:
#         print("Vous pouvez prendre votre retraite")
# else:
#     print("Vous êtes mineur.")  # Sinon, ce bloc est exécuté


# 3. Condition avec if, elif et else
# 'elif' signifie "else if" et permet de tester plusieurs conditions successives.
# Python évalue les conditions dans l'ordre, et exécute le premier bloc dont la condition est vraie.
age = 10
if age < 12:
    print("Vous êtes un enfant.")  # Vérifie si l'âge est inférieur à 12
elif age < 18:
    print("Vous êtes un adolescent.")  # Si la première condition est fausse, vérifie cette condition
else:
    print("Vous êtes un adulte.")  # Si aucune condition précédente n'est vraie, ce bloc est exécuté

# 5. Conditions imbriquées
# On peut imbriquer des conditions pour tester plusieurs cas successifs.

temperature = 30
if temperature > 25:
    print("Il fait chaud.")
    if temperature > 35:
        print("Il fait très chaud ! Hydratez-vous.")
    else:
        print("Profitez du soleil, mais restez prudent.")
else:
    print("Le temps est agréable.")


# 6. Expression conditionnelle (Opérateur ternaire)
# En Python, on peut utiliser une expression conditionnelle en une seule ligne.

note = 9
resultat = "Réussi" if note >= 10 else "Échec"
print(f"Résultat de l'examen : {resultat}")

if note >= 10:
    resultat = "Réussi"
else:
    resultat = "Échec"

# 7. L'instruction pass
# L'instruction 'pass' permet d'écrire une structure conditionnelle sans action immédiate.

nom_utilisateur = ""

if nom_utilisateur:
    print(f"Bienvenue, {nom_utilisateur}")
else:
    pass  # Cette ligne évite une erreur si le bloc else est vide


# 8. Vérification de valeurs avec in
voyelles = "aeiouy"
lettre = "a"
print(lettre in voyelles)
if lettre in voyelles:
    print(f"{lettre} est une voyelle.")


# 9 Verification des types avec isinstance
valeur = 42
print(isinstance(valeur,str))
if isinstance(valeur,int):
    print("La valeur est un entier")