import pygame

from code.const import C_ORANGE, C_WHITE, C_DARK_BLUE, SCREEN_HEIGHT, SCREEN_WIDTH
from code.entity import Entity
from code.player import Player
from code.ball import Ball
from code.brick import Brick

class Level:
    def __init__(self, window: pygame.Surface, name: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.player_score = player_score
        self.entities: list[Entity] = []
        player = Player(window, (SCREEN_WIDTH // 2, 530)) # Posiciona o jogador no centro da tela
        self.entities.append(player)
        self.ball = Ball(window, (SCREEN_WIDTH // 2, 510)) # Posiciona a bola no centro da tela, acima do jogador
        self.entities.append(self.ball)
        
        arena_width = 400
        arena_thickness = 10
        arena_margin = (SCREEN_WIDTH - arena_width) // 2
        
        self.wall_left = pygame.Rect(arena_margin, 0, arena_thickness, SCREEN_HEIGHT) 
        self.wall_right = pygame.Rect(arena_margin + arena_width - arena_thickness, 0, arena_thickness, SCREEN_HEIGHT)
        self.wall_top = pygame.Rect(arena_margin, 0, arena_width, arena_thickness)
        
        # Mapa do level
        level_map = [
            "1111111111",
            "1113113111",  
            "1113113111",
            "1111111111",
            "1311111131",  
            "1133333311",  
            "2222222222"
        ]
        
        # Configuração das tijolos
        brick_width = 34
        brick_height = 20
        brick_spacing = 4
        
        # Posição inicial dos tijolos
        start_x = arena_margin + arena_thickness + 2
        start_y = 60
        
        for row_index, row in enumerate(level_map):
            for col_index in range(len(row)):
                cell = row[col_index]
                if cell == '.':
                    continue
                x = start_x + col_index * (brick_width + brick_spacing)
                y = start_y + row_index * (brick_height + brick_spacing)
        
                if cell == '1':
                    name_brick = "brick1"
                elif cell == '2':
                    name_brick = "brick2"
                elif cell == '3':
                    name_brick = "brick3"
                    
                brick = Brick(self.window, (x,y), name_brick, brick_width, brick_height)
                self.entities.append(brick)
        
        self.sound_brick = pygame.mixer.Sound("asset/brickHit.mp3")
        self.sound_brick.set_volume(1)
                
    def run(self, player_score: int):
        pygame.mixer_music.load(f"asset/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        
        while True:
            self.window.fill(C_DARK_BLUE)
            
            width_int = self.wall_right.left - self.wall_left.right
            height_int = SCREEN_HEIGHT - self.wall_top.bottom
            
            arena_int = pygame.Rect(self.wall_left.right, self.wall_top.bottom, width_int, height_int)
            pygame.draw.rect(self.window, C_ORANGE, arena_int)
            
            
            pygame.draw.rect(self.window, C_WHITE, self.wall_left)
            pygame.draw.rect(self.window, C_WHITE, self.wall_right)
            pygame.draw.rect(self.window, C_WHITE, self.wall_top)

            player = next((e for e in self.entities if isinstance(e, Player)), None)
            if player is None:
                continue
                
            bricks_remove = []
            for entity in self.entities:
                self.window.blit(entity.surf, entity.rect) # Desenha a entidade
                type_name = entity.__class__.__name__ # Pega o nome da classe da entidade
                
                if type_name == "Ball":
                    entity.move(self.wall_left, self.wall_right, self.wall_top, player.rect) # Move a bola
                    for other_entity in self.entities:
                        if other_entity.__class__.__name__ == "Brick": # Verifica se a entidade é um tijolo
                            if entity.rect.colliderect(other_entity.rect):
                                entity.speed_y *= -1
                                
                                self.sound_brick.play()

                                bricks_remove.append(other_entity)
                                break
                else:
                    entity.move() # Move a entidade
                
            for brick in bricks_remove:
                if brick in self.entities:
                    self.entities.remove(brick)
                    
            if self.ball.rect.top > SCREEN_HEIGHT:
                player.health -= 1
                
                if player.health > 0:
                    self.ball.active = False
                    self.ball.speed_x = 0
                    self.ball.speed_y = 0
                    
                    player = next((e for e in self.entities if isinstance(e, Player)), None) 
                    if player:
                        self.ball.rect.centerx = player.rect.centerx
                        self.ball.rect.bottom = player.rect.top
                        self.ball.pos_x = float(self.ball.rect.x)
                        self.ball.pos_y = float(self.ball.rect.y)
                else:
                    self.game_over()
                    return
                     
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                    
    def game_over(self):
        pygame.mixer_music.stop()
    
        font = pygame.font.SysFont('arialblack', 72)
        
        text_surf = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.window.fill((0, 0, 0))
        self.window.blit(text_surf, text_rect)
        pygame.display.flip()
        
        pygame.time.wait(3000)
        pass
            