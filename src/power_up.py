import pygame
import random
from src.game_object import GameObject
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class PowerUp(GameObject):
    def __init__(self):
        """Construtor que inicializa o power-up com posição aleatória e a imagem correspondente."""
        super().__init__(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 400), random.randint(50, SCREEN_HEIGHT - 50), 30, 30)
        self._image = pygame.transform.scale(
            pygame.image.load("assets/images/powerup.png").convert_alpha(),
            (self.width, self.height)
        )
        self._collected = False  # Inicialmente o power-up não foi coletado
        self.speed = 5  # Velocidade de movimento do power-up

    def update(self):
        """Atualiza a posição do power-up, movendo-o para a esquerda e reposicionando quando sai da tela."""
        self.x -= self.speed # Move o power-up para a esquerda
        if self.x + self.width < 0:
            self.reset_position()

    def reset_position(self):
        """Reposiciona o power-up de maneira aleatória na tela e o marca como não coletado."""
        self.x = random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 400)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)
        self._collected = False  # Resetando o status de coleta

    def draw(self, screen):
        """Desenha o power-up na tela, caso ele não tenha sido coletado."""
        if not self._collected:
            screen.blit(self._image, (self.x, self.y))

    def collect(self):
        """Marca o power-up como coletado."""
        self._collected = True

    def is_colliding_with_pipe(self, pipes):
        """Verifica se o power-up está colidindo com algum tubo da lista fornecida."""
        for pipe in pipes:
            if any(pipe_rect.colliderect(self.get_collision_rect()) for pipe_rect in pipe.get_collision_rect()):
                return True  # Retorna True assim que a colisão é detectada
        return False

    @property
    def collected(self):
        """Obtém o status de coleta do power-up."""
        return self._collected

    @collected.setter
    def collected(self, value):
        """Define o status de coleta do power-up, permitindo apenas valores booleanos."""
        if isinstance(value, bool):
            self._collected = value
        else:
            raise ValueError("A propriedade 'collected' deve ser um valor booleano.")

    @property
    def image(self):
        """Obtém a imagem do power-up."""
        return self._image

    @image.setter
    def image(self, value):
        """Define a imagem do power-up com a escala apropriada."""
        self._image = pygame.transform.scale(value, (self.width, self.height))
