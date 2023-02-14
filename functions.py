import pygame
from Ball import Ball

screen= pygame.display.set_mode((1000,700))

def inicial_screen(running, window):
    window = "inicial"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window = "nivel_1"
        elif event.type == pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))
    pygame.display.update()
    return running, window
    
    
def game_screen(running, window):
    ball = Ball()
    while window == "nivel_1":
        for event in pygame.event.get():
            if event.type == pygame.K_0:
                ball.x += 100
            elif event.type == pygame.MOUSEBUTTONDOWN:
                window = "inicial"
            elif event.type == pygame.QUIT:
                running = False
                return running, False

        screen.fill((0,0,0))
        screen.blit(ball.surf,(ball.x,ball.y))
        # Update!
        pygame.display.update()

    return running, window