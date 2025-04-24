from itertools import chain

mot = input("veillez saisire votre mot : ")
riverse = mot[::-1]
if mot == riverse :
    print("le mot est un palindrome")
else:
    print("le mot n'est pas un palindrome")