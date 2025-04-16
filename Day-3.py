import datetime


def calcul_age(annee):
    date = datetime.date.today()
    return  (date.year - annee)

def main():
    print("############## Calculer un age grace a une annee de naissance ##########")
    annee_nais = int(input("Veillez saisire votre annee de naissance : "))
    if datetime.date.today().year >= annee_nais :
        age = calcul_age(annee_nais)
        print(age)
    else:
        print("Veillez saisire une date valide")

if __name__ == "__main__" :
    main()