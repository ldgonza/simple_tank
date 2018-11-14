class EventTicker(object):
    def __init__(self, target_ms, callback):
        self.callback = callback
        self.reset(target_ms)

    def reset(self, target_ms):
        self.target_ms = target_ms
        self.elapsed_ms = 0

    def tick(self, ms):
        self.elapsed_ms += ms
        if self.elapsed_ms >= self.target_ms:
            self.callback()
            self.reset(self.target_ms)
