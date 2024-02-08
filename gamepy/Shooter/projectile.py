#!/usr/bin/python3
import pygame

""" create class projectile """
class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 6
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origine_image = self.image
        self.angle = 0

    def rotate(self):
        # rotattion of the projectile
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)


    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        # check if projectile is a collision with monsters
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # remove projectile
            self.remove()
            # inflict damages
            monster.damage(self.player.attack)

        # check if projectile left screen
        if self.rect.x > 1080:
            #delete projectiles
            self.remove()

    def remove(self):
        self.player.all_projectiles.remove(self)


