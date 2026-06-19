import pygame
from code.const import KEYS, ENTITY_SPEED, SCREEN_WIDTH, SCREEN_HEIGHT
from code.entity import Entity

class Player(Entity):
    def __init__(self, window, position: tuple):
        super().__init__("Player", position)
        self.surf = pygame.transform.scale(self.surf, (60, 15)) # Redimensiona o sprite do jogador
        self.rect = self.surf.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40)) # Posiciona o jogador no centro da tela, 40px acima do fundo
        
        self.pos_x = float(self.rect.x)
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[KEYS['left']]:
            self.pos_x -= ENTITY_SPEED[self.name]
            
        if keys[KEYS['right']]:
            self.pos_x += ENTITY_SPEED[self.name]
            
        arena_width = 400
        arena_thickness = 10
        arena_margin = (SCREEN_WIDTH - arena_width) // 2

        # Calcula os limites da arena
        left_limit = arena_margin + arena_thickness
        right_limit = arena_margin + arena_width - arena_thickness - self.rect.width
        
        # Limita o movimento do jogador dentro da arena
        if self.pos_x < left_limit:
            self.pos_x = left_limit
        
        if self.pos_x > right_limit:
            self.pos_x = right_limit
            
        self.rect.x = int(self.pos_x)
        
    def draw(self):
        self.window.blit(self.surf, self.rect)
        