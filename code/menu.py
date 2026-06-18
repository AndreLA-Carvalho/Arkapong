import pygame

from code.const import MENU_OPTIONS, SCREEN_WIDTH, SCREEN_HEIGHT, C_ORANGE, C_LIGHT_ORANGE, C_WHITE
from code.background import Background
from code.entityFactory import EntityFactory

# Efeito de título com sombra
class titleEffect:
    def __init__(self, text: str, font: pygame.font.Font, pos_x: int, pos_y: int): 
        self.text = text
        self.text_base = font.render(self.text, True, C_ORANGE) # Renderiza o texto principal com a cor C_ORANGE
        self.text_shadow = font.render(self.text, True, C_LIGHT_ORANGE) # Renderiza o texto de sombra com a cor C_LIGHT_ORANGE
    
        self.font = font
        
        self.pos = (pos_x, pos_y) # Posição do texto
        self.width = self.text_base.get_width()
        self.height = self.text_base.get_height() 
        
        self.pos_shadow = -50 # Posição inicial do texto de sombra
        self.width_shadow = 20 # Largura da parte visível do texto de sombra
        self.speed_shadow = 5 # Velocidade de movimento do texto de sombra
        
        self.reset_shadow = self.width + 400 # Posição de reset do texto de sombra
        
    def draw(self, surface: pygame.Surface): 
        surface.blit(self.text_base, self.pos)
        
        self.pos_shadow += self.speed_shadow # Move o texto de sombra
        if self.pos_shadow > self.reset_shadow: # Se o texto de sombra saiu da tela
            self.pos_shadow = -50 # Reseta a posição do texto de sombra
            
        area_cut = pygame.Rect(self.pos_shadow, 0, self.width_shadow, self.height) # Cria uma área de corte para o texto de sombra
        
        destiny_pos = (self.pos[0] + self.pos_shadow, self.pos[1]) 
        surface.blit(self.text_shadow, destiny_pos, area=area_cut)
        

# Menu principal
class Menu:
    def __init__(self, window):
        self.window = window
        self.background_layers = []
        self.layer_names = [
            'menuBg5',
            'menuBg0',
            'menuBg4',
            'menuBg1',
            'menuBg3',
            'menuBg2'
        ]
       

        for name in self.layer_names:
            if name == 'menuBg1':
                bg1 = Background(name, (0, 0))
                self.background_layers.append(bg1) 
            else:
                bg1 = Background(name, (0, 0))
                bg2 = Background(name, (SCREEN_WIDTH, 0))
                self.background_layers.extend([bg1, bg2])
        

    # Executa o menu
    def run(self):
        menu_option = 0
        clock = pygame.time.Clock() 
        title = titleEffect("ARKAPONG", pygame.font.Font(None, 80), SCREEN_WIDTH // 2, 140) 
        
        while True:
            clock.tick(60)
            
            self.window.fill((0, 0, 0)) 
            
            for bg in self.background_layers:
                if bg.name != 'menuBg1': 
                    bg.move()
                self.window.blit(source=bg.surf, dest=bg.rect) 
                
                
            title.draw(self.window) # Desenha o título com efeito de sombra
            
            # Opções do menu
            for i in range(len(MENU_OPTIONS)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTIONS[i], C_LIGHT_ORANGE, (SCREEN_WIDTH // 2, 300 + i * 50))
                else:
                    self.menu_text(20, MENU_OPTIONS[i], C_WHITE, (SCREEN_WIDTH // 2, 300 + i * 50))
                    
            self.menu_text(16, "A - Esquerda | D - Direita", C_WHITE, (SCREEN_WIDTH - 650, 550))
            self.menu_text(16, "ESPACO - Atirar", C_WHITE, (SCREEN_WIDTH - 650, 570))
            self.menu_text(16, "ENTER - Selecionar", C_WHITE, (SCREEN_WIDTH - 650, 590))
                
            # Processa eventos
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: # Sai do jogo
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: # Sai do jogo
                        pygame.quit()
                        exit()
                    if event.key == pygame.K_w: # Move para cima
                        if menu_option > 0:
                            menu_option -= 1
                    if event.key == pygame.K_s: # Move para baixo
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1
                    if event.key == pygame.K_RETURN: # Seleciona
                        return MENU_OPTIONS[menu_option]
                    
            pygame.display.flip()
                        
    # Renderiza o texto no menu
    def menu_text(self, text_size: int, text: str, color: tuple, text_center_pos: tuple):
        text_font: pygame.font.Font = pygame.font.SysFont(name='arialblack', size=text_size) 
        text_surf: pygame.Surface = text_font.render(text, True, color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
        
