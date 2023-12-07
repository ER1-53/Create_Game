import pygame

class player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.spriteSheet = pygame.image.load('/home/lardo/gamepy/map/Knight/KnightRun_strip.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect(0, 0)

    def get_image(self, x, y):
        image = pygame.surface([32, 32])
        image.blit(self.spriteSheet, (0, 0), (x, y, 32, 32))
        return image