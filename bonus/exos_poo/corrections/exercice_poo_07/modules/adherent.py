from livre import Livre
from personne import Personne

class Adherent(Personne):
    """
    Classe représentant un adhérent de la bibliothèque.
    """
    def __init__(self, nom: str, prenom: str, numero_adherent: int):
        super().__init__(nom, prenom)
        self.numero_adherent = numero_adherent
        self.livres_empruntes = []
    
    def emprunter_livre(self, livre: Livre):
        if len(self.livres_empruntes) < 3 and livre.disponible:
            livre.emprunter()
            self.livres_empruntes.append(livre)
    
    def rendre_livre(self, livre: Livre):
        if livre in self.livres_empruntes:
            livre.rendre()
            self.livres_empruntes.remove(livre)
    
    def afficher_details(self):
        print(f"Adhérent N°{self.numero_adherent} - {self.nom} {self.prenom}, Livres empruntés: {len(self.livres_empruntes)}")
