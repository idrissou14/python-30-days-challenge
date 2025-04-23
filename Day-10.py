def compter_voyelles(mot):
    voyelles = "aeiouyAEIOUY"
    compteur = 0
    for lettre in mot:
        if lettre in voyelles:
            compteur += 1
    return compteur

# Exemple d'utilisation
mot = "ordinateur"
print(f"Nombre de voyelles dans '{mot}':", compter_voyelles(mot))
