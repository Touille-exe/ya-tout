import time
import pygame
import whatsapp

class Menu:
    def __init__(self):
        pygame.init()

        # Couleurs
        self.rouge_de_lecriture = (197, 15, 31)
        self.vert_de_lecriture = (21, 171, 12)
        self.gris_du_fond = (121, 125, 127)
        self.blanc = (255, 255, 255)
        self.noir = (0, 0, 0)
        self.rouge = (255, 0, 0)

        # Fenêtre et icône
        largeur, hauteur = 800, 600
        self.ecran = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption('Menu')
         #icone_image = pygame.image.load("image.png")
         #pygame.display.set_icon(icone_image)

        # Police d'écriture
        self.font_1 = pygame.font.SysFont("Comfortaa", 36)

        # Titres
        self.titre_menu = self.font_1.render("Menu :", True, self.blanc)



self = Menu()


boucle = True
while boucle:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boucle = False


    self.ecran.blit(self.titre_menu, (self.titre_menu.get_rect(center=(400, 30))))
    
    pygame.display.flip()

pygame.quit()