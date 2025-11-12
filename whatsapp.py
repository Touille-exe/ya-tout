import pyautogui
import time
import pyperclip

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
    pyperclip.copy(qui)
    pyautogui.click(whatsapp.barre_de_recherche)
    with pyautogui.hold('ctrl'):
        pyautogui.press('v')

#ouvrir_whatsapp()
#time.sleep(5)
#rechercher_whatsapp("")