from .engine.game_engine import GameEngine
from .engine.event_ticker import EventTicker
from .engine.constants import UP, DOWN, LEFT, RIGHT
from .engine.thing import Thing
from tank_game_event_checker import TankGameEventChecker
from tank import Tank
from bullet import Bullet
import random
from tank_game_categories import PLAYER, TANK, BULLET


class TankGameEngine(GameEngine):
    MAX_BULLETS = 3
    MAX_TANKS = 2

    def __init__(self, screen):
        GameEngine.__init__(self, screen, TankGameEventChecker())

        tank = self.add_tank((400, 300), add_tickers=False)
        tank.categories.append(PLAYER)

        self.add_ticker(EventTicker(
            1000,
            lambda ticker: self.spawn_tank_controller(ticker)))

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

    def add_tank(self, pos, add_tickers = True, speed = Thing.DEFAULT_SPEED):
        tank = Tank(speed)
        tank.place_at(pos)
        tank.categories.append(TANK)
        self.entities.append(tank)

        if add_tickers:
            self.add_ticker(EventTicker(
                0,
                lambda ticker: self.tank_move_controller(tank, ticker)))

            self.add_ticker(EventTicker(
                0,
                lambda ticker: self.tank_shoot_controller(tank, ticker)))

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

            pos = self.get_player().rect.center
            delta = 30

            if(self.get_player().direction == LEFT):
                pos = (pos[0] - delta, pos[1])

            if(self.get_player().direction == RIGHT):
                pos = (pos[0] + delta, pos[1])

            if(self.get_player().direction == UP):
                pos = (pos[0], pos[1] - delta)

            if(self.get_player().direction == DOWN):
                pos = (pos[0], pos[1] + delta)

            bullet.place_at(pos)
            bullet.turn_to(self.get_player().direction)

            self.entities.append(bullet)

        self.check_collisions()

        # Game over
        if self.get_player() is None:
            print("GAME OVER")
            self.alive = False

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
            self.add_tank(self.get_random_pos(), speed=Thing.DEFAULT_SPEED/3)

    def spawn_tank_controller(self, ticker):
        self.spawn_tank()
        ticker.reset(random.uniform(500, 1500))

    def tank_move_controller(self, tank, ticker):
        if not tank.is_alive():
            ticker.die()
        else:
            chance = random.uniform(0, 100)
            if(chance > 50):
                # Point to player
                viable_directions = list()
                player = self.get_player()

                if tank.pos[1] >= player.pos[1]:
                    viable_directions.append(UP)
                else:
                    viable_directions.append(DOWN)

                if tank.pos[0] >= player.pos[0]:
                    viable_directions.append(LEFT)
                else:
                    viable_directions.append(RIGHT)

                tank.turn_to(viable_directions[int(random.uniform(0, len(viable_directions)))])
            elif chance > 25:
                # Point somewhere random
                tank.turn_to(int(random.uniform(0, 3)))

            else:
                # Stop
                tank.stop()

            ticker.reset(random.uniform(0, 1000))

    def tank_shoot_controller(self, tank, ticker):
        if not tank.is_alive():
            ticker.die()
        else:
            pass

    def check_collisions(self):
        self.check_bullet_collisions()
        self.check_tank_collisions()

    def check_bullet_collisions(self):
        bullet_and_tank = self.detect_collisions(BULLET, TANK)

        for c in bullet_and_tank:
            bullet = c[0]
            tank = c[1]

            bullet.die()
            tank.die()

    def check_tank_collisions(self):
        tank_and_tank = self.detect_collisions(TANK, TANK)

        for c in tank_and_tank:
            tank1 = c[0]
            tank2 = c[1]
            tank1.die()
            tank2.die()
