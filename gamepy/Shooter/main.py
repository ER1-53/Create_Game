#!/usr/bin/python3
"""" default fo sounds"""
import pygame
from game import Game
pygame.init()


# define a clock
clock = pygame.time.Clock()
FPS = 80

# Dispay the screen
pygame.display.set_caption('UniverSound')
screen = pygame.display.set_mode((1080, 720))

# import the background
background = pygame.image.load('assets/bg.jpg')

# import banner
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = screen.get_width() / 4

# button start
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = screen.get_width() / 3.33
play_button_rect.y = screen.get_height() / 2

# upload game
game = Game()


running = True

# loop while running condition is true
while running:

    # add background in my game
    screen.blit(background, (0, -200))


    #check if game is starting
    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # update the screen
    pygame.display.flip()

    # if player left game
    for event in pygame.event.get():
        # the event is close window
        if event.type == pygame.QUIT:
            print("Game over")
            running = False
            pygame.quit()
        
        # detect if the player drops a keyboard key
        elif event.type == pygame.KEYDOWN:
           game.pressed[event.key] = True

           # detect if key_space is used for launch projectile
           if event.key == pygame.K_SPACE:
               game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # check if you clic in the button
            if play_button_rect.collidepoint(event.pos):
                game.start()
                # play sound
                game.sound_manager.play('ci')

    # fix FPS on clock
    clock.tick(FPS)
