from os import name

from code.entity import Entity
from code.player import Player

class Level:
    def __init__(self, window, name, player_score: list[int]):
        self.window = window
        self.name = name
        self.player_score = player_score
        self.entities: list[Entity] = []
        player = Player(window, (100, 300))
        self.entities.append(player)
        
       
        
        
    def run(self):
        pass