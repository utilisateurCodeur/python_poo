# 1. Déclaration classique avec des parenthèses
couleurs = ("Rouge", "Vert", "Bleu", "Jaune", "Noir")

# 2. Déclaration sans parenthèses (Python comprend automatiquement que c'est un tuple)
animaux = "Chat", "Chien", "Oiseau"

# 3. Tuple avec un seul élément (attention à la virgule)
mon_tuple = ("Unique",)   # Correct
autre_tuple = "Seul",     # Correct
tuple_faux = ("Unique")   # Faux (ceci est une chaîne, pas un tuple)

# Vérification des types
print(type(couleurs))     # <class 'tuple'>
print(type(animaux))      # <class 'tuple'>
print(type(mon_tuple))    # <class 'tuple'>
print(type(tuple_faux))   # <class 'str'>


# Accès aux éléments d'un tuple
print(couleurs[0])   # "Rouge" (1er élément)
print(couleurs[-1])  # "Noir" (dernier élément)

# Extraction d’une sous-partie avec slicing
print(couleurs[1:4])  # ('Vert', 'Bleu', 'Jaune')

# Vérifier la présence d'un élément
if "Vert" in couleurs:
    print("Le Vert est dans le tuple")

# Utilisation de len() et de .index()

# Longueur du tuple
print("Nombre d'éléments dans 'couleurs' :", len(couleurs))

# Trouver la position d'un élément
index_bleu = couleurs.index("Bleu")
print("Index de 'Bleu' :", index_bleu)  # Affiche 2

# Exemple de tuple contenant plusieurs types de données

mixte = (42, "Bonjour", 3.14, False, None)
print("Tuple mixte :", mixte)
print("Longueur du tuple mixte :", len(mixte))

# Accès aux éléments variés
for element in mixte:
    print("Élément :", element)

# Retour multiple d'une fonction (Python retourne un tuple)

def calculs(a, b):
    somme = a + b
    produit = a * b
    return somme, produit  # Retourne un tuple

# Récupération du tuple
resultat = calculs(4, 5)
print("Retour de la fonction :", resultat)  # (9, 20)
print("Type du retour :", type(resultat))   # <class 'tuple'>

# Décomposition du tuple en plusieurs variables
somme_result, produit_result = calculs(4, 5)
print("Somme :", somme_result)
print("Produit :", produit_result)

# Conversion d'un tuple en liste (pour le modifier)

couleurs_liste = list(couleurs)
couleurs_liste.append("Blanc")     # Modification possible
couleurs = tuple(couleurs_liste)   # Reconverti en tuple
print("Tuple modifié :", couleurs)