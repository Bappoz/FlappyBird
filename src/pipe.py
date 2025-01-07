import pygame
import random
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.game_object import GameObject

# Classe Pipe: Representa os canos no jogo.
class Pipe(GameObject):
    def __init__(self, x):
        # Inicializa o cano chamando o construtor da classe base (GameObject).
        super().__init__(x, 0, 80, SCREEN_HEIGHT)  # Define posição inicial e dimensões.
        self._gap = 200  # Define o espaço (gap) entre os canos superior e inferior.
        
        # Calcula a altura do cano superior e inferior, de forma aleatória.
        self._top_height = random.randint(50, self.height - self._gap - 50)
        self._bottom_height = self.height - self._top_height - self._gap

    # Atualiza a posição do cano, movendo-o para a esquerda.
    def update(self):
        self.x -= 5  # Move o cano em 5 unidades por atualização.

    # Reseta a posição do cano quando ele sai da tela.
    def reset_position(self):
        self.x = SCREEN_WIDTH + 200  # Reposiciona o cano para fora da tela, no lado direito.
        
        # Recalcula alturas aleatórias para o topo e base do cano.
        self._top_height = random.randint(50, self.height - self._gap - 50)
        self._bottom_height = self.height - self._top_height - self._gap

    # Desenha os canos superior e inferior na tela.
    def draw(self, screen):
        # Desenha o cano superior (retângulo verde).
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self._top_height))
        
        # Desenha o cano inferior (retângulo verde).
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height - self._bottom_height, self.width, self._bottom_height))

    # Retorna os retângulos de colisão dos canos (superior e inferior).
    def get_collision_rect(self):
        return [
            # Retângulo do cano superior.
            pygame.Rect(self.x, 0, self.width, self._top_height),
            
            # Retângulo do cano inferior.
            pygame.Rect(self.x, self.height - self._bottom_height, self.width, self._bottom_height)
        ]

    # Propriedade para acessar o espaço (gap) entre os canos (agora privada).
    @property
    def gap(self):
        return self._gap

    # Permite alterar o espaço (gap) entre os canos (agora privada).
    @gap.setter
    def gap(self, value):
        self._gap = value

    # Propriedade para acessar a altura do cano superior (agora privada).
    @property
    def top_height(self):
        return self._top_height

    # Permite alterar a altura do cano superior (agora privada).
    @top_height.setter
    def top_height(self, value):
        self._top_height = value

    # Propriedade para acessar a altura do cano inferior (agora privada).
    @property
    def bottom_height(self):
        return self._bottom_height

    # Permite alterar a altura do cano inferior (agora privada).
    @bottom_height.setter
    def bottom_height(self, value):
        self._bottom_height = value
