import pygame
import sys
from src.player import Player
from src.pipe import Pipe
from src.menu import Menu
from src.game_over import GameOverScreen
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        # Inicializa o pygame e configura a tela
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cópia Flappy Bird")  # Define o título da janela
        self.clock = pygame.time.Clock()  # Controla o FPS do jogo
        self.background = pygame.image.load("assets/images/background.jpg").convert()  # Carrega o fundo do jogo
        self.background_x = 0  # Posição inicial do fundo (inicializar o movimento do fundo)

        # Inicializa o menu do jogo
        self.menu = Menu()
        self.reset_game()

        # Carregar áudios para o jogo
        pygame.mixer.music.load("assets/sounds/musica.mp3")  # Música de fundo
        pygame.mixer.music.set_volume(0.3)  # Diminuir o volume da música
        pygame.mixer.music.play(-1)  # Toca a música em loop

        # Sons específicos do jogo
        self.sound_jump = pygame.mixer.Sound("assets/sounds/audiojump.mp3")  # Som do pulo
        pygame.mixer.SoundType.set_volume(self.sound_jump, 0.3)  # Ajusta o volume do som de pulo
        self.sound_score = pygame.mixer.Sound("assets/sounds/pontuacao.mp3")  # Som de pontuação
        self.sound_morte = pygame.mixer.Sound("assets/sounds/morte.mp3")  # Som de morte

    def reset_game(self):
        """Reseta o estado do jogo."""
        # Cria o jogador e os canos iniciais
        self.player = Player()
        self.pipes = [Pipe(SCREEN_WIDTH), Pipe(SCREEN_WIDTH + 400)]  # Inicializa dois canos
        self.score = 0  # Inicializa a pontuação
        self.running = True  # Define o estado de execução do jogo
        self.game_over_screen = None  # Inicializa a tela de Game Over

    def start_game(self):
        """Inicia o jogo a partir do zero."""
        self.reset_game()  # Reseta o jogo
        self.run_game()  # Inicia o loop principal do jogo

    def run_menu(self):
        """Exibe o menu inicial e espera pelo clique em um botão."""
        while True:
            self.menu.draw(self.screen)  # Desenha o menu
            action = self.menu.handle_events()  # Espera a interação do usuário com o menu
            if action == "play":
                self.start_game()  # Inicia o jogo se o botão 'play' for pressionado
                break
            elif action == "exit":
                pygame.quit()  # Sai do jogo se o botão 'exit' for pressionado
                sys.exit()     # encerra o jogo mais limpo

            pygame.display.update()  # Atualiza a tela
            self.clock.tick(FPS)  # Controla o FPS do jogo

    def run_game(self):
        """Executa o loop do jogo enquanto o estado de execução for verdadeiro."""
        while self.running:
            self.handle_events()  # Lida com os eventos do jogo
            self.update()         # Atualiza a lógica do jogo (movimento do pássaro e dos canos)
            self.draw()           # Desenha os elementos na tela
            self.clock.tick(FPS)  # Controla o FPS do jogo

        pygame.quit()  # Encerra o jogo

    def handle_events(self):
        """Lida com os eventos de teclado e clique do jogador."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Se a janela for fechada, encerra o jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()  # Faz o pássaro pular se a tecla espaço for pressionada
                    self.sound_jump.play()  # Toca o som de pulo

    def update(self):
        """Atualiza a posição do pássaro e os canos, verifica colisões e pontuação."""
        self.player.update()  # Atualiza a posição do jogador (loop de atualização)
        
        # Verifica se o pássaro tocou no chão ou no teto, gerando uma morte
        if self.player.y <= 0 or self.player.y + self.player.height >= SCREEN_HEIGHT:
            self.sound_morte.play()  # Toca o som de morte
            self.game_over()  # Chama a tela de Game Over
        
        # Atualiza a movimentação dos canos
        for pipe in self.pipes:
            pipe.move()  # Move o cano
            if pipe.x + pipe.width < 0:  # Se o cano saiu da tela
                pipe.reset_position()  # Reseta a posição do cano
                self.score += 1  # Aumenta a pontuação
                self.sound_score.play()  # Toca o som de pontuação
            if pipe.collide(self.player):  # Verifica se houve colisão entre o pássaro e o cano
                self.sound_morte.play()  # Toca o som de morte
                self.game_over()  # Chama a tela de Game Over

    def draw(self):
        """Desenha todos os elementos na tela."""
        self.screen.blit(self.background, (self.background_x, 0))  # Desenha o fundo
        for pipe in self.pipes:
            pipe.draw(self.screen)  # Desenha os canos
        self.player.draw(self.screen)  # Desenha o jogador (pássaro)
        
        # Exibe a pontuação na tela
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))  # Coloca a pontuação no canto superior esquerdo
        
        pygame.display.flip()  # Atualiza a tela

    def game_over(self):
        """Chama a tela de Game Over quando o jogo acaba."""
        self.game_over_screen = GameOverScreen(self.score)
        self.game_over_screen.draw(self.screen)  # Desenha a tela de Game Over
        pygame.display.update()  # Atualiza a tela
        self.handle_game_over()  # Lida com a escolha após o Game Over

    def handle_game_over(self):
        """Lida com a escolha do jogador após o Game Over."""
        while True:
            action = self.game_over_screen.handle_events()  # Espera a interação do jogador
            if action == "restart":
                self.start_game()  # Reinicia o jogo
                break
            elif action == "menu":
                self.run_menu()  # Volta ao menu principal
                break

    def run(self):
        """Inicia o jogo, mostrando o menu inicial e executando o loop principal do jogo."""
        self.run_menu()  # Exibe o menu inicial

# Garante que o bloco de código dentro dele só seja executado quando o script é executado diretamente.
if __name__ == "__main__": 
    game = Game()  # Cria uma instância do jogo
    game.run()  # Executa o jogo
