import random
import string

def generation_psw(longeur = 8):
    caractere = string.ascii_letters + string.digits
    psw = ''.join(random.choice(caractere) for _ in range(longeur))
    return  psw

def main():
    print("mot de passe", generation_psw())

if __name__ == "__main__" :
    main()