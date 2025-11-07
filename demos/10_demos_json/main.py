import json, os

path = "demo_json/data.json"

if os.path.exists(path):
    with open(path,'r',encoding="utf8") as fichier:
        # Pour charger un fichier il nout faut la méthode .load()
        data = json.load(fichier)
        print(data)
        print(type(data))
else:
    with open(path,'w',encoding="utf8") as fichier:
        json.dump({"prénom": "Toto","nom": "tata"},fichier,indent=4,ensure_ascii=False)