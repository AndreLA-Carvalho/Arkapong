import pygame
import sys

from code.const import SCREEN_HEIGHT, SCREEN_WIDTH, MENU_OPTIONS
from code.menu import Menu
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu_return = menu.run()
        
            if menu_return == MENU_OPTIONS[0]:
                player_score = 0 # Inicia a pontuação do jogador
                level = Level(self.window, "Level1", player_score) # Cria o nível 1
                level_return = level.run(player_score) # Roda o nível 1
                # if level_return:
                #     level = Level(self.window, "Level2", menu_return,player_score) # Cria o nível 2
                #     level_return = level.run(player_score) # Roda o nível 2
                    
                    # --- DESENVOLVIMENTO FUTURO ---
                    # if level_return:
                    #     score.save(menu_return, player_score)
            elif menu_return == MENU_OPTIONS[1]:
                # TODO: Implementar tela de recordes
                pass
            else:
                pygame.quit()
                sys.exit()