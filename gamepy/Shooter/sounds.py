import pygame
pygame.mixer.init()

class SoundManager:

    def __init__(self):
        self.sounds = {
            'ci': pygame.mixer.Sound('assets/sounds/ci.ogg'),
            'game_over': pygame.mixer.Sound("assets/sounds/game_over.ogg"),
            'meteorite': pygame.mixer.Sound("assets/sounds/meteorite.ogg"),
            'tir': pygame.mixer.Sound("assets/sounds/tir.ogg"),
        }

    def play(self, name):
        self.sounds[name].play()
