import pygame
from constants import UP, DOWN, LEFT, RIGHT


class Thing(object):
    DEFAULT_SPEED = 10  # pixels/frame

    def __init__(self):
        self.speeds = {}
        self.speeds[UP] = [0, -self._speed()]
        self.speeds[DOWN] = [0, self._speed()]
        self.speeds[LEFT] = [-self._speed(), 0]
        self.speeds[RIGHT] = [self._speed(), 0]

        self.alive = True
        self.direction = None
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.categories = list()

        self.place_at((0, 0))
        self.turn_to(UP)
        self.speed = None

    def _speed(self):
        return Thing.DEFAULT_SPEED

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
        self.speed = self.speeds[self.direction]

    def move(self):
        if self.speed is None:
            return

        self.pos = self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]
        self.rect.center = int(self.pos[0]), int(self.pos[1])

    def get_image(self):
        pass

    def handle_out_of_bounds(self, screen_rect):
        pass
