
# Générateur

"""
Un générateur est un type spécial d'itérateur. Au lieu de renvoyer tous ses résultats à la fois, un générateur produit 
les éléments à la demande. Cela permet de créer des itérateurs plus efficaces en termes de mémoire.

Un générateur se définit à l'aide d'une fonction contenant une ou plusieurs expressions yield plutôt qu'un return. 
Chaque fois que yield est exécuté, la fonction "retient" son état et renvoie la valeur courante, puis reprend là où elle 
s'était arrêtée la prochaine fois qu'elle est appelée."""

def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()

print(next(gen))  # Affiche 1
print(next(gen))  # Affiche 2
print(next(gen))  # Affiche 3

"""
Mémoire efficace : Un générateur ne stocke pas toute la séquence en mémoire, mais produit les éléments un par un à la demande.
Calcul paresseux : La génération des valeurs se fait à la demande (lorsqu'elles sont nécessaires), ce qui est efficace pour les grandes séries de données ou les flux infinis.
"""

# Expression génératrice
carres = (x**2 for x in range(5))

print(type(carres))

print(type(simple_generator()))