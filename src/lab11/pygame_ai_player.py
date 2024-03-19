import random
from turn_combat import CombatPlayer


class PyGameAIPlayer:
    def selectAction(self, state):
        return ord(str(random.randint(0,9)))


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer(CombatPlayer):
    def __init__(self, name):
        super().__init__(name)

    def weaponSelectingStrategy(self):
        self.weapon = random.randint(0, 2)
        return self.weapon
