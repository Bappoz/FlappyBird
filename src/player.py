import pygame
from src.game_object import GameObject

class Player(GameObject):
    def __init__(self):
        super().__init__(100, 300, 55, 55)  # herança: Chama o construtor da classe base
        self._image = pygame.transform.scale(
            pygame.image.load("assets/images/FlappyBird.png").convert_alpha(),
            (self.width, self.height)
        )
        self._velocity = 0  # Velocidade inicial
        self._gravity = 0.4  # Gravidade
        self._lift = -9.5  # Força de impulso do pulo
        self._jumping = False  # Controle se o jogador está pulando
        self._power_up_count = 0  # Contador de PowerUps coletados

    def jump(self):
        """Faz o jogador pular aplicando o impulso."""
        self._velocity = self._lift
        self._jumping = True

    def update(self):
        """Atualiza a posição do jogador com base na velocidade e gravidade."""
        self._velocity += self._gravity # Faz com que a velocidade do jogador aumente continuamente enquanto ele cai
        self.y += self._velocity

    def draw(self, screen):
        """Desenha o jogador na tela."""
        screen.blit(self._image, (self.x, self.y))

    def get_collision_rect(self):
        """Retorna o retângulo de colisão do jogador com uma margem de segurança."""
        collision_margin = 10
        return pygame.Rect(
            self.x + collision_margin,
            self.y + collision_margin,
            self.width - 2 * collision_margin,
            self.height - 2 * collision_margin
        )

    def collect_power_up(self):
        """Incrementa o contador de power-ups coletados."""
        self._power_up_count += 1

    # Propriedades para acessar e modificar atributos privados

    @property
    def power_up_count(self):
        """Obtém o contador de power-ups coletados."""
        return self._power_up_count

    @property
    def velocity(self):
        """Obtém a velocidade do jogador."""
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        """Define a velocidade do jogador."""
        self._velocity = value

    @property
    def gravity(self):
        """Obtém a gravidade aplicada ao jogador."""
        return self._gravity

    @gravity.setter
    def gravity(self, value):
        """Define a gravidade aplicada ao jogador."""
        self._gravity = value

    @property
    def lift(self):
        """Obtém o valor da força de impulso do pulo."""
        return self._lift

    @lift.setter
    def lift(self, value):
        """Define o valor da força de impulso do pulo."""
        self._lift = value

    @property
    def jumping(self):
        """Obtém se o jogador está pulando."""
        return self._jumping

    @jumping.setter
    def jumping(self, value):
        """Define se o jogador está pulando."""
        self._jumping = value
