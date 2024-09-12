# Exercice : Le Décorateur Magique

# Objectif :
# Créer un décorateur simple appelé 'magic_words' qui ajoute des mots magiques
# au début et à la fin d'une phrase retournée par une fonction.

# Instructions :
# 1. Créez le décorateur 'magic_words'.
# 2. Le décorateur doit :
#    - Ajouter "Abracadabra" au début de la phrase
#    - Ajouter "Alohomora!" à la fin de la phrase
# 3. Appliquez ce décorateur à une fonction simple qui retourne une phrase.


def magic_words(func):
    def wrapper(*args, **kwargs):
        resultat = func(*args, **kwargs)
        return f"Abracadabra {resultat} Alohomora!"
    return wrapper


def dire_bonjour(nom):
    return f"Bonjour {nom}"

print(dire_bonjour("Patrick"))
# Résultat attendu :
# print(dire_bonjour("Patrick"))
# Devrait afficher : "Abracadabra Bonjour Patrick Alohomora!"
