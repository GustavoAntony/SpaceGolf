import pygame
from functions import *

pygame.init()
# font = pygame.font.SysFont(None, 30)



running = True

window = "inicial"
while running:

    # Capturar eventos
    if window == "inicial":

        running,window = inicial_screen(running,window)
    elif window == "nivel_1":
        running,window = nivel_1(running,window)
    # Update!

