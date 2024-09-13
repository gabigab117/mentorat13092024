# Itérateurs et Générateurs en Python

## Introduction

En Python, les itérateurs et les générateurs sont des outils puissants pour travailler avec des séquences de données de manière efficace. Comprendre leur fonctionnement et leurs différences est essentiel pour écrire du code Python performant et élégant.

## 1. Itérateurs avec `iter()` sur un itérable standard

Lorsque vous utilisez `iter()` sur un itérable standard (comme une liste, une chaîne de caractères ou un tuple), l'objet entier est déjà en mémoire.

### Exemple

```python
# Création d'une liste
fruits = ["pomme", "banane", "orange", "fraise", "kiwi"]

# Création d'un itérateur
it_fruits = iter(fruits)

# Parcours de l'itérateur
print(next(it_fruits))  # Affiche : pomme
print(next(it_fruits))  # Affiche : banane
print(next(it_fruits))  # Affiche : orange

# On peut aussi utiliser une boucle for
for fruit in it_fruits:
    print(fruit)  # Affiche : fraise, puis kiwi
```

**Note :** Même si on utilise un itérateur, toute la liste `fruits` est déjà en mémoire.

## 2. Générateurs

Un générateur produit des éléments à la demande, sans stocker toute la séquence en mémoire. C'est très utile pour traiter de grandes quantités de données ou des flux infinis.

### Exemple avec une fonction génératrice

```python
def carre_generator(max_num):
    for i in range(max_num):
        yield i ** 2

# Utilisation du générateur
for carre in carre_generator(5):
    print(carre)

# Affiche :
# 0
# 1
# 4
# 9
# 16
```

### Exemple avec une expression génératrice

```python
# Expression génératrice pour les carrés des nombres pairs
carres_pairs = (x**2 for x in range(10) if x % 2 == 0)

# Utilisation de l'expression génératrice
for carre in carres_pairs:
    print(carre)

# Affiche :
# 0
# 4
# 16
# 36
# 64
```

### Utilisation de `next()` et des boucles `for` avec les générateurs

Les générateurs peuvent être utilisés avec `next()` ou dans des boucles `for`. Voici les intérêts de chaque approche :

#### Utilisation de `next()`

```python
gen = carre_generator(5)
print(next(gen))  # Affiche : 0
print(next(gen))  # Affiche : 1
print(next(gen))  # Affiche : 4
```

**Intérêt :**
- Permet un contrôle précis sur l'itération
- Utile quand vous voulez traiter les éléments un par un de manière spécifique
- Pratique pour les tests ou le débogage

#### Utilisation d'une boucle `for`

```python
for carre in carre_generator(5):
    print(carre)
```

**Intérêt :**
- Plus simple et plus lisible pour parcourir tous les éléments
- Gère automatiquement l'arrêt de l'itération (pas besoin de gérer l'exception `StopIteration`)
- Idéal pour traiter tous les éléments de manière séquentielle

## 3. Classe d'itérateur personnalisé

Vous pouvez créer votre propre classe d'itérateur en définissant les méthodes `__iter__()` et `__next__()`. Cela permet un contrôle plus fin sur l'itération.

### Exemple

```python
class CompteurPairs:
    def __init__(self, limite):
        self.limite = limite
        self.valeur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.valeur >= self.limite:
            raise StopIteration
        valeur_actuelle = self.valeur
        self.valeur += 2
        return valeur_actuelle

# Utilisation de notre itérateur personnalisé
compteur = CompteurPairs(10)
for nombre in compteur:
    print(nombre)

# Affiche :
# 0
# 2
# 4
# 6
# 8
```

## Comparaison et conclusion

1. **Itérateur standard (`iter()`)** :
   - Tout est chargé en mémoire dès le début
   - Pratique pour les petites séquences

2. **Générateur** :
   - Génère les éléments à la demande
   - Économe en mémoire
   - Idéal pour de grandes séquences ou des flux de données
   - Peut être utilisé avec `next()` pour un contrôle précis ou avec des boucles `for` pour une itération simple

3. **Classe d'itérateur personnalisé** :
   - Offre un contrôle fin sur l'itération
   - Aussi efficace qu'un générateur en termes de mémoire
   - Plus complexe à écrire

Pour la plupart des cas, les générateurs sont le choix optimal : ils sont simples à écrire et efficaces en mémoire. Utilisez une classe d'itérateur personnalisée uniquement si vous avez besoin d'un contrôle très spécifique sur le processus d'itération.
