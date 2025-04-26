#supprimer les doublons dans une list
ma_list = []
n = int(input("entrer le nombre d'element de votre liste : "))
for i in range(n):
    nombre = float(input("valeur => "))
    ma_list.append(nombre)

#chercher les doublons et les supprimer
ma_list_sans_doublon = []
for element in ma_list:
    if element not in ma_list_sans_doublon:
        ma_list_sans_doublon.append(element)

for element in ma_list_sans_doublon:
    print(element)