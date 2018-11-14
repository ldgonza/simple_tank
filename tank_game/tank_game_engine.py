from .engine.game_engine import GameEngine
from .engine.event_ticker import EventTicker
from tank_game_event_checker import TankGameEventChecker
from tank import Tank
from bullet import Bullet
import random
from tank_game_categories import PLAYER, TANK, BULLET


class TankGameEngine(GameEngine):
    MAX_BULLETS = 3
    MAX_TANKS = 5

    def __init__(self, screen):
        GameEngine.__init__(self, screen, TankGameEventChecker())

        tank = self.add_tank((400, 300))
        tank.categories.append(PLAYER)

        ticker = EventTicker(1000, lambda: self.spawn_tank_controller())
        self.spawn_tank_ticker = ticker
        self.add_ticker(ticker)

    def bullet_count(self):
        return self.count(BULLET)

    def tank_count(self):
        return self.count(TANK)

    def count(self, category):
        count = 0
        for e in self.entities.all():
            if category in e.categories:
                count += 1

        return count

    def add_tank(self, pos):
        tank = Tank()
        tank.place_at(pos)
        tank.categories.append(TANK)
        self.entities.append(tank)
        return tank

    def can_shoot(self):
        not_at_bullet_cap = self.bullet_count() < TankGameEngine.MAX_BULLETS
        want_to_shoot = self.event_checker.shooting
        return want_to_shoot and not_at_bullet_cap

    def do_events(self, event_checker):
        GameEngine.do_events(self, event_checker)

        if event_checker.direction is None:
            self.get_player().stop()
        else:
            self.get_player().turn_to(event_checker.direction)

        if self.can_shoot():
            bullet = Bullet()
            bullet.categories.append(BULLET)
            bullet.place_at(self.get_player().rect.center)
            bullet.turn_to(self.get_player().direction)

            self.entities.append(bullet)

    def get_player(self):
        for e in self.entities.all():
            if PLAYER in e.categories:
                return e

    def get_random_pos(self):
        x = random.uniform(0, self.screen_rect.width)
        y = random.uniform(0, self.screen_rect.height)
        return (x, y)

    def get_tank(self, pos):
        tank = Tank()
        tank.categories.append(TANK)
        tank.place_at(pos)

    # spawn a tank somewhere
    # if there's no more than a set number of tanks already there
    def spawn_tank(self):
        if self.tank_count() < TankGameEngine.MAX_TANKS:
            self.add_tank(self.get_random_pos())

    def spawn_tank_controller(self):
        self.spawn_tank()
        self.spawn_tank_ticker.reset(random.uniform(500, 1500))
