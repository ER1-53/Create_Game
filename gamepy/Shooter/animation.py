import pygame

""" create class animation"""
class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #define a method for activate animation
    def start_animation(self):
        self.animation = True

    # method for anime sprite
    def animate(self, loop=False):

        if self.animation:
            # go to the next image
            self.current_image += 1

            # check if is the last image
            if self.current_image >= len(self.images):
                # restart animation
                self.current_image = 0

                #check if animation isn't to loop
                if loop is False:
                    # desactivate animation
                    self.animation = False

            # change image by next
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

# define function for upload animation
def load_animation_images(sprite_name):
    # upload sprite images
    images = []
    # recup the path of the sprite
    path = f"assets/{sprite_name}/{sprite_name}"


    # loop all image 
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        pygame.image.load(image_path)
        images.append(pygame.image.load(image_path))
    
    return images

# define à dict of images
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}