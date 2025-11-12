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