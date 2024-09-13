ma_liste = [1, 2, 3]  # Ceci est un itérable

# Ceci crée implicitement un itérateur et l'utilise
for element in ma_liste:
    print(element)

# C'est équivalent à :
iterateur = iter(ma_liste)  # Crée explicitement un itérateur
try:
    while True:
        element = next(iterateur)
        print(element)
except StopIteration:
    pass  # L'itérateur est épuisé
