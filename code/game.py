import pygame
import sys

from code.const import SCREEN_HEIGHT, SCREEN_WIDTH
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True

    def run(self):
        while self.running:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return == 1:
                break
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()