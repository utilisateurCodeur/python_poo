from bibliotheque import Bibliotheque
from livre import Livre
from adherent import Adherent

if __name__ == "__main__":
    biblio = Bibliotheque()
    livre1 = Livre("1984", "George Orwell", "123456")
    livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", "789101")
    adherent1 = Adherent("Dupont", "Jean", 1)
    
    biblio.ajouter_livre(livre1)
    biblio.ajouter_livre(livre2)
    biblio.ajouter_adherent(adherent1)
    
    adherent1.emprunter_livre(livre1)
    biblio.afficher_details()
