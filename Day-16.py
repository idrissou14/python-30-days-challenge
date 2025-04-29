#ecrire un liste de course dans un fichier
items = []
i = 0
course = ""
print("ecrire <fin> pour arreter la liste de course :")
while course != "fin":
    course = input("entrer l'element a enregistrer : ")
    items.append(course)
    i += 1

fichier = open("fichier.txt", "a")
for item in items:
    fichier.write(item + "\n")

fichier.close()
print("liste de courses enregistrer, veillez consulter votre fichier.")
