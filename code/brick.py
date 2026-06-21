import pygame

from code.entity import Entity
from code.const import ENTITY_HEALTH

class Brick(Entity):
    def __init__(self, window, position: tuple, brick_name: str, largura: int, altura: int):
        super().__init__(brick_name, position)
        self.window = window
        self.name = brick_name
        
        self.hp = ENTITY_HEALTH.get(brick_name, 1)
        
        self.surf = pygame.transform.scale(self.surf, (largura, altura))
        self.rect = self.surf.get_rect(topleft=position)
        
    def move(self):
        pass
