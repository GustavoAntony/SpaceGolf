import pygame
import math

# Define as constantes necessárias
FORCE_MAX = 10.0
BALL_MASS = 1.0
INITIAL_VELOCITY = 5.0

# Inicializa o Pygame
pygame.init()

# Cria uma janela para o jogo
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bola em Movimento")

# Define a cor da bola
ball_color = (255, 255, 0)

# Define a posição inicial da bola
ball_pos = (400, 300)

# Define a velocidade inicial da bola
ball_velocity = (0, 0)

# Cria uma fonte para exibir a força aplicada
font = pygame.font.SysFont(None, 30)

# Loop principal do jogo
while True:
    # Processa os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
            start_pos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
            end_pos = pygame.mouse.get_pos()
            force_vector = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]
            force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
            force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
            ball_velocity = (force_normalized[0]*force_magnitude/BALL_MASS, force_normalized[1]*force_magnitude/BALL_MASS)

    # Limpa a janela
    window.fill((0, 0, 0))

    # Desenha a bola na posição atual
    pygame.draw.circle(window, ball_color, ball_pos, 10)

    # Exibe a força aplicada na tela
    force_text = font.render("Força: {:.2f}".format(ball_velocity[0]*BALL_MASS), True, (255, 255, 255))
    window.blit(force_text, (10, 10))

    # Atualiza a posição da bola de acordo com a velocidade
    ball_pos = (ball_pos[0] + ball_velocity[0], ball_pos[1] + ball_velocity[1])

    # Atualiza a janela
    pygame.display.update()