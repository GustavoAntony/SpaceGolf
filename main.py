import pygame

pygame.init()

screen= pygame.display.set_mode((500,600))


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
    
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()