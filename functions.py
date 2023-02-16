import pygame
from Ball import Ball

HEIGHT = 900
WIDTH = 700
screen= pygame.display.set_mode((WIDTH,HEIGHT))


#TELA INICIAL
def inicial_screen(running, window):
    window = "inicial"
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            window = "nivel_1"
        elif event.type == pygame.QUIT:
            running = False
    
        screen.fill((0,0,0))
        pygame.display.update()
    return running, window
    
    
def nivel_1(running, window):
    ball = Ball()
    while window == "nivel_1":
        ball.pos[0] += 0.02
        ball.pos[1] += 0.01
        if (ball.pos[0] > WIDTH or ball.pos[0] <0 )or (ball.pos[1] > HEIGHT or ball.pos[1] < 0):
            ball.pos[0] = WIDTH/2
            ball.pos[1] = HEIGHT/2
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.MOUSEBUTTONDOWN:
                window = "inicial"
            elif event.type == pygame.QUIT:
                running = False
                return running, False

        screen.fill((0,0,0))
        screen.blit(ball.surf,(ball.pos[0],ball.pos[1]))
        # Update!
        pygame.display.update()

    return running, window