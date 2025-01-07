import pygame
import sys
from src.player import Player
from src.pipe import Pipe
from src.power_up import PowerUp
from src.menu import Menu
from src.records import Records
from src.game_over import GameOverScreen
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Cópia Flappy Bird")
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/images/background.jpg").convert()
        self.background_x = 0

        self.menu = Menu()
        self.records = Records()
        self.reset_game()

        pygame.mixer.music.load("assets/sounds/musica.mp3")
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)

        self.sound_jump = pygame.mixer.Sound("assets/sounds/audiojump.mp3")
        pygame.mixer.Sound.set_volume(self.sound_jump, 0.3)
        self.sound_score = pygame.mixer.Sound("assets/sounds/pontuacao.mp3")
        self.sound_death = pygame.mixer.Sound("assets/sounds/morte.mp3")
        self.sound_powerup = pygame.mixer.Sound("assets/sounds/powerup.mp3")
        pygame.mixer.Sound.set_volume(self.sound_powerup, 0.3)

    def reset_game(self):
        self.player = Player()
        self.pipes = [Pipe(SCREEN_WIDTH), Pipe(SCREEN_WIDTH + 400)]
        self.power_ups = [PowerUp() for _ in range(2)]  # Adiciona dois PowerUps
        self.score = 0
        self.running = True
        self.game_over_screen = None
        self.pipe_speed = 5  # Velocidade inicial dos canos

    def start_game(self):
        self.reset_game()
        self.run_game()

    def run_menu(self):
        while True:
            self.menu.draw(self.screen)
            action = self.menu.handle_events()
            if action == "play":
                self.start_game()
                break
            elif action == "records":
                self.handle_back_to_menu()
                break
            elif action == "exit":
                pygame.quit()
                sys.exit()

            pygame.display.update()
            self.clock.tick(FPS)

    def handle_back_to_menu(self):
        self.records.show_records(self.screen)
        self.run_menu()

    def run_game(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        self.game_over()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.jump()
                    self.sound_jump.play()

    def update(self):
        self.player.update()
        if self.player.y > SCREEN_HEIGHT or self.player.y < 0:
            self.sound_death.play()
            self.running = False
            
        for pipe in self.pipes:
            pipe.x -= self.pipe_speed
            if pipe.x + pipe.width < 0:
                pipe.reset_position()
                self.score += 1
                self.sound_score.play()
                # Aumenta a velocidade do jogo conforme o jogador passa por um número específico de canos
                if self.score == 25 or self.score == 50 or self.score == 60 or self.score == 75 or self.score == 100:
                    self.pipe_speed += 1

            if any(pipe_rect.colliderect(self.player.get_collision_rect()) for pipe_rect in pipe.get_collision_rect()):
                self.sound_death.play()
                self.running = False

        for power_up in self.power_ups:
            power_up.update()
            if power_up.is_colliding_with_pipe(self.pipes):
                power_up.reset_position()
            if power_up.get_collision_rect().colliderect(self.player.get_collision_rect()) and not power_up.collected:
                power_up.collect()
                self.player.collect_power_up()
                self.sound_powerup.play()
                self.score += 2  # Aumenta a pontuação em 2 ao coletar um power-up

    def draw(self):
        self.screen.blit(self.background, (self.background_x, 0))
        
        # Polimorfismo: chamando o método draw em diferentes tipos de objetos
        for pipe in self.pipes:
            pipe.draw(self.screen)
        for power_up in self.power_ups:
            power_up.draw(self.screen)
        self.player.draw(self.screen)
        
        # Desenha a pontuação e a contagem de power-ups coletados na tela
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
        power_up_text = font.render(f"Golden Apple(+2p): {self.player.power_up_count}", True, (255, 255, 255))
        self.screen.blit(power_up_text, (10, 40))
        pygame.display.flip()

    def game_over(self):
        self.records.save_record(self.score)
        self.game_over_screen = GameOverScreen(self.score)
        self.game_over_screen.draw(self.screen)
        pygame.display.update()
        self.handle_game_over()

    def handle_game_over(self):
        while True:
            action = self.game_over_screen.handle_events()
            if action == "restart":
                self.start_game()
                break
            elif action == "menu":
                self.run_menu()
                break

    def run(self):
        self.run_menu()

if __name__ == "__main__":
    game = Game()
    game.run()