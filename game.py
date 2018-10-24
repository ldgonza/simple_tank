import sys, pygame
from tank_game_engine import TankGameEngine

pygame.display.init()

#
# Game 
#

size = width, height = 800, 600
screen_rect = pygame.Rect(0, 0, width, height)
screen = pygame.display.set_mode(size)

game = TankGameEngine(screen)
game.start()
