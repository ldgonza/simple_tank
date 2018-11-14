import pygame
from thing_list import ThingList


class GameEngine(object):
    DEFAULT_FRAMES_PER_SECOND = 60

    def __init__(self, screen, event_checker):
        self.tickers = list()
        self.event_checker = event_checker
        self.entities = ThingList()
        self.alive = False

        self.screen = screen
        self.screen_rect = screen.get_rect()

    def start(self):
        self._do_loop()

    def add_ticker(self, ticker):
        self.tickers.append(ticker)

    def _do_loop(self):
        self.alive = True

        clock = pygame.time.Clock()
        while self.alive:
            ms = clock.tick(self.get_target_frames_per_second())
            self._do_frame(ms)

    # Do one frame
    def _do_frame(self, ms):
        self.event_checker.check()
        self.do_events(self.event_checker)

        # An event might want to trigger the end of the loop
        if not self.alive:
            return

        self.do_tickers(ms)
        self.do_update()
        self.do_draw()

    def do_tickers(self, ms):
        for ticker in self.tickers:
            ticker.tick(ms)

    def do_events(self, event_checker):
        if self.event_checker.quit:
            self.alive = False

    def do_update(self):
        # Move
        for e in self.entities.all():
            e.move()

        # Dispatch events to entities
        # like collisions or out of bounds
        for e in self.entities.all():
            if not self.screen_rect.contains(e.rect):
                e.handle_out_of_bounds(self.screen_rect)

    def do_draw(self):
        self.screen.fill((0, 0, 0))

        for e in self.entities.all():
            self.screen.blit(e.get_image(), e.rect)

        pygame.display.flip()

    def get_target_frames_per_second(self):
        return self.DEFAULT_FRAMES_PER_SECOND

    def entities_by_category(self, cat):
        result = list()
        for e in self.entities.all():
            if cat in e.categories:
                result.append(e)

        return result

    # Return entities that collide
    # in pair (e1, e2)
    # where e1 belongs to cat1 and e2 belongs to cat2
    def detect_collisions(self, cat1, cat2):
        collisions = list()
        for e1 in self.entities_by_category(cat1):
            for e2 in self.entities_by_category(cat2):
                if e1 is e2:
                    continue

                if e1.rect.colliderect(e2.rect):
                    collisions.append((e1, e2))

        return collisions
