#!/usr/bin/python3
import pygame
from projectile import Projectile
import animation

""" create player """
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 20
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        # inflict damage
        self.health -= amount

        # health <= 0
        if self.health <= 0:
            # left 1up
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        # draw life bar
        pygame.draw.rect(surface, (0, 0, 83), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def launch_projectile(self):
        # create new instance
        self.all_projectiles.add(Projectile(self))
        # start animation
        self.start_animation()
        # play sound
        """self.game.sound_manager.play('tir')"""


    def move_right(self):
        # move possible if there is no collision with monster
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
