''' 
Lab 12: Beginnings of Reinforcement Learning

Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / ".." / "..").resolve().absolute()))

from src.lab11.turn_combat import Combat
from src.lab11.pygame_combat import PyGameComputerCombatPlayer
from src.lab11.pygame_combat import PyGameHumanCombatPlayer
from src.lab11.pygame_combat import run_turn

def run_episode(player1, player2):
    currentGame = Combat()
    episode_list = []

    while not currentGame.gameOver:
        reward = run_turn(currentGame, player1, player2)
        health = tuple([player1.health, player2.health])
        result = (health, player1.weapon, reward)
        episode_list.append(result)
    
    return episode_list



# if __name__ == "__main__":
#     player1 = PyGameHumanCombatPlayer("Legolas")
#     player2 = PyGameComputerCombatPlayer("Computer")

#     print(run_episode(player1, player2))
