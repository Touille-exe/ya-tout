import tkinter as tk
import time
import pyautogui

def init():
    global choix, texte, etape, personne, quoi, combien_de_messages
    choix = 0
    etape = 1
    texte = "Initialisation"
    menu()

def menu():
    global choix, texte, etape, Entree, Ecran, fenetre

    # Création de la fenêtre principale
    fenetre = tk.Tk()
    fenetre.title("Emmerdeur graphique")

    # Label pour afficher le texte des étapes
    Ecran = tk.Label(fenetre, text=texte)
    Ecran.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    # Fonction pour modifier le choix
    def mettre_choix(val):
        global choix
        choix = val

    # Boutons d'options
    bouton1 = tk.Button(fenetre, text="Bouton 1", command=lambda: mettre_choix(1))
    bouton1.grid(row=1, column=0)

    bouton2 = tk.Button(fenetre, text="Bouton 2", command=lambda: mettre_choix(2))
    bouton2.grid(row=1, column=1)

    bouton3 = tk.Button(fenetre, text="Bouton 3", command=lambda: mettre_choix(3))
    bouton3.grid(row=1, column=2)

    bouton4 = tk.Button(fenetre, text="Bouton 4", command=lambda: mettre_choix(4))
    bouton4.grid(row=1, column=3)

    # Champ de texte pour l'entrée utilisateur
    Entree = tk.Entry(fenetre)
    Entree.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

    bouton_valider = tk.Button(fenetre, text="Valider", command=lambda: mettre_choix(1))
    bouton_valider.grid(row=2, column=3)

    # Fonction pour mettre à jour l'affichage et gérer les étapes
    def mise_a_jour():
        global texte, etape, personne, quoi, combien_de_messages, choix

        if etape == 1:
            texte = "1 = Spam WhatsApp\n2 = Ouvrir une app\n(Autres choix non disponibles)"
            if choix == 1:
                choix = 0
                etape = 2
            elif choix == 2:
                choix = 0
                etape = 3

        elif etape == 2:
            texte = "À qui envoyer le message ?"
            if choix == 1:
                personne = Entree.get()
                choix = 0
                etape = 2.1

        elif etape == 2.1:
            texte = "Quel message envoyer ?"
            if choix == 1:
                quoi = Entree.get()
                choix = 0
                etape = 2.2

        elif etape == 2.2:
            texte = "Combien de messages ?"
            if choix == 1:
                combien_de_messages = Entree.get()
                choix = 0
                etape = 2.3
                spam(personne, quoi, combien_de_messages)
                fenetre.destroy()
                init()
                return

        elif etape == 3:
            texte = "Quelle app ?\n1 = WhatsApp\n2 = Bloc-Note\n3 = Google Messages\n4 = Spotify"
            if choix == 1:
                choix = 0
                etape = 3.1
                ouvrir("https;//web.whatsapp.com/")
                fenetre.destroy()
                init()
                return
            elif choix == 2:
                choix = 0
                etape = 3.1
                ouvrir_app("notepad")
                fenetre.destroy()
                init()
                return
            elif choix == 3:
                choix = 0
                etape = 3.1
                ouvrir("https;//messages.google.com/web/conversations")
                fenetre.destroy()
                init()
                return
            elif choix == 4:
                choix = 0
                etape = 3.1
                ouvrir_app("spotify")
                fenetre.destroy()
                init()
                return


        Ecran.config(text=texte)  # Mise à jour du texte
        fenetre.after(150, mise_a_jour)  # Rafraîchir toutes les 150 ms

    mise_a_jour()
    fenetre.mainloop()

def ouvrir(site):
    with pyautogui.hold("win"):
        pyautogui.press("r")
    pyautogui.typewrite("chrome ")
    pyautogui.write(site)
    pyautogui.press("enter")

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

def spam(personne, quoi, combien_de_messages):
    ouvrir("https;//web.whatsapp.com/")
    time.sleep(12)
    pyautogui.click(303, 191)
    pyautogui.typewrite(str(personne))
    time.sleep(1)
    pyautogui.click(338, 357)
    time.sleep(0.3)
    pyautogui.click(854, 980)
    for y in range(int(combien_de_messages)):
        pyautogui.typewrite(quoi)
        pyautogui.press("enter")
        print(y)

def spam_2(quoi, combien_de_messages):
    time.sleep(10)
    for y in range(int(combien_de_messages)):
        pyautogui.typewrite(quoi)
        pyautogui.press("enter")
        print(y)

# Lancer le programme
init()
