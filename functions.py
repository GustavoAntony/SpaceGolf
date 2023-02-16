import pygame
from Ball import Ball
import math
import numpy as np
HEIGHT = 900
WIDTH = 700
FORCE_MAX = 10.0
BALL_MASS = 1.0
INITIAL_VELOCITY = 0.3
screen= pygame.display.set_mode((WIDTH,HEIGHT))
# font = pygame.font.SysFont(None, 30)



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
    print ("nivel 1")
    while window == "nivel_1":

            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.QUIT:
                running = False
                return running, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
                start_pos = ball.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
                end_pos = pygame.mouse.get_pos()
                force_vector = [end_pos[0] - ball.pos[0], end_pos[1] - ball.pos[1]]
                force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
                force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
                ball.velocity = (force_normalized[0]*force_magnitude/BALL_MASS*0.003*(-1), force_normalized[1]*force_magnitude/BALL_MASS*(-1)*0.003)
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1])
        

        screen.fill((0,0,0))

        

        if pygame.mouse.get_pressed()[0]:
                
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(ball.pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        

            # Exibe a força aplicada na tela
            # force_text = font.render("Força: {:.2f}".format(ball_velocity[0]*BALL_MASS), True, (255, 255, 255))
            # screen.blit(force_text, (10, 10))

            

            # Atualiza a janela
            
            # screen.blit(ball.surf,(ball.pos[0],ball.pos[1]))
            # Update!
        pygame.draw.circle(screen, ball.color, ball.pos, 10)
        pygame.display.update()


    return running, window