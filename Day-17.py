from datetime import datetime  # ✅ Pas _datetime, juste datetime

print("########### Bienvenue sur mon journal de bord ###########")
entries = []  # ✅ Évite d’utiliser 'list' comme nom de variable
item = ""

print("Écrivez <fin> pour arrêter la saisie.")

while True:
    item = input("Entrer votre élément : ").strip()
    if item.lower() == "fin":  # ✅ Pour accepter "fin", "Fin", "FIN", etc.
        break
    entries.append(item)

# Ouverture du fichier en mode ajout
with open("fichier.txt", "a", encoding="utf-8") as fichier:
    fichier.write("\n\n########## Entrée du " + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + " ##########\n")
    for element in entries:
        fichier.write("- " + element + "\n")

print("Éléments enregistrés avec succès. Veuillez consulter votre fichier.")
