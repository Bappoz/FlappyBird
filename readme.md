# Cópia Flappy Bird 🐦

Um jogo simples inspirado no clássico Flappy Bird, desenvolvido em Python usando a biblioteca Pygame.

------

## Como Jogar
O objetivo é controlar o pássaro para que ele passe pelos espaços entre os canos, evitando colisões. Cada cano ultrapassado aumenta sua pontuação. Além disso, a cada maça dourada que o passáro pega é +2 pontos no score. 
Outra mecânica que aparece é que a velocidade é aumentada a partir de uma certa quantidade de pontos do score.

- **Tecla de controle:** Pressione a tecla `Espaço` para fazer o pássaro pular.
- **Cuidado:** Não deixe o pássaro colidir com os canos, cair no chão ou colidir com o teto.

------

## Recursos

- **Menu Principal:** Permite iniciar o jogo, visualizar recordes ou sair.
- **Jogo:** Controle o pássaro para evitar os canos e colete power-ups.
- **Power-Ups:** Coleta de power-ups que aumentam a pontuação.
- **Tela de Game Over:** Exibe a pontuação final e permite reiniciar ou voltar ao menu.
- **Recordes:** Exibe os 10 melhores recordes com opção de retornar ao menu.

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

## Descrição dos Arquivos
  - assets/: Contém imagens e sons usados no jogo.
  - src/: Contém o código-fonte do jogo.
  - config.py: Configurações do jogo, como largura e altura da tela.
  - game.py: Arquivo principal que inicia o jogo.
  - game_object.py: Classe base para objetos do jogo.
  - game_over.py: Tela de Game Over.
  - menu.py: Menu principal do jogo.
  - pipe.py: Implementação dos canos.
  - player.py: Implementação do jogador (pássaro).
  - power_up.py: Implementação dos power-ups.
  - records.py: Gerenciamento de recordes.
  - records.json: Arquivo JSON que armazena os recordes.
  - README.md: Este arquivo.

------
## Requisitos do Sistema
- **Python 3.8 ou superior**
- **Biblioteca Pygame**

------

## Como Executar
```bash
pip install pygame 
  # **pip install pygame**: Comando para instalar a biblioteca Pygame.
git clone https://github.com/Bappoz/FlappyBird.git
  # **git clone**: Comando para clonar o repositório do GitHub.
cd ../FlappyBird
  # **cd FlappyBird**: Comando para navegar até o diretório do projeto clonado.
python src/game.py 
  # **python src/game.py**: Comando para executar o jogo.
