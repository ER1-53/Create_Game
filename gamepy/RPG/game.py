import pygame
import pytmx
import pyscroll

from player import player


class Game:

    def __init__(self):

        # creer la fenetre du jeu

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Fire Power")

        # charger la carte en format tmx

        tmx_data = pytmx.util_pygame.load_pygame('/home/lardo/gamepy/map/texture_map/firepower.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 2

        # generer un joueur
        self.player = player()

        # dessiner le groupe de calques

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)

    def run(self):

        # boucle du jeu
        running = True

        while running:

            self.group.draw(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.QUIT()

