import pygame
from functions import *

pygame.init()
pygame.mixer.init()


running = True


# Music by <a href="https://pixabay.com/users/alexzavesa-24262182/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10714">AleXZavesa</a> from <a href="https://pixabay.com//?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=10714">Pixabay</a>

# musica de fundo
pygame.mixer.music.load("music/space-age-10714.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(loops=-1)

window = "inicial"
while running:
    
    # Veirfica a tela que o usuário está para fazer a mudança de tela
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
    elif window == "gameover":
        running,window = game_over(running,window)
    elif window == "winner":
        running,window = winner(running,window)

