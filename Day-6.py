#calculer la somme et la moyenne d'une liste de nombre

ma_list = []
n = int(input("Entrer le nombre d'element de votre liste : "))
cpt = 0
for i in range(n):
    nombre = float(input("==>"))
    ma_list.append(nombre)
    cpt += 1

#calcule de la somme
somme = 0
for i in range(n):
    somme += ma_list[i]

print("la somme est :", somme)

#la moyenne
moy = somme/cpt
print("la moyenne est : ", moy)