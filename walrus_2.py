# a = 1
# b = 2
# print(a + b)


# Pourquoi cette expression ne fonctionne pas :
# print(c := 1 + d := 2)

# Raison 1 : Priorité des opérateurs
# L'opérateur := a une priorité plus faible que +
# Python interprète cela comme : (c := 1) + (d := 2)
# Ce qui n'est pas une expression valide


print((c := 1) + (d := 2))

print(f"Valeur de c : {c}, Valeur de d : {d}")

