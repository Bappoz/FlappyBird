import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class Menu:
    def __init__(self):
        # Carrega o fundo e o título do menu
        self.background = pygame.image.load("assets/images/background.jpg").convert()
        self.title_image = pygame.transform.scale(
            pygame.image.load("assets/images/titulo.png").convert_alpha(), 
            (500, 200)  # Redimensiona a imagem do título para 500x200 pixels
        )
        
        # Define a fonte e as configurações dos botões
        self.font = pygame.font.Font(None, 74)  # Fonte para o título
        self.buttons = [  # Define os botões do menu
            {"text": "Jogar", "action": "play"},
            {"text": "Recordes", "action": "records"},
            {"text": "Sair", "action": "exit"}
        ]
        self.button_width = 200  # Largura dos botões
        self.button_height = 50  # Altura dos botões
        self.button_spacing = 20  # Espaçamento entre os botões

    def draw_button(self, screen, text, y_position):
        """Desenha um botão na tela."""
        button_font = pygame.font.Font(None, 50)  # Fonte para o texto dos botões
        button_text = button_font.render(text, True, (0, 0, 0))  # Renderiza o texto em preto
        button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - self.button_width // 2,  # Centraliza horizontalmente
            y_position - self.button_height // 2,  # Define a posição vertical
            self.button_width, self.button_height
        )
        
        # Desenha o retângulo do botão
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Fundo branco
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Borda preta
        
        # Centraliza o texto dentro do botão
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)

    def draw(self, screen):
        """Desenha todos os elementos do menu (fundo, título e botões)."""
        
        # Desenha o fundo
        screen.blit(self.background, (0, 0))
        
        # Desenha o título centralizado
        screen.blit(
            self.title_image, 
            (SCREEN_WIDTH // 2 - self.title_image.get_width() // 2, 50)
        )
        
        # Desenha os botões, com espaçamento vertical entre eles
        for index, button in enumerate(self.buttons):
            y_position = 300 + index * (self.button_height + self.button_spacing)
            self.draw_button(screen, button["text"], y_position)

    def handle_events(self):
        """Lida com os eventos do menu, como cliques nos botões."""
        
        # Itera sobre os eventos do pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fecha o jogo ao clicar no "X" da janela
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:  # Verifica se o botão do mouse foi pressionado
                # Verifica se algum botão foi clicado
                for index, button in enumerate(self.buttons):
                    y_position = 300 + index * (self.button_height + self.button_spacing)
                    button_rect = pygame.Rect(
                        SCREEN_WIDTH // 2 - self.button_width // 2,  # Centraliza horizontalmente
                        y_position - self.button_height // 2,  # Define a posição vertical
                        self.button_width, self.button_height
                    )
                    if button_rect.collidepoint(event.pos):  # Verifica se o clique foi dentro do botão
                        return button["action"]  # Retorna a ação associada ao botão
        return None  # Retorna None se nenhum botão foi clicado
