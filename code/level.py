import pygame

from code.const import C_WHITE, SCREEN_HEIGHT, SCREEN_WIDTH
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
        player = Player(window, (SCREEN_WIDTH // 2, 530)) 
        self.entities.append(player)
        
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
                
    def run(self, player_score: int):
        pygame.mixer_music.load(f"asset/{self.name}.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        while True:
            self.window.fill((0, 0, 0))
            pygame.draw.rect(self.window, C_WHITE, self.wall_left)
            pygame.draw.rect(self.window, C_WHITE, self.wall_right)
            pygame.draw.rect(self.window, C_WHITE, self.wall_top)


            for entity in self.entities:
                self.window.blit(entity.surf, entity.rect) # Desenha a entidade
                if isinstance(entity, Ball):
                    entity.move(self.wall_left, self.wall_right, self.wall_top)
                else:
                    entity.move() # Move a entidade
                    
                    
                    
                    
                # if isinstance(entity, Player):
                #     shoot = entity.shoot()
                #     if shoot is not None:
                #         self.entities.append(shoot)
                # if entity.name == "Player1":
                #     self.level_text(text_size=14, text=f"Health: {entity.health}", text_color=(255, 255, 255), pos=(50, 50))
                #     self.level_text(text_size=14, text=f"Score: {entity.score}", text_color=(255, 255, 255), pos=(50, 70))
                    
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            