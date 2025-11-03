# Pour vérifier le type d'un objet, nous utilisons la fonction type()
texte = "   bonjour, Python est génial!   "
print(f"Le type de l'objet texte est : {type(texte)}")  # Affiche <class 'str'>

# Comme 'texte' est un objet de type str (chaîne de caractères), il possède des méthodes spécifiques aux chaînes.

# 1. Suppression des espaces inutiles
print(f"Avant strip(): '{texte}'")
print(f"Après strip(): '{texte.strip()}'")  # Supprime les espaces en début et fin

# 2. Conversion en majuscules et minuscules
print(f"En majuscules : {texte.upper()}")  # Convertit en majuscules
print(f"En minuscules : {texte.lower()}")  # Convertit en minuscules

# 3. Capitalisation 
print(f"Première lettre en majuscule : {texte.strip().capitalize()}")  # Met la première lettre en majuscule

# 4. Remplacement de texte
print(f"Remplacement de 'Python' par 'Java' : {texte.replace('Python', 'Java')}")


# 5. Vérification de contenu
print(f"Le texte commence-t-il par 'Bonjour' ? {texte.startswith('Bonjour')}")
print(f"Le texte se termine-t-il par '!' ? {texte.endswith('!')}")

# 6. Recherche dans une chaîne
print(f"Nombre d'occurrences de 'on' : {texte.count('on')}")

# 7. Vérification du type de contenu
print(f"La chaîne contient-elle uniquement des lettres ? {texte.isalpha()}")  # False car il y a des espaces et des signes
print(f"La chaîne contient-elle uniquement des chiffres ? {'12345'.isdigit()}")  # True car uniquement des chiffres
