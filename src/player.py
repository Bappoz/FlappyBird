import pygame
from src.game_object import GameObject

class Player(GameObject):
    def __init__(self):
        super().__init__(100, 300, 55, 55)  # herança: Chama o construtor da classe base
        self._image = pygame.transform.scale(
            pygame.image.load("assets/images/FlappyBird.png").convert_alpha(),
            (self.width, self.height)
        )
        self._velocity = 0
        self._gravity = 0.4
        self._lift = -9.5
        self._jumping = False
        self._power_up_count = 0  # Contador de PowerUps coletados

    def jump(self):
        self._velocity = self._lift
        self._jumping = True

    def update(self):
        self._velocity += self._gravity
        self.y += self._velocity

    def draw(self, screen):
        screen.blit(self._image, (self.x, self.y))

    def get_collision_rect(self):
        collision_margin = 10
        return pygame.Rect(
            self.x + collision_margin,
            self.y + collision_margin,
            self.width - 2 * collision_margin,
            self.height - 2 * collision_margin
        )

    def collect_power_up(self):
        self._power_up_count += 1

    @property
    def power_up_count(self):
        return self._power_up_count

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def gravity(self):
        return self._gravity

    @gravity.setter
    def gravity(self, value):
        self._gravity = value

    @property
    def lift(self):
        return self._lift

    @lift.setter
    def lift(self, value):
        self._lift = value

    @property
    def jumping(self):
        return self._jumping

    @jumping.setter
    def jumping(self, value):
        self._jumping = value