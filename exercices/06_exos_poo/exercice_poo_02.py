# Exercice : Classe CompteBancaire

# Objectif :
# - Créer une classe `CompteBancaire` qui représente un compte bancaire.
#
# Étapes :
# 1. Définir la classe `CompteBancaire` avec les attributs suivants :
#    - `numero_compte` (int) : Numéro du compte.
#    - `nom` (str) : Nom du titulaire du compte.
#    - `solde` (int) : Solde du compte.
# 2. Créer un constructeur permettant d'initialiser ces attributs.
# 3. Ajouter une méthode `versement(montant)` pour gérer les dépôts d'argent.
# 4. Ajouter une méthode `retrait(montant)` pour gérer les retraits d'argent.
# 5. Ajouter une méthode `agios()` appliquant des frais de gestion de 5% du solde.
# 6. Ajouter une méthode `afficher()` pour afficher les détails du compte bancaire.


class CompteBancaire:
    """
    Classe représentant un compte bancaire.
    """
    def __init__(self, numero_compte: int, nom: str, solde: int = 0):
        """
        Initialise un compte bancaire avec un numéro, un nom et un solde initial.
        """
        self.numero_compte = numero_compte
        self.nom = nom
        self.solde = solde
    
    def versement(self, montant: int):
        """
        Ajoute un montant au solde du compte.
        """
        if montant > 0:
            self.solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Erreur : Le montant du versement doit être positif.")

    def retrait(self, montant: int):
        """
        Retire un montant du solde du compte si le solde est suffisant.
        """
        if 0 < montant <= self.solde:
            self.solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde : {self.solde}€")
        else:
            print("Erreur : Retrait impossible, solde insuffisant ou montant invalide.")

    def agios(self):
        """
        Applique un agio de 5% sur le solde du compte.
        """
        frais = self.solde * 0.05
        self.solde -= frais
        print(f"Agios de 5% appliqués ({frais:.2f}€). Nouveau solde : {self.solde:.2f}€")
    
    def afficher(self):
        """
        Affiche les informations du compte bancaire.
        """
        print(f"\nCompte N°{self.numero_compte}")
        print(f"Titulaire : {self.nom}")
        print(f"Solde : {self.solde}€\n")

    def __str__(self):
        return f"\nCompte N°{self.numero_compte} \nTitulaire : {self.nom} \nSolde : {self.solde}€"

# Exemple d'utilisation
if __name__ == "__main__":
    compte = CompteBancaire(numero_compte=123456, nom="Jean Dupont", solde=1000)
    compte.afficher()
    compte.versement(500)
    compte.retrait(200)
    compte.agios()
    compte.afficher()
    print(compte)

