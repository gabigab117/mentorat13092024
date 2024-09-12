# Cours : Les décorateurs en Python

## Introduction

Les décorateurs sont un outil puissant en Python qui permet de modifier ou d'étendre le comportement de fonctions ou de
classes sans changer leur code source. Ils sont utilisés pour ajouter des fonctionnalités à du code existant de manière
élégante et réutilisable.

## Concept de base

Un décorateur est une fonction qui prend une autre fonction comme argument et renvoie une nouvelle fonction qui modifie
le comportement de la fonction originale.

## Syntaxe de base

```python
def mon_decorateur(func):
    def wrapper():
        print("Avant l'exécution de la fonction")
        func()
        print("Après l'exécution de la fonction")

    return wrapper


@mon_decorateur
def ma_fonction():
    print("Exécution de ma_fonction")


ma_fonction()
```

Explication :

1. `mon_decorateur` est une fonction qui prend une autre fonction `func` comme argument.
2. À l'intérieur, nous définissons une nouvelle fonction `wrapper` qui ajoute du comportement avant et après l'appel à
   `func`.
3. Le décorateur renvoie cette nouvelle fonction `wrapper`.
4. En utilisant `@mon_decorateur` au-dessus de `ma_fonction`, nous appliquons le décorateur.
5. Lorsque nous appelons `ma_fonction()`, c'est en réalité la version décorée (wrapper) qui est exécutée.

Résultat :

```
Avant l'exécution de la fonction
Exécution de ma_fonction
Après l'exécution de la fonction
```

## Décorateurs avec arguments de fonction

```python
def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Appel de la fonction {func.__name__} avec args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"La fonction {func.__name__} a retourné: {result}")
        return result

    return wrapper


@log_function_call
def addition(a, b):
    return a + b


resultat = addition(3, 5)
print(f"Résultat final: {resultat}")
```

Explication :

1. `log_function_call` est un décorateur qui enregistre les appels de fonction.
2. `wrapper` utilise `*args` et `**kwargs` pour accepter n'importe quel nombre d'arguments.
3. Le décorateur affiche les informations sur l'appel de la fonction, exécute la fonction, puis affiche le résultat.
4. `@log_function_call` est appliqué à la fonction `addition`.

Résultat :

```
Appel de la fonction addition avec args: (3, 5), kwargs: {}
La fonction addition a retourné: 8
Résultat final: 8
```

