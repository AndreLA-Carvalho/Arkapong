import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED

class Ball(Entity):
    def __init__(self, window, position: tuple):
        super().__init__("Ball", position)
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = position
        self.speed_x = ENTITY_SPEED['Ball']
        self.speed_y = ENTITY_SPEED['Ball']
        
    def move(self, wall_left, wall_right, wall_top):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.colliderect(wall_left): # Rebate para a direita se bater na parede esquerda
            self.speed_x *= -1
            self.rect.left = wall_left.rect.right # previne de grudar
        if self.rect.colliderect(wall_right): # Rebate para a esquerda se bater na parede direita
            self.speed_x *= -1
            self.rect.right = wall_right.rect.left # previne de grudar
        if self.rect.colliderect(wall_top): # Rebate para baixo se bater na parede superior
            self.speed_y *= -1
            self.rect.top = wall_top.rect.bottom # previne de grudar
        
    def draw(self):
        self.window.blit(self.surf, self.rect)