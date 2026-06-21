import pygame
import sys
from code.const import SCREEN_WIDTH, SCREEN_HEIGHT, C_DARK_BLUE, C_WHITE, C_ORANGE
from code.DBProxy import DBProxy

class ScoreSystem:
    def __init__(self):
        self.db = DBProxy()
        self.font_title = pygame.font.SysFont("arialblack", 50)
        self.font_text = pygame.font.SysFont("arialblack", 24)
        self.font_ranking = pygame.font.SysFont("monospace", 22) 

    def show_input_nickname(self, window: pygame.Surface, player_score: list[int]):
        nickname = ""
        pygame.key.start_text_input() # Entrada de texto
        
        while True:
            window.fill((0, 0, 0))
            
            # Textos de orientação
            txt_victory = self.font_title.render("VOCÊ VENCEU O JOGO!", True, (0, 255, 0))
            txt_points = self.font_text.render(f"PONTUAÇÃO FINAL: {player_score[0]}", True, C_WHITE)
            txt_orientation = self.font_text.render("DIGITE SEU NICK (3 LETRAS):", True, C_ORANGE)
            
            # Desenha o Nickname na tela piscando ou fixo
            txt_nick = self.font_title.render(nickname.upper(), True, (255, 215, 0))
            
            # Renderiza na tela
            window.blit(txt_victory, txt_victory.get_rect(center=(SCREEN_WIDTH // 2, 100)))
            window.blit(txt_points, txt_points.get_rect(center=(SCREEN_WIDTH // 2, 180)))
            window.blit(txt_orientation, txt_orientation.get_rect(center=(SCREEN_WIDTH // 2, 280)))
            window.blit(txt_nick, txt_nick.get_rect(center=(SCREEN_WIDTH // 2, 360)))
            
            txt_confirmar = self.font_text.render("[PRESSIONE ENTER PARA SALVAR]", True, (120, 120, 120))
            if len(nickname) == 3:
                window.blit(txt_confirmar, txt_confirmar.get_rect(center=(SCREEN_WIDTH // 2, 450)))

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                # Captura as letras digitadas
                elif event.type == pygame.TEXTINPUT:
                    if len(nickname) < 3 and event.text.isalpha():
                        nickname += event.text
                        
                elif event.type == pygame.KEYDOWN:
                    # Apagar letra
                    if event.key == pygame.K_BACKSPACE:
                        nickname = nickname[:-1]
                    # Salvar
                    elif event.key == pygame.K_RETURN and len(nickname) == 3:
                        pygame.key.stop_text_input()
                        # Salva no banco
                        self.db.save_score(nickname, player_score[0])
                        return # Sai da tela de input

    def show_top10_menu(self, window: pygame.Surface):
        top10 = self.db.get_top10()
        
        while True:
            window.fill(C_DARK_BLUE)
            
            txt_titulo = self.font_title.render("TOP 10 SCORES", True, (255, 215, 0))
            window.blit(txt_titulo, txt_titulo.get_rect(center=(SCREEN_WIDTH // 2, 60)))
            
            cabecalho = f"{'POS':<4}{'NICK':<6}{'PONTOS':<10}{'DATA/HORA':<16}"
            txt_cabecalho = self.font_ranking.render(cabecalho, True, C_ORANGE)
            window.blit(txt_cabecalho, (SCREEN_WIDTH // 2 - 200, 140))
            
            # Linha divisória
            pygame.draw.line(window, C_WHITE, (SCREEN_WIDTH // 2 - 200, 170), (SCREEN_WIDTH // 2 + 200, 170), 2)
            
            # Lista os jogadores
            y_offset = 190
            for i, jogador in enumerate(top10):
                nick, pontos, data = jogador
                # Formata as colunas
                linha = f"{i+1:>2}. {nick:<5} {pontos:<9} {data}"
                txt_linha = self.font_ranking.render(linha, True, C_WHITE)
                window.blit(txt_linha, (SCREEN_WIDTH // 2 - 200, y_offset))
                y_offset += 30
                
            if not top10:
                txt_vazio = self.font_text.render("NENHUM RECORDE REGISTRADO", True, (150, 150, 150))
                window.blit(txt_vazio, txt_vazio.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)))

            # Rodapé para voltar
            txt_voltar = self.font_text.render("[PRESSIONE ESC PARA VOLTAR]", True, C_ORANGE)
            window.blit(txt_voltar, txt_voltar.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)))
            
            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return # Fecha a tela de score e volta para o loop do Menu principal