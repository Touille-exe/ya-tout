import time
import pyautogui


def ouvrir(site):
    with pyautogui.hold("win"):
        pyautogui.press("r")
    pyautogui.typewrite("chrome ")
    pyautogui.write(site)
    pyautogui.press("enter")
    pass

def ouvrir_app(quoi):
    with pyautogui.hold("win"):
        pyautogui.press("r")
    pyautogui.typewrite(quoi)
    pyautogui.press("enter")


def trouver_les_coo():
    time.sleep(10)
    x, y = pyautogui.position()
    print(f"Les coordonnées du curseur sont : x = {x}, y = {y}")
    pyautogui.click(774, 1047)
    menu()
    pass


def spam(personne,quoi,combien_de_messages):
    ouvrir("https;//web.whatsapp.com/")
    time.sleep(12)
    pyautogui.click(303, 191)
    pyautogui.typewrite(str(personne))
    time.sleep(1)
    pyautogui.click(338, 357)
    time.sleep(0.3)
    pyautogui.click(854, 980)
    for y in range(combien_de_messages):
        pyautogui.typewrite(quoi)
        pyautogui.press("enter")
        print(y)
        pass
    pass

def spam_2(quoi, combien_de_messages):
    time.sleep(10)
    for y in range(int(combien_de_messages)):
        pyautogui.typewrite(quoi)
        pyautogui.press("enter")
        print(y)
        pass
    pass

def menu():
    print("  1 = spam txt\n  2 = spam whatsapp\n  3 = coo du curseur\n  4 = Ouvrir une App\n  5 = Annuler")
    choix = str(input("1, 2, 3, 4 ou 5 ?"))

    if choix == "1":
        choix_2 = False
        if input("Ouvrir une app") == "oui" :
            print("  1 = Bloc-Note\n  2 = Google messages\n  3 = WhatsApp\n  4 = Annuler")
            choix_2 = input("1, 2, 3 ou 4 ?")


        quoui = input("Quel message ?")
        nombre = input("En combien de fois ?")

        if choix_2 == "1":
            ouvrir_app("notepad")
        elif choix_2 == "2":
            ouvrir("https;//messages.google.com/web/")
        elif choix_2 == "3":
            ouvrir("https;//web.whatsapp.com/")
        elif choix_2 == "4":
            return

        spam_2(quoui, nombre)

    elif choix == "2":
        perssonne = input("A qui ?")
        quoui = input("Quel message ?")
        nombre = int(input("En comnien de fois ?"))
        spam(perssonne, quoui, nombre)

    elif choix == "3":
        trouver_les_coo()

    elif choix == "4":
        print("  1 = Bloc-Note\n  2 = Google messages\n  3 = WhatsApp\n  4 = Annuler")
        choix_2 = input("1, 2, 3 ou 4 ?")

        if choix_2 == "1":
            ouvrir_app("notepad")
        elif choix_2 == "2":
            ouvrir("https;//messages.google.com/web/")
        elif choix_2 == "3":
            ouvrir("https;//web.whatsapp.com/")
        elif choix_2 == "4":
            return

menu()