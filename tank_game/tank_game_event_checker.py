import pygame
from engine.constants import *

class TankGameEventChecker(object):
    def __init__(self):
        self.clear()
        
    def check(self):
        self.clear()
        self.check_pressed_keys()
        self.check_events()

    def clear(self):
        self.quit = False
        self.direction = None
        self.shooting = False
    

    def check_pressed_keys(self):
        keys=pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction = UP
        
        if keys[pygame.K_DOWN]:
            self.direction = DOWN

        if keys[pygame.K_LEFT]:
            self.direction = LEFT
        
        if keys[pygame.K_RIGHT]:
            self.direction = RIGHT

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.shooting = True

                if event.key == pygame.K_ESCAPE:
                    self.quit = True


        
