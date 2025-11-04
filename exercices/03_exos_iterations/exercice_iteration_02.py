# Exercice :
# Soit un capital `c` placé à un taux `t`. On veut connaître le nombre
# d'années nécessaire au doublement de ce capital.
# Exemple de calcul (le taux est de 4%, soit 0,04) :
# Cn = 10 000 x (1+0,04)^5 = 12 166 euros, soit un gain de 2 166 euros.


# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande de saisie du capital initial et du taux d'intérêt
capital_initial = float(input("Entrez le capital initial : "))
taux = float(input("Entrez le taux d'intérêt (ex: 4 pour 4%) : ")) / 100  # Convertit en décimal

# Initialisation
capital = capital_initial
annees = 0

# Boucle jusqu'à ce que le capital double
while capital < 2 * capital_initial:
    capital *= (1 + taux)  # Applique le taux d'intérêt
    annees += 1  # Incrémente le compteur d'années

# Affichage du résultat
print(f"Le capital double en {annees} ans.")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande de saisie du taux d'intérêt
taux = float(input("Entrez le taux d'intérêt (ex: 4 pour 4%) : ")) / 100  # Convertit en décimal

# Initialisation
capital = 1  # Peu importe le capital initial, on prend 1 comme référence
annees = 0

# Boucle jusqu'à ce que le capital double
while capital < 2:  # On cherche à doubler par rapport à 1 (ex: 1 → 2)
    capital *= (1 + taux)  # Applique le taux d'intérêt
    annees += 1  # Incrémente le compteur d'années

# Affichage du résultat
print(f"Le capital double en {annees} ans, quel que soit le capital initial.")

