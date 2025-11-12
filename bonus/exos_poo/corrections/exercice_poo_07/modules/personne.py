class Personne:
    """
    Classe de base représentant une personne.
    """
    def __init__(self, nom: str, prenom: str):
        self.nom = nom
        self.prenom = prenom
    
    def afficher_details(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}")
