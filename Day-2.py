def celcus_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celcus(f):
    return (f - 32)*5/9

def main():
    print("convertisseur de temperature : veillez faire un choix")
    print("1 : celcus -> Fahrenheit")
    print("2 : Fahrenheit -> celcus")

    choix = input("entrer votre choix : 1 ou 2")

    if choix == "1" :
        celcus = float(input("entrer la temperature en celcus "))
        fahrenheit = celcus_to_fahrenheit(celcus)
        print(f"temperature en Fahrenheit",fahrenheit)

    if choix == "2" :
        fahrenheit = float(input("entrer la temperature en Fahrenheit"))
        celcus = fahrenheit_to_celcus(fahrenheit)
        print(f"temperature en celcus",celcus)

    else:
        print("choix non valide")

if  __name__ == "__main__":
    main()
