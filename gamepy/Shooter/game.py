#!/usr/bin/python3
import pygame
from sounds import SoundManager
from player import Player
from monster import Alien, Mummy
from comet_event import CometFallEvent


""" create class game """
class Game:

    def __init__(self):
        #define if game start
        self.is_playing = False
        # genere player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # define a monters group
        self.all_monsters = pygame.sprite.Group()
        # genere event
        self.comet_event = CometFallEvent(self)
        # sound manager
        self.sound_manager = SoundManager()
        # Score to 0
        self.font = pygame.font.Font("assets/myfont.ttf", 25)
        self.score = 0
        self.pressed = {}
        
        
    
    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # restart game
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        # play over sound
        self.sound_manager.play('game_over')
        
    def update(self, screen):
        # display score
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # add player image in my game
        screen.blit(self.player.image, self.player.rect)

        # refresh health bar
        self.player.update_health_bar(screen)

        # refresh event bar
        self.comet_event.update_bar(screen)

        # refresh player animation
        self.player.update_animation()

        # recup the player projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recup game monsters
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # recup game comets
        for comet in self.comet_event.all_comets:
            comet.fall()

        # add group of projectile images
        self.player.all_projectiles.draw(screen)

        #add group of comet images
        self.comet_event.all_comets.draw(screen)

        # add group of monster images
        self.all_monsters.draw(screen)

        # check if player go right or left
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width() :
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))