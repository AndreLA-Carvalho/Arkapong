import pygame
import sys

from code.const import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_OPTIONS, ENTITY_HEALTH
from code.menu import Menu
from code.level import Level
from code.score import ScoreSystem


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self):
        score_system = ScoreSystem()
        while self.running:
            menu = Menu(self.window)
            menu_return = menu.run()
        
            if menu_return == MENU_OPTIONS[0]:
                player_score = [0] # Inicia a pontuação do jogador
                player_health = [ENTITY_HEALTH['Player']]
                level = Level(self.window, "Level1", player_score, player_health, 1) # Cria o nível 1
                level_return = level.run(player_score) # Roda o nível 1
                if level_return == True and player_health[0] > 0:
                     level = Level(self.window, "Level2", player_score, player_health, 2) # Cria o nível 2
                     level_return = level.run(player_score) # Roda o nível 2
                     if level_return:
                        score_system.show_input_nickname(self.window, player_score)
                    
            elif menu_return == MENU_OPTIONS[1]:
                score_system.show_top10_menu(self.window)
            else:
                pygame.quit()
                sys.exit()