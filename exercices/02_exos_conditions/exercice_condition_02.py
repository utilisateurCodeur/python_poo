# Exercice :
# Dans une reprographie, le coût des photocopies dépend de la quantité demandée :
# - Pour moins de 10 copies, le prix est de 0,5 euros par copie.
# - Pour un nombre de copies entre 10 et 20 inclus, le prix est de 0,4 euros par copie.
# - Au-delà de 20 copies, le prix est de 0,3 euros par copie.
# 
# Écrivez un algorithme qui demande à l'utilisateur le nombre de
# photocopies à effectuer et qui calcule le prix à payer.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande du nombre de copies à l'utilisateur
nb_copies = int(input("Entrez le nombre de photocopies : "))

# Calcul du prix total
if nb_copies < 10:
    prix_total = nb_copies * 0.5
elif nb_copies <= 20:
    prix_total = nb_copies * 0.4
else:
    prix_total = nb_copies * 0.3

# Affichage du prix total
print(f"Le prix à payer est de {prix_total:.2f} euros.")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande du nombre de copies
nb_copies = int(input("Entrez le nombre de photocopies : "))

# Utilisation d'une expression conditionnelle pour le calcul du prix
prix_total = nb_copies * (0.5 if nb_copies < 10 else (0.4 if nb_copies <= 20 else 0.3))

# Affichage du prix total
print(f"Le prix à payer est de {prix_total:.2f} euros.")

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

# Demande du nombre de copies
nb_copies = int(input("Entrez le nombre de photocopies : "))

# Utilisation de match-case
match nb_copies:
    case n if n < 10:
        prix_total = n * 0.5
    case n if 10 <= n <= 20:
        prix_total = n * 0.4
    case _:
        prix_total = nb_copies * 0.3

# Affichage du prix total
print(f"Le prix à payer est de {prix_total:.2f} euros.")