# Exercice : Système de Paiement

# Objectif :
# - Implémenter un système de paiement avec des moyens de paiement diversifiés utilisant l'héritage.
#
# Étapes :
# 1. Créer une classe `MoyenDePaiement` avec un attribut `solde` et une méthode `payer(montant)`.
# 2. Créer trois sous-classes `CarteBancaire`, `Paypal` et `Crypto` héritant de `MoyenDePaiement`.
#    - `CarteBancaire` valide la transaction si le solde est suffisant.
#    - `Paypal` applique des frais fixes par transaction.
#    - `Crypto` applique des frais variables en fonction du montant.

class MoyenDePaiement:
    """
    Classe de base représentant un moyen de paiement.
    """
    def __init__(self, solde: float):
        """
        Initialise un moyen de paiement avec un solde disponible.
        """
        self.solde = solde
    
    def payer(self, montant: float) -> bool:
        """
        Méthode générique de paiement, à redéfinir dans les sous-classes.
        """
        raise NotImplementedError("Cette méthode doit être redéfinie dans une sous-classe.")


class CarteBancaire(MoyenDePaiement):
    """
    Classe représentant un paiement par carte bancaire.
    """
    def payer(self, montant: float) -> bool:
        """
        Effectue le paiement si le solde est suffisant.
        """
        if self.solde >= montant:
            self.solde -= montant
            print(f"Paiement de {montant:.2f}€ par Carte Bancaire effectué. Solde restant : {self.solde:.2f}€")
            return True
        else:
            print("Paiement refusé : solde insuffisant sur la Carte Bancaire.")
            return False


class Paypal(MoyenDePaiement):
    """
    Classe représentant un paiement via PayPal avec des frais fixes.
    """
    FRAIS_FIXES = 2.0  # Frais fixes de 2€ par transaction
    
    def payer(self, montant: float) -> bool:
        """
        Effectue le paiement avec des frais fixes.
        """
        total = montant + self.FRAIS_FIXES
        if self.solde >= total:
            self.solde -= total
            print(f"Paiement de {montant:.2f}€ via PayPal (frais de {self.FRAIS_FIXES}€). Solde restant : {self.solde:.2f}€")
            return True
        else:
            print("Paiement refusé : solde insuffisant sur PayPal.")
            return False


class Crypto(MoyenDePaiement):
    """
    Classe représentant un paiement en cryptomonnaie avec des frais variables.
    """
    FRAIS_VARIABLES = 0.02  # 2% du montant
    
    def payer(self, montant: float) -> bool:
        """
        Effectue le paiement avec des frais de 2%.
        """
        frais = montant * self.FRAIS_VARIABLES
        total = montant + frais
        if self.solde >= total:
            self.solde -= total
            print(f"Paiement de {montant:.2f}€ en Crypto (frais de {frais:.2f}€). Solde restant : {self.solde:.2f}€")
            return True
        else:
            print("Paiement refusé : solde insuffisant en Crypto.")
            return False


# Exemple d'utilisation
if __name__ == "__main__":
    carte = CarteBancaire(100)
    paypal = Paypal(50)
    crypto = Crypto(200)
    
    carte.payer(30)
    paypal.payer(40)
    crypto.payer(100)
