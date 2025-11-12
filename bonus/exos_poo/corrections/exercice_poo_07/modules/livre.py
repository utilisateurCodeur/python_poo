class Livre:
    """
    Classe représentant un livre dans la bibliothèque.
    """
    def __init__(self, titre: str, auteur: str, isbn: str):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn
        self.disponible = True
    
    def emprunter(self):
        if self.disponible:
            self.disponible = False
        
    def rendre(self):
        self.disponible = True
    
    def afficher_details(self):
        etat = "Disponible" if self.disponible else "Emprunté"
        print(f"Livre: {self.titre}, Auteur: {self.auteur}, ISBN: {self.isbn}, État: {etat}")
