from .engine.game_engine import GameEngine
from tank_game_event_checker import TankGameEventChecker
from tank import Tank
from bullet import Bullet

from tank_game_categories import *

class TankGameEngine(GameEngine):
    MAX_BULLETS = 3

    def __init__(self, screen):
        GameEngine.__init__(self, screen, TankGameEventChecker())

        tank = Tank()
        tank.categories.append(PLAYER)
        tank.place_at((400, 300))

        self.entities.append(tank)

    def bullet_count(self):
        count = 0
        for e in self.entities.all():
            if BULLET in e.categories: count += 1

        return count;

    def do_events(self, event_checker):
        GameEngine.do_events(self, event_checker)
        
        if event_checker.direction is None:
            self.get_player().stop()
        else:
            self.get_player().turn_to(event_checker.direction)

        if self.event_checker.shooting and self.bullet_count() < TankGameEngine.MAX_BULLETS:
            bullet = Bullet()
            bullet.categories.append(BULLET)
            bullet.place_at(self.get_player().rect.center)
            bullet.turn_to(self.get_player().direction)

            self.entities.append(bullet)

    def get_player(self):
        for e in self.entities.all():
            if PLAYER in e.categories: return e
        

    
