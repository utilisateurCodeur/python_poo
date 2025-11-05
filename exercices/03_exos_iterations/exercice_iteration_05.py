# Exercice :
# Réaliser un programme permettant à l'utilisateur d'entrer comme données :
# - Une population initiale.
# - Un taux d'accroissement.
# - Une population visée.
# Ce programme permettra à l'utilisateur de savoir en combien de temps la population visée sera atteinte.

# Demande de saisie des données
population_initiale = int(input("Entrez la population initiale : "))
taux_accroissement = float(input("Entrez le taux d'accroissement annuel (en pourcentage) : ")) / 100
population_visee = int(input("Entrez la population visée : "))

# Initialisation
population = population_initiale
annees = 0

# Boucle jusqu'à atteindre ou dépasser la population visée
while population < population_visee:
    population *= (1 + taux_accroissement)  # Applique le taux de croissance
    annees += 1  # Incrémente le nombre d'années

# Affichage du résultat
print(f"La population atteindra {population_visee} en {annees} ans.")
