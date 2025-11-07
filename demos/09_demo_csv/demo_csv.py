import csv

# Ecriture

# fichier2 = open("demo_csv/test.csv","wt",newline="")
# writer_csv = csv.writer(fichier2,delimiter=";")
# writer_csv.writerow(["titi",66,"au pif"])
# writer_csv.writerow(["toto",88,"lille"])
# writer_csv.writerow(["tata",24,"paris"])
# fichier2.close()


# Lecture et affichage de chaque ligne

# fichier = open("demo_csv/test.csv","rt")
# reader = csv.reader(fichier,delimiter=";")
# for row in reader:
#     print(row)
#     print(type(row))
#     print(row[0])
# fichier.close()


with open("demo_csv/test.csv",mode='r') as fichier:
    reader = csv.reader(fichier,delimiter=";")
    #print(reader)
    for row in reader:
        print(row)
        for element in row:
            print(element)

# with open("demo_csv/test.csv",mode='a',encoding="UTF-8",newline="") as fichier:
#     writer = csv.writer(fichier,delimiter=";")
#     writer.writerow(["Toto",16,"Playstation"])
#     writer.writerow(["Toto",16,"Playstation"])