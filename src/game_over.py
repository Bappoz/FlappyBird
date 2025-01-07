import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class GameOverScreen:
    def __init__(self, final_score):
        self.final_score = final_score  # Pontuação final do jogador
        self.font = pygame.font.Font(None, 50)  # Fonte para o texto principal
        self.small_font = pygame.font.Font(None, 35)  # Fonte menor para o botão "Voltar ao Menu"
        self.button_height = 60  # Altura dos botões
        self.button_spacing = 20  # Espaçamento entre os botões
        self.buttons = [
            {"label": "Reiniciar", "action": "restart", "y_position": 400, "font": self.font},
            {"label": "Voltar ao Menu", "action": "menu", "y_position": 480, "font": self.small_font}
        ]  # Lista de botões com suas propriedades
        self.game_over_image = pygame.image.load("assets/images/gameover.png").convert_alpha()  # Carrega a imagem de Game Over
        self.game_over_image_rect = self.game_over_image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100))  # Centraliza a imagem de Game Over na tela

    def draw(self, screen):
        
        # Desenha a imagem de Game Over
        screen.blit(self.game_over_image, self.game_over_image_rect)
        
        # Exibe a pontuação na tela
        self.display_text(screen, f"Pontuação: {self.final_score}", (255, 255, 255), SCREEN_HEIGHT // 2)

        # Desenha os botões na tela
        for button in self.buttons:
            self.draw_button(screen, button["label"], button["y_position"], button["font"])

    def display_text(self, screen, text, color, y_position):
        # Renderiza o texto com a fonte e cor especificadas
        text_surface = self.font.render(text, True, color)
        # Centraliza o texto na posição y especificada
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_position))
        # Desenha o texto na tela
        screen.blit(text_surface, text_rect)

    def draw_button(self, screen, text, y_position, font):
        button_width = 200 # Define a largura do botão
        # Cria um retângulo para o botão
        button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, y_position, button_width, self.button_height)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Fundo branco
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2) # Desenha o retângulo do botão
        text_surface = font.render(text, True, (0, 0, 0)) # Renderiza o texto do botão
        text_rect = text_surface.get_rect(center=button_rect.center) # Centraliza o texto no retângulo do botão
        screen.blit(text_surface, text_rect) # Desenha o texto do botão na tela

    def handle_events(self):
        """Lida com os eventos da tela de Game Over"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo do mouse
                    mouse_x, mouse_y = event.pos
                    for index, button in enumerate(self.buttons):
                        y = 400 + index * (self.button_height + self.button_spacing)
                        button_rect = pygame.Rect(
                            SCREEN_WIDTH // 2 - 100, y, 200, self.button_height
                        )
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            return button["action"]
        return None