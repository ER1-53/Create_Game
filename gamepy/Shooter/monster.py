import pygame
import random
import animation

""" creater class Monster"""
class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0) :
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount
        

    def damage(self, amount):
        # inflict damage
        self.health -= amount

        # health <= 0
        if self.health <= 0:
            # reload monster
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health
            # add point to score
            self.game.add_score(self.loot_amount)
            
            # event bar is full, stop the monters
            if self.game.comet_event.is_full_loaded():
                # don't reload monster
                self.game.all_monsters.remove(self)
                # call comet fall
                self.game.comet_event.attempt_fall()
                
    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        # draw life bar
        pygame.draw.rect(surface, (0, 0, 83), [self.rect.x + 10, self.rect.y - 20, self.max_health, 2])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 10, self.rect.y - 20, self.health, 2])

    def forward(self):
        # Don't move if collision with players group
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # player damages
            self.game.player.damage(self.attack)

""" define mummy class"""
class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(6)
        self.set_loot_amount(20)

""" define alien class """
class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(3)
        self.set_loot_amount(50)
