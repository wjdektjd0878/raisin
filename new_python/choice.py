# choice.py
import random

class Choice:
    def __init__(self, description, success_rate, points, story):
        self.description = description
        self.success_rate = success_rate
        self.points = points
        self.story = story

    def is_successful(self):
        return random.random() < self.success_rate
