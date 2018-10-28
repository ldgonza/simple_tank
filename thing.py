import pygame
from constants import *

class Thing(object):
    speeds = dict()

    # Speeds are pixels/frame
    RATE = 10
    speeds[UP] = [0, -RATE]
    speeds[DOWN] = [0, RATE]
    speeds[LEFT] = [-RATE, 0]
    speeds[RIGHT] = [RATE, 0]

    def __init__(self):
        self.alive = True
        self.speed = None
        self.direction = None
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.categories = list()
        
        self.place_at((0, 0))
        self.turn_to(UP)

    def place_at(self, center):
        self.rect.center = center
        self.pos = float(self.rect.center[0]), float(self.rect.center[1])
        
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
        self.pos = self.pos[0] +  self.speed[0], self.pos[1] + self.speed[1]
        self.rect.center = int(self.pos[0]), int(self.pos[1])
        
    def get_image(self):
        pass
        
    def handle_out_of_bounds(self, screen_rect):
        pass
