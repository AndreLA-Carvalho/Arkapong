import pygame

from code.const import ENTITY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if name == 'menuBg1':
            original_width, original_height = self.surf.get_size()
            scale_factor = 0.25  # Reduce to 25% of original size
            new_width = int(original_width * scale_factor)
            new_height = int(original_height * scale_factor)
            self.surf = pygame.transform.scale(self.surf, (new_width, new_height))
            self.rect.width = new_width
            self.rect.height = new_height
            self.rect.x = SCREEN_WIDTH - new_width - 40
            self.rect.y = 40
            
        else:
            self.surf = pygame.transform.scale(self.surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.rect = self.surf.get_rect(topleft=position)
        
    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
            
        if self.rect.right < 0: 
            self.rect.left = SCREEN_WIDTH - 2
        