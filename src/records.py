import json
import os
import pygame
import sys
from src.config import SCREEN_WIDTH, SCREEN_HEIGHT

class Records:
    def __init__(self, filename="records.json"):
        """Inicializa a classe Records. Carrega os records de um arquivo JSON."""
        self.filename = filename  # Nome do arquivo onde os records serão armazenados
        self.records = self.load_records()  # Carrega os records existentes

    def load_records(self):
        """Carrega os records de um arquivo JSON, retornando uma lista de records."""
        if os.path.exists(self.filename):  # Verifica se o arquivo de records existe
            with open(self.filename, "r") as file:
                data = json.load(file)  # Carrega os dados JSON
                if isinstance(data, dict):  # Verifica se os dados carregados são um dicionário
                    return data.get("records", [])  # Retorna os records ou uma lista vazia se não houver
        return []  # Retorna uma lista vazia se o arquivo não existir ou for inválido

    def save_record(self, score):
        """Adiciona um novo score à lista de records e salva no arquivo JSON, mantendo apenas os 6 melhores."""
        self.records.append(score)  # Adiciona o novo score à lista de records
        self.records.sort(reverse=True)  # Ordena os records em ordem decrescente
        self.records = self.records[:6]  # Mantém apenas os 6 melhores records
        data = {"records": self.records}  # Estrutura os dados para serem salvos no arquivo JSON
        with open(self.filename, "w") as file:
            json.dump(data, file)  # Salva os dados no arquivo JSON

    def get_top_records(self, n=10):
        """Retorna os n melhores records. O valor padrão é 10."""
        return self.records[:n]  # Retorna os primeiros n records da lista

    def draw_button(self, screen, text, y_position, font_size=36):
        """Desenha um botão na tela com o texto fornecido e a posição especificada."""
        button_font = pygame.font.Font(None, font_size)  # Cria a fonte para o botão
        button_text = button_font.render(text, True, (0, 0, 0))  # Renderiza o texto do botão
        button_rect = pygame.Rect(
            SCREEN_WIDTH // 2 - 100, y_position - 25, 200, 50  # Calcula a posição e o tamanho do botão
        )
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Desenha o fundo branco do botão
        pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)  # Desenha a borda preta do botão
        text_rect = button_text.get_rect(center=button_rect.center)  # Centraliza o texto dentro do botão
        screen.blit(button_text, text_rect)  # Desenha o texto no botão
        return button_rect  # Retorna o retângulo do botão para verificação de cliques

    def show_records(self, screen):
        """Exibe os records na tela com um botão para voltar ao menu."""
        top_records = self.get_top_records()  # Obtém os melhores records

        while True:
            screen.fill((135, 206, 250))  # Cor de fundo azul claro 

            # Título "Recordes"
            font = pygame.font.Font(None, 74)  # Fonte maior para o título
            title = font.render("Recordes", True, (0, 0, 0))  # Renderiza o título "Recordes"
            screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, 50))  # Exibe o título na tela

            # Exibe os records
            font = pygame.font.Font(None, 36)  # Fonte para os records
            for i, record in enumerate(top_records):  # Itera sobre os records
                record_text = font.render(f"{i + 1}. {record}", True, (0, 0, 0))  # Renderiza cada record
                screen.blit(record_text, (SCREEN_WIDTH // 2 - record_text.get_width() // 2, 150 + i * 40))  # Exibe os records

            # Desenha o botão de "Menu"
            return_button_rect = self.draw_button(screen, "Menu", SCREEN_HEIGHT - 100)  # Desenha o botão
            pygame.display.flip()  # Atualiza a tela

            # Verifica eventos de clique ou pressionamento de tecla
            if self.handle_events(return_button_rect):  # Se o botão for clicado ou a tecla ESC for pressionada
                return  # Retorna para o menu

    def handle_events(self, return_button_rect):
        """Verifica os eventos e retorna True se o botão 'Menu' for clicado ou a tecla ESC for pressionada."""
        for event in pygame.event.get():  # Itera sobre os eventos
            if event.type == pygame.QUIT:  # Se o evento for o fechamento da janela
                pygame.quit()
                sys.exit()  # Fecha o Pygame e o programa
            if event.type == pygame.MOUSEBUTTONDOWN:  # Se um botão do mouse for pressionado
                if return_button_rect.collidepoint(event.pos):  # Verifica se o clique foi dentro do botão "Menu"
                    return True  # Retorna True se o botão foi clicado
            if event.type == pygame.KEYDOWN:  # Se uma tecla for pressionada
                if event.key == pygame.K_ESCAPE:  # Se a tecla ESC for pressionada
                    return True  # Retorna True se a tecla ESC foi pressionada
        return False  # Retorna False se nenhum evento válido ocorrer
