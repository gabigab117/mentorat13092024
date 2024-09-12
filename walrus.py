# Exemple 1 : Assignation dans une condition
# Avant
nombre = int(input("Entrez un nombre : "))
if nombre > 10:
    print(f"{nombre} est supérieur à 10")

# Après
if (nombre := int(input("Entrez un nombre : "))) > 10:
    print(f"{nombre} est supérieur à 10")


# Exemple 2 : Boucle while avec entrée utilisateur
# Avant
reponse = input("Entrez 'q' pour quitter : ")
while reponse != 'q':
    print("Vous avez entré :", reponse)
    reponse = input("Entrez 'q' pour quitter : ")

# Après
while (reponse := input("Entrez 'q' pour quitter : ")) != 'q':
    print("Vous avez entré :", reponse)


# Exemple 3 : Liste en compréhension avec calcul
# Avant
nombres = [1, 2, 3, 4, 5]
carres_pairs = []
for n in nombres:
    carre = n ** 2
    if carre % 2 == 0:
        carres_pairs.append(carre)

# Après
nombres = [1, 2, 3, 4, 5]
carres_pairs = [carre for n in nombres if (carre := n ** 2) % 2 == 0]
# compréhension sans walrus
carres_pairs_bis = [n ** 2 for n in nombres if (n ** 2) % 2 == 0]
print(carres_pairs_bis)
print(carres_pairs)


# Exemple 4 : Réutilisation d'un calcul
# Avant
import math

rayon = 5
surface = 4 * math.pi * rayon ** 2
volume = surface * rayon / 3

# Après

rayon = 5
volume = (surface := 4 * math.pi * rayon ** 2) * rayon / 3
