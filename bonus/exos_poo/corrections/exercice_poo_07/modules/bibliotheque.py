from livre import Livre
from adherent import Adherent

class Bibliotheque:
    """
    Classe représentant une bibliothèque.
    """
    def __init__(self):
        self.livres = []
        self.adherents = []
    
    def ajouter_livre(self, livre: Livre):
        self.livres.append(livre)
    
    def ajouter_adherent(self, adherent: Adherent):
        self.adherents.append(adherent)
    
    def rechercher_livre(self, titre: str) -> Livre:
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None
    
    def emprunter_livre(self, adherent: Adherent, livre: Livre):
        if adherent in self.adherents and livre in self.livres:
            adherent.emprunter_livre(livre)
    
    def rendre_livre(self, adherent: Adherent, livre: Livre):
        if adherent in self.adherents and livre in self.livres:
            adherent.rendre_livre(livre)
    
    def afficher_details(self):
        print("Bibliothèque :")
        print("Livres disponibles :")
        for livre in self.livres:
            if livre.disponible:
                livre.afficher_details()
        print("\nAdhérents inscrits :")
        for adherent in self.adherents:
            adherent.afficher_details()
