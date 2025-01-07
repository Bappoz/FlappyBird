import pygame

class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        """Atualiza o estado do objeto do jogo."""
        pass

    def draw(self, screen):
        """Desenha o objeto do jogo na tela."""
        pass

    def get_collision_rect(self):
        """Retorna o retângulo de colisão do objeto do jogo."""
        return pygame.Rect(self.x, self.y, self.width, self.height)