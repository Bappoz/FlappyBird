import pygame
import random
from src.game_object import GameObject
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(GameObject):
    def __init__(self):
        # herança: Chama o construtor da classe base
        super().__init__(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 400), random.randint(50, SCREEN_HEIGHT - 50), 30, 30)
        self.image = pygame.transform.scale(
            pygame.image.load("assets/images/powerup.png").convert_alpha(),
            (self.width, self.height)
        )
        self.collected = False

    def update(self):
        self.x -= 5
        if self.x + self.width < 0:
            self.reset_position()

    def reset_position(self):
        self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 400)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.collected = False

    def draw(self, screen):
        if not self.collected:
            screen.blit(self.image, (self.x, self.y))

    def collect(self):
        self.collected = True

    def is_colliding_with_pipe(self, pipes):
        for pipe in pipes:
            if any(pipe_rect.colliderect(self.get_collision_rect()) for pipe_rect in pipe.get_collision_rect()):
                return True
        return False