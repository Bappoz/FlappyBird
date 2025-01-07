# Cópia Flappy Bird 🐦

Um jogo simples inspirado no clássico Flappy Bird, desenvolvido em Python usando a biblioteca Pygame.

------

## Como Jogar
O objetivo é controlar o pássaro para que ele passe pelos espaços entre os canos, evitando colisões. Cada cano ultrapassado aumenta sua pontuação.

- **Tecla de controle:** Pressione a tecla `Espaço` para fazer o pássaro pular.
- **Cuidado:** Não deixe o pássaro colidir com os canos, cair no chão ou colidir com o teto.

------

## Funcionalidades
- **Menu principal:** Escolha entre jogar ou sair.
- **Sistema de pontuação:** Pontos são incrementados toda vez que o pássaro ultrapassa um conjunto de canos.
- **Física do jogo:** Simulação de gravidade e pulo.
- **Animações e sons:**
  - Música de fundo.
  - Sons para eventos como pulo, pontuação e colisão.
- **Tela de Game Over:** Exibe a pontuação final e permite reiniciar ou voltar ao menu.

------

## Requisitos do Sistema
- **Python 3.8 ou superior**
- **Biblioteca Pygame**

------

## Como Executar
```bash
git clone https://github.com/Bappoz/FlappyBird.git
cd FlappyBird

pip install pygame #Instala o Pygame

python src/game.py #Executa o jogo
