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



# Un Générateur est à la fois un itérable et un itérateur
def generateur_simple():
    yield 1
    yield 2
    yield 3

# Utilisation comme un itérable
for nombre in generateur_simple():
    print(nombre)

# Utilisation comme un itérateur
gen = generateur_simple()
print(next(gen))  # Affiche 1
print(next(gen))  # Affiche 2
print("autre action")
print(next(gen))  # Affiche 3