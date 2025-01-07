import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverScreen:
    def __init__(self, final_score):
        # Inicializa a tela de Game Over com a pontuação final
        self.final_score = final_score
        self.font = pygame.font.Font(None, 50)  # Fonte principal para textos grandes
        self.small_font = pygame.font.Font(None, 35)  # Fonte secundária para textos menores
        self.button_height = 60  # Altura dos botões
        self.button_spacing = 20  # Espaçamento entre os botões
        
        # Lista de botões com rótulos, ações e posições Y
        self.buttons = [
            {"label": "Reiniciar", "action": "restart", "y_position": 400, "font": self.font},
            {"label": "Voltar ao Menu", "action": "menu", "y_position": 480, "font": self.small_font}
        ]
        # Carrega a imagem do Game Over
        self.game_over_image = pygame.image.load("assets/images/gameover.png").convert_alpha()
        # Ajusta a posição da imagem de Game Over para o centro da tela
        self.game_over_image_rect = self.game_over_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))

    def draw(self, screen):
        # Desenha a imagem de Game Over na tela
        screen.blit(self.game_over_image, self.game_over_image_rect)
        
        # Exibe o texto de pontuação na tela, centralizado no meio da tela
        self.display_text(screen, f"Pontuação: {self.final_score}", (255, 255, 255), SCREEN_HEIGHT // 2)

        # Desenha os botões na tela
        for button in self.buttons:
            self.draw_button(screen, button["label"], button["y_position"], button["font"])

    def display_text(self, screen, text, color, y_position):
        # Renderiza o texto para exibição e o posiciona no centro
        text_surface = self.font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_position))
        screen.blit(text_surface, text_rect)

    def draw_button(self, screen, text, y_position, font):
        # Calcula a posição e o tamanho do botão
        button_width = 200  # Largura do botão
        button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, y_position, button_width, self.button_height)
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Desenha o contorno do botão
        # Renderiza o texto do botão e o posiciona no centro
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=button_rect.center)
        screen.blit(text_surface, text_rect)

    def handle_events(self):
        # Lida com os eventos da tela de Game Over
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # Detecta clique do mouse
                mouse_pos = event.pos  # Pega a posição do clique
                for button in self.buttons:
                    # Define o retângulo de colisão para o botão
                    button_rect = pygame.Rect((SCREEN_WIDTH - 200) // 2, button["y_position"], 200, self.button_height)
                    # Verifica se o clique ocorreu dentro do botão
                    if button_rect.collidepoint(mouse_pos):
                        return button["action"]  # Retorna a ação associada ao botão
        return None  # Se não houver clique, retorna None
