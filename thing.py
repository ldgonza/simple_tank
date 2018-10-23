import pygame
from constants import *

class Thing(object):
    speeds = dict()
    speeds[UP] = [0, -1]
    speeds[DOWN] = [0, 1]
    speeds[LEFT] = [-1, 0]
    speeds[RIGHT] = [1, 0]

    def __init__(self):
        self.alive = True
        self.rect = pygame.Rect(0, 0, 0, 0)

        self.speed = None
        self.direction = None
        self.turn_to(UP)

    def place_at(self, center):
        self.rect.center = center
        
    def die(self):
        self.alive = False

    def is_alive(self):
        return self.alive

    def stop(self):
        self.speed = [0, 0]
        
    def turn_to(self, direction):
        self.direction = direction
        self.speed = Thing.speeds[self.direction]
    
    def move(self):
        self.rect = self.rect.move(self.speed)

    def get_image(self):
        pass
        
    def handle_out_of_bounds(self, screen_rect):
        pass
