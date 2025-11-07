import os

path = "fichier.txt"

# verifier que le fichier existe
# if not os.path.exists(path):
#     fichier = open(path,"w")
#     fichier.write("du texte")
#     fichier.close()
# else:
#     fichier = open(path,"r")
#     contenu = fichier.read()
#     print(f"Contenu du fichier : {contenu}")
#     fichier.close()

open()

if not os.path.exists(path):
    with open(path,"w") as mon_fichier:
        mon_fichier.write("toto")
        mon_fichier.write("tata")
else:
    with open(path,'r') as fichier:
        contenu = fichier.read()
        print(f"Contenu du fichier : {contenu}")