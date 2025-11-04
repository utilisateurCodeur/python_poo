
def saluer(nom):
    """Retourne un message de salutation avec le nom donné."""
    return f"Bonjour, {nom} !"

# Définition d'une variable globale
VERSION = "1.0"

def addition(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

if __name__ == "__main__":
    print("Ce module est executer")
    print(saluer("Toto"))
    print(f"Le module {__name__} est utilisée (fichier : mon_module.py)")