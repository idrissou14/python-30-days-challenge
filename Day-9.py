#trouver le mot le plus long dans un texte
phrase = input("entrer votre texte : ")
mots = phrase.split()
#mots le plus long
resultat = max(mots, key=len)
print(f"le mots le plus long est :", resultat)
