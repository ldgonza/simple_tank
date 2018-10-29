# TODO: use an iterator to navigate it
# so that cleanup does not need to happen all the time
class ThingList:
    def __init__(self):
        self.things = list()

    def all(self):
        self.cleanup()
        return self.things

    def append(self, thing):
        self.things.append(thing)
    
    def cleanup(self):
        old_things = self.things[:]

        self.things = []
        for thing in old_things:
            if thing.is_alive(): self.things.append(thing)
