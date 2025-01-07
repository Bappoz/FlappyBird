import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self):
        self.background = pygame.image.load("assets/images/background.jpg").convert()
        self.title_image = pygame.transform.scale(
            pygame.image.load("assets/images/titulo.png").convert_alpha(),
            (500, 200)
        )
        self.font = pygame.font.Font(None, 74)
        self.buttons = [
            {"text": "Jogar", "action": "play"},
            {"text": "Recordes", "action": "records"},
            {"text": "Sair", "action": "exit"}
        ]
        self.button_width = 200
        self.button_height = 50
        self.button_spacing = 20

    def draw_button(self, screen, text, y_position):
        button_font = pygame.font.Font(None, 50)
        button_text = button_font.render(text, True, (0, 0, 0))
        button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - self.button_width // 2, y_position - self.button_height // 2, self.button_width, self.button_height
        )
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Fundo branco
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Borda preta
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

    def draw(self, screen):
        """Desenha todos os elementos do menu (fundo, título e botões)."""
        
        # Desenha o fundo
        screen.blit(self.background, (0, 0))
        
        # Desenha a imagem do título, centralizando ela na tela
        screen.blit(
            self.title_image, 
            (SCREEN_WIDTH // 2 - self.title_image.get_width() // 2, 50)
        )
        
        # Desenha os botões na tela, com um espaçamento entre eles
        for index, button in enumerate(self.buttons):
            y_position = 300 + index * (self.button_height + self.button_spacing)
            self.draw_button(screen, button["text"], y_position)

    def handle_events(self):
        """Lida com os eventos do menu, como cliques nos botões."""
       
        # Verifica todos os eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Fecha o jogo se a janela for fechada
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for index, button in enumerate(self.buttons):
                    y_position = 300 + index * (self.button_height + self.button_spacing)
                    button_rect = pygame.Rect(
                        SCREEN_WIDTH // 2 - self.button_width // 2, y_position - self.button_height // 2, self.button_width, self.button_height
                    )
                    if button_rect.collidepoint(event.pos):
                        return button["action"]
        return None