import pygame
import random


"""create the comet"""

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #define image comet
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 5)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        # play sound
        self.comet_event.game.sound_manager.play('meteorite')

        # check there are not comets
        if len(self.comet_event.all_comets) == 0:
            # event bar to zero
            self.comet_event.reset_percent()
            # display monsters
            self.comet_event.game.start()
             

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 500:
            self.remove()

            # if there are not more comet
            if len(self.comet_event.all_comets) == 0:
                 print("event finish")
                 # refresh event bar
                 self.comet_event.reset_percent()
                 self.comet_event.fall_mode = False
        
        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_players
            ):
                print("joueur touché")
                # left comet
                self.remove()
                # damage player
                self.comet_event.game.player.damage(20)

            
