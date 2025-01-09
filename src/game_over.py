import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT  
class GameOverScreen:
    def __init__(self, final_score):
        """
        Inicializa a tela de Game Over com a pontuação final e elementos visuais.
        """
        self.final_score = final_score  # Salva a pontuação final do jogador
        self.font = pygame.font.Font(None, 50)  # Define a fonte padrão para textos maiores
        self.small_font = pygame.font.Font(None, 35)  # Define uma fonte menor para textos secundários
        self.button_height = 60  # Altura fixa para os botões
        self.button_spacing = 20  # Espaçamento vertical entre os botões

        # Define os botões disponíveis com rótulos, ações e posições
        self.buttons = [
            {"label": "Reiniciar", "action": "restart", "y_position": 400, "font": self.font},
            {"label": "Voltar ao Menu", "action": "menu", "y_position": 480, "font": self.small_font}
        ]

        # Carrega a imagem de "Game Over" e ajusta para ser exibida centralizada na tela
        self.game_over_image = pygame.image.load("assets/images/gameover.png").convert_alpha()
        self.game_over_image_rect = self.game_over_image.get_rect(
            center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100)
        )

    def draw(self, screen):
        """
        Desenha a tela de Game Over incluindo texto, imagem e botões.
    
        """
        # Desenha a imagem "Game Over" no centro da tela
        screen.blit(self.game_over_image, self.game_over_image_rect)

        # Mostra a pontuação final do jogador abaixo da imagem
        self.display_text(screen, f"Pontuação: {self.final_score}", (255, 255, 255), SCREEN_HEIGHT // 2)

        # Percorre a lista de botões e desenha cada um deles
        for button in self.buttons:
            self.draw_button(screen, button["label"], button["y_position"], button["font"])

    def display_text(self, screen, text, color, y_position):
        
        # Renderiza o texto com a fonte definida e a cor fornecida
        text_surface = self.font.render(text, True, color)
        # Centraliza o texto horizontalmente na tela
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, y_position))
        # Desenha o texto na superfície fornecida
        screen.blit(text_surface, text_rect)

    def draw_button(self, screen, text, y_position, font):
        
        button_width = 200  # Define uma largura fixa para todos os botões
        # Cria o retângulo que representa o botão
        button_rect = pygame.Rect(
            (SCREEN_WIDTH - button_width) // 2, y_position, button_width, self.button_height
        )
        # Preenche o botão com um fundo branco
        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        # Desenha uma borda preta ao redor do botão
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
        # Renderiza o texto do botão na cor preta
        text_surface = font.render(text, True, (0, 0, 0))
        # Centraliza o texto no retângulo do botão
        text_rect = text_surface.get_rect(center=button_rect.center)
        # Desenha o texto no botão
        screen.blit(text_surface, text_rect)

    def handle_events(self):
        """
        Lida com eventos da tela de Game Over, como cliques do mouse.
       
        """
        # Percorre todos os eventos capturados pelo Pygame
        for event in pygame.event.get():
            # Se o evento for para fechar o jogo
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Se o evento for um clique do mouse
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Verifica se o clique foi com o botão esquerdo
                    mouse_x, mouse_y = event.pos  # Obtém as coordenadas do clique do mouse
                    # Itera sobre os botões para verificar se algum foi clicado
                    for index, button in enumerate(self.buttons):
                        # Calcula a posição vertical do botão atual
                        y = 400 + index * (self.button_height + self.button_spacing)
                        # Cria o retângulo representando o botão
                        button_rect = pygame.Rect(
                            SCREEN_WIDTH // 2 - 100, y, 200, self.button_height
                        )
                        # Verifica se o clique ocorreu dentro dos limites do botão
                        if button_rect.collidepoint(mouse_x, mouse_y):
                            return button["action"]  # Retorna a ação correspondente ao botão
        return None  # Retorna None caso nenhum botão tenha sido clicado
