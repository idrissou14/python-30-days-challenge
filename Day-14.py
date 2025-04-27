#lister tout les nombre premier jusqu'a 100
for i in range(1,100) :
    indice = 0
    for j in range(2,100):
        if i%j == 0 and j != i :
            indice += 1
            break
    if indice == 0 :
        print(f"nombre premier : {i} ")



