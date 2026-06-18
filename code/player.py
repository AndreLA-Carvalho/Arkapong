import pygame
from const import KEYS

class Player:
    def __init__(self, window, position: tuple):
        super().__init__()
        
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[KEYS['left']]:
            self.rect.x -= self.speed
        if keys[KEYS['right']]:
            self.rect.x += self.speed
        if keys[KEYS['up']]:
            self.rect.y -= self.speed
        if keys[KEYS['down']]:
            self.rect.y += self.speed
        
    def draw(self):
        self.window.blit(self.image, self.rect)
        