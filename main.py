import pygame
from Rocket import Rocket

pygame.init()

screen= pygame.display.set_mode((1000,700))


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    rocket = Rocket()
    screen.fill((0,0,0))
    screen.blit(rocket.surf,(500,350))
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()