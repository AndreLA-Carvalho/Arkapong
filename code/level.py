import pygame

from code.const import C_ORANGE, C_WHITE, C_DARK_BLUE, SCREEN_HEIGHT, SCREEN_WIDTH, ENTITY_SCORE
from code.entity import Entity
from code.player import Player
from code.ball import Ball
from code.brick import Brick

class Level:
    def __init__(self, window: pygame.Surface, name: str, player_score: list[int], player_health: list[int], numero_fase: int):
        self.window = window
        self.name = name
        self.player_score = player_score
        self.player_health = player_health
        self.numero_fase = numero_fase
        self.entities: list[Entity] = []
        player = Player(window, (SCREEN_WIDTH // 2, 530)) # Posiciona o jogador no centro da tela
        player.health = self.player_health[0] # Define a vida do jogador
        self.entities.append(player)
        self.ball = Ball(window, (SCREEN_WIDTH // 2, 510)) # Posiciona a bola no centro da tela, acima do jogador
        self.entities.append(self.ball)
        
        arena_width = 400
        arena_thickness = 10
        arena_margin = (SCREEN_WIDTH - arena_width) // 2
        
        self.wall_left = pygame.Rect(arena_margin, 0, arena_thickness, SCREEN_HEIGHT) 
        self.wall_right = pygame.Rect(arena_margin + arena_width - arena_thickness, 0, arena_thickness, SCREEN_HEIGHT)
        self.wall_top = pygame.Rect(arena_margin, 0, arena_width, arena_thickness)
        
        # Configuração das tijolos
        self.brick_width = 34
        self.brick_height = 20
        brick_spacing = 4
        
        # Posição inicial dos tijolos
        start_x = arena_margin + arena_thickness + 2
        start_y = 60
        
        # Mapa do level
        if self.numero_fase == 1:
            level_map = [
            "1111111111",
            "1113113111",  
            "1113113111",
            "1111111111",
            "1311111131",  
            "1133333311",  
            "2222222222"
            ]
            
        elif self.numero_fase == 2:
            level_map = [
            "2.2.2.2.2.",
            ".2.2.2.2.2",  
            "2.2.2.2.2.",
            ".2.2.2.2.2",
            "2.2.2.2.2.",  
            ".2.2.2.2.2",  
            "2.2.2.2.2."
            ]
        
        for row_index, row in enumerate(level_map):
            for col_index in range(len(row)):
                cell = row[col_index]
                if cell == '.':
                    continue
                x = start_x + col_index * (self.brick_width + brick_spacing)
                y = start_y + row_index * (self.brick_height + brick_spacing)
        
                if cell == '1':
                    name_brick = "brick1"
                elif cell == '2':
                    name_brick = "brick2"
                elif cell == '3':
                    name_brick = "brick3"
                    
                brick = Brick(self.window, (x,y), name_brick, self.brick_width, self.brick_height)
                
                if self.numero_fase == 2:
                    brick.hp = 2
                
                self.entities.append(brick)
        
        self.sound_brick = pygame.mixer.Sound("asset/brickHit.mp3")
        self.sound_brick.set_volume(1)
        
        # Sistema de cronometro
        self.tempo_inicial = pygame.time.get_ticks()
        self.fonte_ui = pygame.font.SysFont("Arial", 18)
        
                
    def run(self, player_score: list[int]):
        pygame.mixer_music.load(f"asset/level1.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        
        while True:
            self.window.fill(C_DARK_BLUE)
            
            width_int = self.wall_right.left - self.wall_left.right
            height_int = SCREEN_HEIGHT - self.wall_top.bottom
            
            arena_int = pygame.Rect(self.wall_left.right, self.wall_top.bottom, width_int, height_int)
            pygame.draw.rect(self.window, C_ORANGE, arena_int)
            
            # Desenha as paredes
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
                                
                                self.sound_brick.play()
                                
                                overlap_x = min(entity.rect.right, other_entity.rect.right) - max(entity.rect.left, other_entity.rect.left)
                                overlap_y = min(entity.rect.bottom, other_entity.rect.bottom) - max(entity.rect.top, other_entity.rect.top)
                                
                                if overlap_x < overlap_y:
                                    entity.speed_x *= -1 # Inverte a direção horizontal
                                    
                                    # Descobre se bateu na esquerda ou na direita do tijolo para recuar
                                    if entity.rect.centerx < other_entity.rect.centerx:
                                        # Bateu na lateral esquerda do bloco
                                        entity.rect.right = other_entity.rect.left
                                        entity.pos_x = float(entity.rect.x)
                                    else:
                                        # Bateu na lateral direita do bloco
                                        entity.rect.left = other_entity.rect.right
                                        entity.pos_x = float(entity.rect.x)
                                        
                                # Batida por cima ou por baixo
                                else:
                                    entity.speed_y *= -1 # Inverte a direção vertical
                                    
                                    if entity.rect.centery < other_entity.rect.centery:
                                        
                                        # Bateu por cima
                                        entity.rect.bottom = other_entity.rect.top
                                        entity.pos_y = float(entity.rect.y)
                                    else:
                                        # Bateu por baixo
                                        entity.rect.top = other_entity.rect.bottom
                                        entity.pos_y = float(entity.rect.y)
                                
                                if self.numero_fase == 2 and other_entity.name == 'brick2' and other_entity.hp == 2:
                                    self.player_score[0] += ENTITY_SCORE.get('brick2', 20) # Ganha os pontos do brick2
                                    other_entity.hp = 1
                                    other_entity.name = 'brick1'
                                    other_entity.surf = pygame.image.load('asset/brick1.png').convert_alpha()
                                    other_entity.surf = pygame.transform.scale(other_entity.surf, (self.brick_width, self.brick_height))
                                else:
                                    self.player_score[0] += ENTITY_SCORE.get(other_entity.name, 10) # Se for bloco comum ou o segundo hit do brick2, puxa os pontos pelo nome atual
                                    bricks_remove.append(other_entity)
                                break
                else:
                    entity.move() # Move a entidade
                
            for brick in bricks_remove:
                if brick in self.entities:
                    self.entities.remove(brick)
                    
            # Calcula o tempo da fase em segundos
            time_level_seconds = (pygame.time.get_ticks() - self.tempo_inicial) / 1000.0
            
            # Mostra o texto na tela das informações do jogador
            texto_pontos = self.fonte_ui.render(f"PONTOS: {self.player_score[0]}", True, (255, 255, 255))
            texto_vidas = self.fonte_ui.render(f"VIDAS: {self.player_health[0]}", True, (255, 255, 255))
            texto_tempo = self.fonte_ui.render(f"TEMPO: {int(time_level_seconds)}s", True, (255, 255, 255))
            
            self.window.blit(texto_pontos, (15, 30))
            self.window.blit(texto_vidas, (15, 65))
            self.window.blit(texto_tempo, (15, 100))
                    
            bricks_left = [e for e in self.entities if e.__class__.__name__ == "Brick"] # Lista de tijolos restantes
            
            if len(bricks_left) == 0:
                # Calcula o multiplicador baseado no tempo
                if time_level_seconds <= 80.0:
                    multiplier = 3
                elif time_level_seconds <= 120.0:
                    multiplier = 2
                else:
                    multiplier = 1
                
                # Multiplica os pontos pelo multiplicador
                self.player_score[0] *= multiplier
                
                if self.numero_fase == 1:
                    self.show_transition("LEVEL 2")
                    return True
                else:
                    self.show_transition("VOCÊ VENCEU!")
                    return True
                    
            if self.ball.rect.top > SCREEN_HEIGHT:
                self.player_health[0] -= 1
                
                if self.player_health[0] > 0:
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
    
    def show_transition(self, message):
        font = pygame.font.SysFont('arialblack', 72)
        
        text_surf = font.render(message, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.window.fill((0, 0, 0))
        self.window.blit(text_surf, text_rect)
        pygame.display.flip()
        pygame.time.wait(3000)
        
        pygame.mixer_music.load(f"asset/level1.mp3")
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)
        
            