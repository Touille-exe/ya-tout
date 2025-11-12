import whatsapp
import time
import sdl2
import sdl2.ext

class Menu:
    def __init__(self):
        # interface graphique
        sdl2.ext.init()
        self.fenetre = sdl2.ext.Window("L'app de touille", size=(800, 600))
        self.fenetre.show()
        self.rendu = sdl2.ext.Renderer(self.fenetre)
        self.gestionnaire_police = sdl2.ext.FontManager(font_path="C:\\Windows\\Fonts\\arial.ttf", size=24)

    def

self = Menu()

self.fenetre.show()

boucle = True
while boucle:
    for evenement in sdl2.ext.get_events():
        if evenement.type == sdl2.SDL_QUIT:
            print("quit")
            boucle = False


    self.rendu.present()


sdl2.ext.quit()