from game_engine import GameEngine
from tank_game_event_checker import TankGameEventChecker
from tank import Tank
from bullet import Bullet

from constants import *

class TankGameEngine(GameEngine):
    MAX_BULLETS = 1

    def __init__(self, screen):
        GameEngine.__init__(self, screen, TankGameEventChecker())

        self.tank = Tank()
        self.tank.place_at((400, 300))
        self.entities = [self.tank]
    
    #
    # Awful way to know how many bullets there are:
    # len(entities) - 1
    #
    def bullet_count(self):
        return len(self.entities) - 1

    def do_events(self, event_checker):
        GameEngine.do_events(self, event_checker)
        
        if event_checker.direction is None:
            self.tank.stop()
        else:
            self.tank.turn_to(event_checker.direction)

        if self.event_checker.shooting and self.bullet_count() < TankGameEngine.MAX_BULLETS:
            bullet = Bullet()
            bullet.place_at(self.tank.rect.center)
            bullet.turn_to(self.tank.direction)

            self.entities.append(bullet)
