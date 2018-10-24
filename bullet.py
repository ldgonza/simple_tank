import pygame
from thing import Thing
from constants import *

class Bullet(Thing):
    image = pygame.Surface((10,10))
    pygame.draw.circle(image, white, (5,5), 2)

    def handle_out_of_bounds(self, screen_rect):
        self.die()

    def get_image(self):
        return Bullet.image