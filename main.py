import pygame
from Ball import Ball

pygame.init()

screen= pygame.display.set_mode((1000,700))


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    ball = Ball()
    screen.fill((0,0,0))
    screen.blit(ball.surf,(500,350))
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()