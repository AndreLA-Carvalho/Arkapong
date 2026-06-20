import pygame
from code.entity import Entity
from code.const import ENTITY_SPEED, KEYS

class Ball(Entity):
    def __init__(self, window, position: tuple):
        super().__init__('brick1', position)
        self.window = window
        
        self.surf = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.circle(self.surf, (255, 255, 255), (6, 6), 5)
        self.rect = self.surf.get_rect(center=position)
        
        self.pos_x = float(self.rect.x)
        self.pos_y = float(self.rect.y)
        
        self.speed_x = 0
        self.speed_y = 0
        self.active = False # A bola fica travada no jogador até o usuário pressionar espaço
        
        self.sound_wall = pygame.mixer.Sound("asset/wallBounce.mp3")
        self.sound_player = pygame.mixer.Sound("asset/playerBounce.mp3")
        self.sound_wall.set_volume(0.4)
        self.sound_player.set_volume(0.4)
        
    def move(self, wall_left, wall_right, wall_top, player_rect):
        keys = pygame.key.get_pressed()

        if not self.active:
            self.rect.centerx = player_rect.centerx
            self.rect.bottom = player_rect.top
            self.pos_x = float(self.rect.x)
            self.pos_y = float(self.rect.y)

            if keys[KEYS["space"]]:
                self.active = True
                self.speed_x = ENTITY_SPEED["Ball"]
                self.speed_y = -ENTITY_SPEED["Ball"]
        else:
            
            self.pos_x += self.speed_x
            self.pos_y += self.speed_y
            
            self.rect.x = int(self.pos_x)
            self.rect.y = int(self.pos_y)
        
            if self.rect.colliderect(wall_left): # Rebate para a direita se bater na parede esquerda
                self.speed_x *= -1
                self.pos_x = float(wall_left.right)
                self.rect.left = wall_left.right # previne de grudar
                self.sound_wall.play()
                
            if self.rect.colliderect(wall_right): # Rebate para a esquerda se bater na parede direita
                self.speed_x *= -1
                self.pos_x = float(wall_right.left - 12)
                self.rect.right = wall_right.left # previne de grudar
                self.sound_wall.play()
                
            if self.rect.colliderect(wall_top): # Rebate para baixo se bater na parede superior
                self.speed_y *= -1
                self.pos_y = float(wall_top.bottom)
                self.rect.top = wall_top.bottom # previne de grudar
                self.sound_wall.play()
                
            if self.rect.colliderect(player_rect): # Rebate para cima se bater no jogador
                self.speed_y *= -1
                self.pos_y = float(player_rect.top - 12)
                self.rect.bottom = player_rect.top # previne de grudar
                self.sound_player.play()
        
    def draw(self):
        self.window.blit(self.surf, self.rect)
        