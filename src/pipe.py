import pygame
import random
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT
from src.game_object import GameObject

class Pipe(GameObject):
    def __init__(self, x):
        super().__init__(x, 0, 80, SCREEN_HEIGHT) # herança: Chama o construtor da classe base
        self._gap = 200
        self._top_height = random.randint(50, self.height - self._gap - 50)
        self._bottom_height = self.height - self._top_height - self._gap

    def update(self):
        self.x -= 5

    def reset_position(self):
        self.x = SCREEN_WIDTH + 200
        self._top_height = random.randint(50, self.height - self._gap - 50)
        self._bottom_height = self.height - self._top_height - self._gap

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, 0, self.width, self._top_height))
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.height - self._bottom_height, self.width, self._bottom_height))

    def get_collision_rect(self):
        return [
            pygame.Rect(self.x, 0, self.width, self._top_height),
            pygame.Rect(self.x, self.height - self._bottom_height, self.width, self._bottom_height)
        ]

    @property
    def gap(self):
        return self._gap

    @gap.setter
    def gap(self, value):
        self._gap = value

    @property
    def top_height(self):
        return self._top_height

    @top_height.setter
    def top_height(self, value):
        self._top_height = value

    @property
    def bottom_height(self):
        return self._bottom_height

    @bottom_height.setter
    def bottom_height(self, value):
        self._bottom_height = value