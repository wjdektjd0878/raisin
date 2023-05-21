# character.py
class Character:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points

    def can_unlock_choice(self, choice):
        return self.points >= choice.points
