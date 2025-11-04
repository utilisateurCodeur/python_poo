# Exercice :
# Écrire un programme qui prend en entrée une température `temp` et qui
# renvoie l'état de l'eau à cette température, c'est-à-dire "SOLIDE", "LIQUIDE"
# ou "GAZEUX".
#
# On prendra comme conditions les suivantes :
# - Si la température est strictement négative, alors l'eau est à l'état solide.
# - Si la température est entre 0 et 100 (compris), l'eau est à l'état liquide.
# - Si la température est strictement supérieure à 100, l'eau est à l'état gazeux.
#
# Il est possible de réaliser cet exercice sans if imbriqué grâce au `elif`.

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# Demande de la température à l'utilisateur
temp = float(input("Entrez la température de l'eau en °C : "))

# Détermination de l'état de l'eau
if temp < 0:
    etat = "SOLIDE"
elif 0 <= temp <= 100:
    etat = "LIQUIDE"
else:  # temp > 100
    etat = "GAZEUX"

# Affichage du résultat
print(f"À {temp}°C, l'eau est à l'état : {etat}")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# Demande de la température
temp = float(input("Entrez la température de l'eau en °C : "))

# Utilisation de match-case
match temp:
    case t if t < 0:
        etat = "SOLIDE"
    case t if 0 <= t <= 100:
        etat = "LIQUIDE"
    case _:
        etat = "GAZEUX"

# Affichage du résultat
print(f"À {temp}°C, l'eau est à l'état : {etat}")

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

# Demande de la température
temp = float(input("Entrez la température de l'eau en °C : "))

# Détermination de l'état avec une expression conditionnelle
etat = "SOLIDE" if temp < 0 else "LIQUIDE" if temp <= 100 else "GAZEUX"

# Affichage du résultat
print(f"À {temp}°C, l'eau est à l'état : {etat}")