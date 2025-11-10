import pyautogui
import time

class whatsapp:
    def __init__(self):
        self.barre_de_recherche = 134, 82

whatsapp = whatsapp()

def ouvrir_whatsapp():
    with pyautogui.hold('win'):
        pyautogui.press('r')
    pyautogui.typewrite('chrome https;//web.whatsapp.com')
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('f11')


def rechercher_whatsapp(qui):
    pyautogui.click(whatsapp.barre_de_recherche)
    pyautogui.typewrite(qui)

ouvrir_whatsapp()
rechercher_whatsapp("")