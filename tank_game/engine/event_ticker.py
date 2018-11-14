class EventTicker(object):
    def __initialize__(self, target_ms, callback):
        self.target_ms = target_ms
        self.callback = callback

        self.reset()

    def reset(self):
        self.elapsed_ms = 0

    def tick(self, ms):
        self.elapsed_ms += ms
        if self.elapsed_ms >= self.target_ms:
            self.callback()
            self.reset()
