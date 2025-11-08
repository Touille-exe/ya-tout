import time

def calc():
    choix = str(input("  Addition = 1\n  Soustraction = 2\n  Multiplication = 3\n  Division = 4\n  Quitter = 5\n\n >>"))
    if choix == "1":
        time.sleep(0.2)
        premierchiffre = int(input("premier chiffre\n\n >>"))
        time.sleep(0.2)
        dexiemechifre = int(input("dexieme chifre\n\n >>"))
        time.sleep(0.2)
        print(premierchiffre + dexiemechifre)
        calc()
    elif choix == "2":
        time.sleep(0.2)
        premierchiffre = int(input("premier chiffre\n\n >>"))
        time.sleep(0.2)
        dexiemechifre = int(input("dexieme chifre\n\n >>"))
        time.sleep(0.2)
        print(premierchiffre - dexiemechifre)
        calc()
    elif choix == "3":
        time.sleep(0.2)
        premierchiffre = int(input("premier chiffre\n\n >>"))
        time.sleep(0.2)
        dexiemechifre = int(input("dexieme chifre\n\n >>"))
        time.sleep(0.2)
        print(premierchiffre * dexiemechifre)
        calc()
    elif choix == "4":
        time.sleep(0.2)
        premierchiffre = int(input("premier chiffre\n\n >>"))
        time.sleep(0.2)
        dexiemechifre = int(input("dexieme chifre\n\n >>"))
        time.sleep(0.2)
        print(premierchiffre / dexiemechifre)
        calc()


calc()