# Exercice :
# Écrire un programme qui utilise une fonction retournant, à partir de deux nombres envoyés en paramètres :
# - La somme des deux nombres
# - La différence des deux nombres
# - Le quotient des deux nombres 
# - Le produit des deux nombres
#
# La fonction prendra donc deux nombres en entrée et renverra les 4 résultats : somme, différence, quotient et produit.
#
# Ensuite, vous testerez cette fonction dans un programme console qui :
# 1. Demande à l'utilisateur de saisir deux valeurs.
# 2. Utilise la fonction pour calculer les 4 résultats.
# 3. Affiche ces résultats à l'utilisateur dans la console.


def calculs(a: float, b: float):
    """
    Prend deux nombres en entrée et retourne :
    - La somme
    - La différence
    - Le quotient (gère la division par zéro)
    - Le produit
    """
    somme = a + b
    difference = a - b
    produit = a * b
    quotient = a / b 

    return (somme, difference, quotient, produit)

# Demande de saisie des deux nombres
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

# Appel de la fonction
s, d, q, p = calculs(a, b)
recup = calculs(a, b)
diff = recup[1]
_, diff2,_,_ = recup

print(diff)
print(diff2)

print(f"Somme : {s}")
print(f"Différence : {d}")
print(f"Produit : {p}")
print(f"Quotient : {q}")


