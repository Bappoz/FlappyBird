import pygame
import sys
from src.player import Player  # Classe que gerencia o jogador
from src.pipe import Pipe  # Classe que gerencia os obstáculos (canos)
from src.power_up import PowerUp  # Classe que gerencia os power-ups
from src.menu import Menu  # Classe que gerencia o menu principal
from src.records import Records  # Classe para gerenciar recordes
from src.game_over import GameOverScreen  # Tela de Game Over
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS  # Configurações gerais do jogo

class Game:
    def __init__(self):
        pygame.init()  # Inicializa o pygame
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Define o tamanho da janela do jogo
        pygame.display.set_caption("Cópia Flappy Bird")  # Define o título da janela
        self.clock = pygame.time.Clock()  # Relógio para controlar a taxa de quadros
        self.background = pygame.image.load("assets/images/background.jpg").convert()  # Carrega o fundo do jogo
        self.background_x = 0  # Posição inicial do fundo (pode ser usada para criar efeito de rolagem)

        # Inicializa os módulos do jogo: menu e recordes
        self.menu = Menu()
        self.records = Records()
        self.reset_game()  # Configura o estado inicial do jogo

        # Carrega a música de fundo e sons
        pygame.mixer.music.load("assets/sounds/musica.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)  # Reproduz em loop

        # Carrega efeitos sonoros
        self.sound_jump = pygame.mixer.Sound("assets/sounds/audiojump.mp3")
        pygame.mixer.Sound.set_volume(self.sound_jump, 0.3)
        self.sound_score = pygame.mixer.Sound("assets/sounds/pontuacao.mp3")
        self.sound_death = pygame.mixer.Sound("assets/sounds/morte.mp3")
        self.sound_powerup = pygame.mixer.Sound("assets/sounds/powerup.mp3")
        pygame.mixer.Sound.set_volume(self.sound_powerup, 0.3)

    def reset_game(self):
        """Reinicia os parâmetros do jogo para começar uma nova partida."""
        self.player = Player()  # Cria o jogador
        self.pipes = [Pipe(SCREEN_WIDTH), Pipe(SCREEN_WIDTH + 400)]  # Inicializa dois canos
        self.power_ups = [PowerUp() for _ in range(2)]  # Adiciona dois power-ups na tela
        self.score = 0  # Reseta a pontuação
        self.running = True  # Define o estado do jogo como ativo
        self.game_over_screen = None  # Limpa a tela de Game Over anterior
        self.pipe_speed = 5  # Define a velocidade inicial dos canos

    def start_game(self):
        """Inicia o jogo após o menu principal."""
        self.reset_game()
        self.run_game()

    def run_menu(self):
        """Exibe o menu principal e aguarda a escolha do jogador."""
        while True:
            self.menu.draw(self.screen)  # Desenha o menu na tela
            action = self.menu.handle_events()  # Verifica as ações do menu
            if action == "play":
                self.start_game()  # Inicia o jogo
                break
            elif action == "records":
                self.menu_records()  # Mostra os recordes e retorna ao menu
                break
            elif action == "exit":
                pygame.quit()
                sys.exit()

            pygame.display.update()  # Atualiza a tela
            self.clock.tick(FPS)

    def menu_records(self):
        """Gerencia a transição de volta ao menu após visualizar os recordes."""
        self.records.show_records(self.screen)
        self.run_menu()

    def handle_events(self):
        """Lida com eventos, como teclas pressionadas."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # Sai do loop do jogo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Pula quando o jogador pressiona a barra de espaço
                    self.player.jump()
                    self.sound_jump.play()

    def update(self):
        """Atualiza os elementos do jogo (jogador, canos e power-ups)."""
        self.player.update()  # Atualiza a posição do jogador
        
        if self.player.y > SCREEN_HEIGHT or self.player.y < 0:  # Verifica colisão com os limites da tela
            self.sound_death.play()
            self.running = False
            
        # Atualiza os canos
        for pipe in self.pipes:
            pipe.x -= self.pipe_speed  # Move os canos para a esquerda
            if pipe.x + pipe.width < 0:  # Reposiciona o cano quando sai da tela
                pipe.reset_position()
                self.score += 1
                self.sound_score.play()
                # Aumenta a velocidade dos canos a cada número específico de pontos
                if self.score in {25, 50, 60, 75, 100, 115}:
                    self.pipe_speed += 1.5
                    for power_up in self.power_ups:
                        power_up.speed += 1.5
                    

            # Verifica colisão com o jogador
            if any(pipe_rect.colliderect(self.player.get_collision_rect()) for pipe_rect in pipe.get_collision_rect()):
                self.sound_death.play()
                self.running = False

        # Atualiza os power-ups
        for power_up in self.power_ups:
            power_up.update()
            if power_up.is_colliding_with_pipe(self.pipes):  # Reposiciona se colidir com um cano
                power_up.reset_position()
            if power_up.get_collision_rect().colliderect(self.player.get_collision_rect()) and not power_up.collected:
                power_up.collect()
                self.player.collect_power_up()  # Jogador coleta o power-up
                self.sound_powerup.play()
                self.score += 2  # Adiciona 2 pontos ao coletar um power-up

    def draw(self):
        """Desenha os elementos do jogo na tela."""
        self.screen.blit(self.background, (self.background_x, 0))  # Desenha o fundo
        
        # Desenha os canos e power-ups
        for pipe in self.pipes:
            pipe.draw(self.screen)
            
        for power_up in self.power_ups:
            power_up.draw(self.screen)
            
        self.player.draw(self.screen)  # Desenha o jogador
        
        # Exibe pontuação e contagem de power-ups
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        power_up_text = font.render(f"Golden Apple(+2p): {self.player.power_up_count}", True, (255, 255, 255))
        self.screen.blit(power_up_text, (10, 40))
        pygame.display.flip()

    def game_over(self):
        """Exibe a tela de Game Over e salva a pontuação."""
        self.records.save_record(self.score)  # Salva o recorde
        self.game_over_screen = GameOverScreen(self.score)  # Cria a tela de Game Over
        self.game_over_screen.draw(self.screen)  # Desenha a tela
        pygame.display.update()
        self.handle_game_over()  # Gerencia ações após Game Over

    def handle_game_over(self):
        """Gerencia as ações na tela de Game Over."""
        while True:
            action = self.game_over_screen.handle_events()
            if action == "restart":
                self.start_game()  # Reinicia o jogo
                break
            elif action == "menu":
                self.run_menu()  # Volta ao menu
                break

    def run(self):
        """Inicia o ciclo do jogo começando pelo menu principal."""
        self.run_menu()
        
    def run_game(self):
        """Loop principal do jogo."""
        while self.running:
            self.handle_events()  # Lida com eventos do jogador
            self.update()  # Atualiza o estado do jogo
            self.draw()  # Renderiza os elementos na tela
            self.clock.tick(FPS)  # Mantém a taxa de quadros

        self.game_over()  # Exibe a tela de Game Over quando o jogo termina

if __name__ == "__main__":
    game = Game()
    game.run()
