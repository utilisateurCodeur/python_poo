# Exercice : Gestion des Employés

# Objectif :
# - Utiliser l'héritage pour modéliser une hiérarchie d'employés.
#
# Étapes :
# 1. Créer une classe `Employe` avec les attributs `nom` et `salaire_base`.
# 2. Créer deux sous-classes `Developpeur` et `Manager` qui héritent de `Employe`.
#    - `Developpeur` aura un attribut `langage_programmation`.
#    - `Manager` aura un attribut `nombre_personnes_supervisees`.
# 3. Ajouter une méthode `calculer_salaire()` dans `Employe` et la redéfinir dans les sous-classes pour ajouter des bonus spécifiques.