import pygame
from functions import *

pygame.init()
pygame.mixer.init()
# font = pygame.font.SysFont(None, 30)



running = True


# Music by <a href="https://pixabay.com/users/alexzavesa-24262182/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10714">AleXZavesa</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10714">Pixabay</a>

pygame.mixer.music.load("music/space-age-10714.mp3")
pygame.mixer.music.play(loops=-1)

window = "inicial"
while running:



    
    # Capturar eventos
    if window == "inicial":
        running,window = inicial_screen(running,window)
    elif window == "nivel_1":
        running,window = nivel_1(running,window)
    elif window == "nivel_2":
        running,window = nivel_2(running,window)
    elif window == "nivel_3":
        running,window = nivel_3(running,window)
    elif window == "nivel_4":
        running,window = nivel_4(running,window)
    # Update!

