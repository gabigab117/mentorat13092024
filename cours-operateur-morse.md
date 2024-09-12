# Cours : L'opérateur morse (walrus) en Python

## Introduction

L'opérateur morse (walrus operator) a été introduit dans Python 3.8. Son nom vient de sa ressemblance avec les défenses
d'un morse `:=`. Il permet d'assigner une valeur à une variable dans le cadre d'une expression.

## Version Python

L'opérateur morse est disponible à partir de Python 3.8 (sorti en octobre 2019).

## Syntaxe

```python
(variable := expression)
```

## Utilisation et avantages

1. **Simplification des boucles while**
   Avant :
   ```python
   longueur = len(mot)
   while longueur > 5:
       print(f"Le mot '{mot}' est trop long ({longueur} caractères)")
       mot = input("Entrez un mot plus court : ")
       longueur = len(mot)
   ```
   Avec l'opérateur morse :
   ```python
   while (longueur := len(mot := input("Entrez un mot court : "))) > 5:
       print(f"Le mot '{mot}' est trop long ({longueur} caractères)")
   ```

2. **Utilisation dans les conditions**
   Avant :
   ```python
   nombre = int(input("Entrez un nombre : "))
   if nombre % 2 == 0:
       print(f"{nombre} est pair")
   else:
       print(f"{nombre} est impair")
   ```
   Avec l'opérateur morse :
   ```python
   if (nombre := int(input("Entrez un nombre : "))) % 2 == 0:
       print(f"{nombre} est pair")
   else:
       print(f"{nombre} est impair")
   ```

3. **Utilisation dans les listes en compréhension**
   Avant :
   ```python
   nombres = [1, 2, 3, 4, 5]
   carres_pairs = []
   for n in nombres:
       carre = n ** 2
       if carre % 2 == 0:
           carres_pairs.append(carre)
   ```
   Avec l'opérateur morse :
   ```python
   nombres = [1, 2, 3, 4, 5]
   carres_pairs = [carre for n in nombres if (carre := n ** 2) % 2 == 0]
   ```

## Avantages

- Réduit la répétition de code
- Permet d'assigner et d'utiliser une variable en une seule expression
- Peut rendre le code plus concis et lisible dans certains cas

## Précautions d'utilisation

- Utilisez l'opérateur morse avec modération pour maintenir la lisibilité du code
- Évitez de l'utiliser dans des expressions trop complexes
- N'oubliez pas les parenthèses pour contrôler la portée de l'affectation

