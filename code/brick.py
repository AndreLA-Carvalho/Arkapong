import pygame

from code.const import C_WHITE, SCREEN_HEIGHT, SCREEN_WIDTH
from code.entity import Entity

class Brick(Entity):
    def __init__(self, window, position: tuple, brick_name: str, largura: int, altura: int):
        super().__init__(brick_name, position)
        self.window = window
        
        self.surf = pygame.transform.scale(self.surf, (largura, altura))
        self.rect = self.surf.get_rect(topleft=position)
        
    def move(self):
        pass
        
    # def draw(self):
    #     self.window.blit(self.surf, self.rect)
