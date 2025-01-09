"""
Este arquivo define a classe base GameObject, que serve como uma superclasse para todos os objetos do jogo.
A classe GameObject fornece uma estrutura básica para objetos do jogo, incluindo posição, tamanho e métodos
para atualização, desenho e detecção de colisão.
"""

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