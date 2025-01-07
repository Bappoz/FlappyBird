import pygame

class Player:
    def __init__(self):
        # Carrega a imagem do pássaro e redimensiona para o tamanho desejado
        self.image = pygame.transform.scale(
            pygame.image.load("assets/images/FlappyBird.png").convert_alpha(),
            (55, 55)  # Redimensiona a imagem para 55x55 pixels
        )
        
        # Posição inicial do pássaro na tela
        self.x = 100  
        self.y = 300  
        
        # Largura e altura da imagem do pássaro
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        # Velocidade inicial do pássaro
        self.velocity = 0
        # Gravidade aplicada ao pássaro
        self.gravity = 0.4
        # Força de levantamento quando o pássaro pula
        self.lift = -9.5
        # Variável que controla se o pássaro está pulando
        self.jumping = False

    def jump(self):
        """Faz o pássaro saltar, alterando sua velocidade para um valor negativo"""
        self.velocity = self.lift  # Aplica o valor da força de levantamento para simular o pulo
        self.jumping = True  # Marca que o pássaro está no ar (pulando)

    def update(self):
        """Atualiza a posição do pássaro com base na velocidade e gravidade"""
        self.velocity += self.gravity  # Aplica a gravidade, aumentando a velocidade do pássaro
        self.y += self.velocity  # Atualiza a posição vertical do pássaro

    def get_collision_rect(self):
        """Retorna o retângulo de colisão do pássaro, com uma margem ajustável"""
        collision_margin = 10  # Ajusta a margem de colisão para melhorar a detecção
        return pygame.Rect(
            self.x + collision_margin,  # Ajusta a posição x do retângulo de colisão
            self.y + collision_margin,  # Ajusta a posição y do retângulo de colisão
            self.width - 2 * collision_margin,  # Largura do retângulo de colisão com a margem
            self.height - 2 * collision_margin  # Altura do retângulo de colisão com a margem
        )

    def draw(self, screen):
        """Desenha a imagem do pássaro na tela"""
        screen.blit(self.image, (self.x, self.y))  # Desenha a imagem na posição (x, y)
