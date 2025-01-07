import json
import os
import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class Records:
    def __init__(self, filename="records.json"):
        self.filename = filename
        self.records = self.load_records()

    def load_records(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data.get("records", [])
        return []

    def save_record(self, score):
        self.records.append(score)
        self.records.sort(reverse=True)
        self.records = self.records[:6]  # Mantém apenas os 6 melhores
        data = {
            "records": self.records
        }
        with open(self.filename, "w") as file:
            json.dump(data, file)

    def get_top_records(self, n=10):
        return self.records[:n]

    def draw_button(self, screen, text, y_position):
        button_font = pygame.font.Font(None, 36)  # Ajusta o tamanho da fonte
        button_text = button_font.render(text, True, (0, 0, 0))
        button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, y_position - 25, 200, 50
        )
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Fundo branco
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Borda preta
        text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, text_rect)
        return button_rect

    def show_records(self, screen):
        top_records = self.get_top_records()

        while True:
            screen.fill((0, 0, 0))

            font = pygame.font.Font(None, 74)
            title = font.render("Recordes", True, (255, 255, 255))
            screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))
            font = pygame.font.Font(None, 36)
            for i, record in enumerate(top_records):
                record_text = font.render(f"{i + 1}. {record}", True, (255, 255, 255))
                screen.blit(record_text, (SCREEN_WIDTH // 2 - record_text.get_width() // 2, 150 + i * 40))

            # Adiciona o botão de "Retornar ao Menu"
            return_button_rect = self.draw_button(screen, "Menu", SCREEN_HEIGHT - 100)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if return_button_rect.collidepoint(event.pos):
                        return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return