# Exercice :
# Écrire un programme qui permet de tester si un profil est valable pour une
# candidature ou non selon ces trois critères :
#
# - L'âge minimum pour le poste est 30 ans.
# - Le salaire maximum possible est 40 000 euros.
# - Le nombre d'années d'expérience minimum est de 5 ans.
#
# On affichera différents messages pour chaque condition non respectée.
# Il est possible de réaliser cet exercice avec une seule structure conditionnelle
# ne comportant qu'une condition par clause (pas de `and` / `or`).

# Correction 1
print("Solution 1 :")
print() # saut de ligne 

# age = int(input("Saisir age : "))
# sal = int(input("Saisir salaire minimum demandé : "))
# xp = int(input("Saisir années d'expérience : "))

# if age < 30:
#     print("trop jeune")
# elif sal > 40000:
#     print("salaire demandé trop élevé")
# elif xp < 5:
#     print("pas assez d'expérience jeune homme/femme")
# else:
#     print("Bienvenue dans l'entreprise futur collègue !")

# Correction 2
print() # saut de ligne 
print("Solution 2 :")
print() # saut de ligne 

# age = int(input("Veuillez entrer votre âge : \n"))

# if age < 30 :
#     print("Vous n'avez pas l'âge requis pour cette candidature.")
#     exit()
    
# salaire = int(input("Salaire demandé \n"))

# if salaire > 40000 :
#     print("salaire demandé trop élevé")
#     exit()
    
# experience = int(input("Combien d'années d'expérience avez-vous ? \n"))

# if experience < 5 :
#     print("Vous n'avez pas l'expérience requise pour cette candidature.")
#     exit()
    
# print("Vous avez tous les critères pour être embauché(e).")

# Correction 3
print() # saut de ligne 
print("Solution 3 :")
print() # saut de ligne 

print("Entrez votre profil pour la validation de votre adéquation au poste")
age = int(input("Quel est votre age?\n"))
salaire = int(input("Quel salaire souhaitez vous?\n"))
experience = int(input("Combien d'années d'expérience avez vous ?\n"))

message =""
convient = True

if age < 30:
    message = "Vous n'avez pas l'age minimum requis\n"
    convient = False
    
if salaire > 40000:
    message += "Le salaire exigé est trop élevé\n"
    convient = False
    
if experience < 5:
    message += "Vous n'avez pas assez d'expérience"
    convient = False
    
if convient == True:
    message = "Votre profil convient"
    
print(message)
