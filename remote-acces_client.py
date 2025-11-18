import socket
import pygame

class remote_access:
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
        # icone_image = pygame.image.load("image.png")
        # pygame.display.set_icon(icone_image)

        # Police d'écriture
        self.font_1 = pygame.font.SysFont("Comfortaa", 36)

        # Textes
        self.titre_menu = self.font_1.render("Menu :", True, self.blanc)

        # Variables
        self.latence = False

        # Socket
        self.remoteaccess = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



remote_access = remote_access()

def connecttoremoteaccess(host, port, user):
    try:
        remote_access.remoteaccess.connect((host, port))
        print(f"Connecté au serveur {host}:{port} !")
    except ConnectionRefusedError:
        print("Erreur 404 : server not found")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

def boucle():
    boucle = True
    while boucle:
        pygame.display.flip()

