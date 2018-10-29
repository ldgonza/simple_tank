import pygame
import os
from .engine.thing import Thing
from .engine.constants import *

class Tank(Thing):
    rotations = dict()
    rotations[UP] = pygame.image.load(os.path.dirname(__file__) + "/tank.gif")
    rotations[LEFT] = pygame.transform.rotate(rotations[UP], 90)
    rotations[DOWN] = pygame.transform.rotate(rotations[UP], 180)
    rotations[RIGHT] = pygame.transform.rotate(rotations[UP], 270)

    def __init__(self):
        Thing.__init__(self)
        self.rect = self.get_image().get_rect();
        
    def handle_out_of_bounds(self, screen_rect):
        self.rect = self.rect.clamp(screen_rect)

    def get_image(self):
        return Tank.rotations[self.direction]
