import random
from lab11.turn_combat import CombatPlayer

print("draft")
class PyGameAIPlayer:
    def __init__(self):
        self.money = 100
        self.health = 100
    def selectAction(self):
        return ord(str(random.randint(0,9)))


""" Create PyGameAICombatPlayer class here"""

class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)
        self.money = 100
        self.health = 100

    def weaponSelectingStrategy(self):
        return random.randint(0, 2)
