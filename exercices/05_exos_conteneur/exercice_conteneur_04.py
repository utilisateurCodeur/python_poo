# Exercice :
# Dans cette édition de la course de modules de Tatooine, la position des concurrents est stockée dans une liste.
# Chaque module (ou concurrent) est représenté par son nom dans cette liste.
# Les événements marquants de la course incluent les changements de position des modules suite à divers événements.
#
# Les événements sont les suivants :
# 1. Une panne moteur fait passer le premier module (premier élément de la liste) à la dernière position.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module C', 'Module A']
#
# 2. Le deuxième module (deuxième élément de la liste) accélère et prend la tête de la course.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module A', 'Module C']
#
# 3. Le dernier module (dernier élément de la liste) dépasse l'avant-dernier module pour prendre sa place.
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module A', 'Module C', 'Module B']
#
# 4. Un tir de blaster élimine le module en tête de la course (le premier élément de la liste).
#    Exemple : ['Module A', 'Module B', 'Module C'] -> ['Module B', 'Module C']
#
# 5. Un module qu'on pensait éliminé fait son grand retour et rejoint la dernière position de la course.
#    Exemple : ['Module B', 'Module C'] -> ['Module B', 'Module C', 'Module A']
#
# Créer les fonctions suivantes :
#
# 1. panne_moteur : modifie la liste de manière à ce que le premier module passe dernier, le deuxième passe premier,
#    et ainsi de suite. La fonction prendra en entrée une liste de modules et la modifiera.
#
# 2. passe_en_tete : modifie la liste de manière à ce que le premier module passe deuxième et le deuxième module passe premier.
#    La fonction prendra également une liste et changera les positions des deux premiers éléments.
#
# 3. sauve_honneur : modifie la liste pour que le dernier module prenne la place de l'avant-dernier et l'avant-dernier passe dernier.
#    Par exemple, si la liste est ['Module A', 'Module B', 'Module C'], elle deviendra ['Module A', 'Module C', 'Module B'].
#
# 4. tir_blaster : enlève le premier module de la liste (le module en tête de la course).
#    Par exemple, si la liste est ['Module A', 'Module B', 'Module C'], elle deviendra ['Module B', 'Module C'].
#
# 5. retour_inattendu : ajoute un module (qui pourrait être un module "éliminé") à la fin de la liste.
#    Exemple : si la liste est ['Module B', 'Module C'], elle deviendra ['Module B', 'Module C', 'Module A'].
