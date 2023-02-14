import pygame
from functions import *

pygame.init()


running = True
window = "inicial"
while running:

    # Capturar eventos
    if window == "inicial":
        running,window = inicial_screen(running,window)
    elif window == "nivel_1":
        running,window = nivel_1(running,window)
    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()

