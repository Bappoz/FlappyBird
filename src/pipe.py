import pygame
import random
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class Pipe:
    def __init__(self, x):
        # Define a posição horizontal inicial do cano
        self.x = x  
        
        # Define a largura do cano
        self.width = 80  
        
        # Define a altura do cano como a altura da tela
        self.height = SCREEN_HEIGHT  
        
        # Define o espaço entre o cano superior e o inferior
        self.gap = 200  
        
        # Define a altura do cano superior de forma aleatória, garantindo que o espaço entre os canos seja suficiente
        self.top_height = random.randint(50, self.height - self.gap - 50)  
        
        # A altura do cano inferior é calculada com base na altura da tela e na altura do cano superior
        self.bottom_height = self.height - self.top_height - self.gap  

    def move(self):
        """Move o cano para a esquerda, simulando o movimento do cenário"""
        self.x -= 5  # Move o cano para a esquerda a uma velocidade fixa

    def reset_position(self):
        """Reposiciona o cano à direita da tela e redefine suas alturas"""
        self.x = SCREEN_WIDTH + 200  # Reposiciona o cano para o lado direito da tela (fora da tela)
        
        # Redefine a altura do cano superior aleatoriamente
        self.top_height = random.randint(50, self.height - self.gap - 50)  
        
        # Redefine a altura do cano inferior, garantindo que a distância entre os canos seja mantida
        self.bottom_height = self.height - self.top_height - self.gap  

    def draw(self, screen):
        """Desenha o cano na tela"""
        # Desenha o cano superior em verde
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self.top_height))
        
        # Desenha o cano inferior em verde
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height - self.bottom_height, self.width, self.bottom_height))

    def collide(self, player):
        """Verifica se o pássaro colidiu com o cano"""
        
        # Obtém o retângulo de colisão do pássaro
        player_rect = player.get_collision_rect()

        # Verifica se o retângulo do pássaro colide com o cano superior ou inferior
        if player_rect.colliderect(pygame.Rect(self.x, 0, self.width, self.top_height)) or player_rect.colliderect(pygame.Rect(self.x, self.height - self.bottom_height, self.width, self.bottom_height)):
            return True  # Retorna True se houve colisão
        return False  # Retorna False se não houve colisão
