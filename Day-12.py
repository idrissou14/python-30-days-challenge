ma_list = []
n = int(input("entrer le nombre d'element de votre liste : "))

for i in range(n):
    nombre = float(input("valeur => "))
    ma_list.append(nombre)

#trier par odre croissant
min = 0
for i in range(n):
    for j in range(n):
        if ma_list[i] < ma_list[j] :
            min = ma_list[i]
            ma_list[i] = ma_list[j]
            ma_list[j] = min

#afficher la liste trier
for i in range(n):
    print(ma_list[i])