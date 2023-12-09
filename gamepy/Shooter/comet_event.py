import pygame
import random
from comet import Comet


""" create class comet"""
class CometFallEvent:

    # at the start -> create count
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 50
        self.game = game
        self.fall_mode = False

        # define a comets group
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        for i in range(1, random.randint(1, 10)):
            self.all_comets.add(Comet(self))
    
    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de cometes !")
            self.meteor_fall()
            self.fall_mode= True # active the event comet

    def update_bar(self, surface):

        # add percent to the bar
        self.add_percent()

        # level event black bar
        pygame.draw.rect(surface, (0, 0, 0), [
            0, # axe x
            surface.get_height() - 20, # axe y
            surface.get_width(), # length of bar
            10 # thickness
        ])

        # level event red bar
        pygame.draw.rect(surface, (187, 11, 11), [
            0, # axe x
            surface.get_height() - 20, # axe y
            (surface.get_width() / 100) * self.percent, # length of bar
            10 # thickness
        ])

