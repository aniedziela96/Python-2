import random


class Client:
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.steps = random.randrange(1, 9, 2)

    def paint(self):
        self.steps -= 1

    def is_done(self):
        return self.steps <= 0

    def get_steps(self):
        return self.steps
    
    def waiting_time(self, current_time):
        return current_time - self.timestamp