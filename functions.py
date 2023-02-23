import pygame
from Ball import Ball
from Planet import Planet
from Buraco import Buraco
from BuracoDeMinhoca import BuracoDeMinhoca
import math
import numpy as np
from Button import Button
import pygame
import sys
HEIGHT = 900
WIDTH = 700
FORCE_MAX = 10.0
BALL_MASS = 1.0
INITIAL_VELOCITY = 0.3

screen= pygame.display.set_mode((WIDTH,HEIGHT))
# font = pygame.font.SysFont(None, 30)
background_inicial = pygame.image.load("images\space_golf.png")
background_tutorial = pygame.image.load("images\load_tutorial.jpg")
ball_jpg = pygame.image.load("images\golf_ball.png")


#TELA INICIAL
def inicial_screen(running, window):
    window = 'inicial'

    pygame.init()

    screen_width = 700
    screen_height = 900


    screen = pygame.display.set_mode((screen_width, screen_height))

    start_button = pygame.Rect(170, 375, 360, 110)
    tutorial_button = pygame.Rect(217,572,265,81)
    exit_button = pygame.Rect(217,691,265,81)

    font = pygame.font.Font(None, 36)


    while window == "inicial":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    print("Botão Start clicado!")
                    window = "nivel_2"
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
                if start_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_2"
                elif tutorial_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_1"
                elif exit_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    pygame.quit()
                    sys.exit()


        screen.blit(background_inicial, (0,0))
        pygame.display.update()

    return True, window
    
    
def nivel_1(running, window):
    ball = Ball()
    planets = []
    buraco = Buraco(np.array([WIDTH/2,360]))


    print(ball.surf.get_rect())
    toque_valido = False
    start_pos = ball.pos

    print ("nivel 1")
    while window == "nivel_1":
        if ball.lifes == 0:
            window = "inicial"
            break


        
        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.lifes -=1
            ball.launched = False
        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.lifes -= 1
            ball.velocity = np.array([0, 0])
            ball.launched = False


        if buraco.acerto(ball):
            window = "inicial"
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.QUIT:
                running = False
                return running, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
                start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP and toque_valido == True:
                # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
                end_pos = pygame.mouse.get_pos()
                force_vector = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]
                if force_vector == [0,0] :
                    force_vector = [1,1]
                force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
                force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
                ball.velocity = [force_normalized[0]*force_magnitude/BALL_MASS*0.003*(-1), force_normalized[1]*force_magnitude/BALL_MASS*(-1)*0.003]
                ball.launched = True
            elif event.type == pygame.MOUSEBUTTONUP:
                toque_valido = True

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        

        

        screen.blit(background_tutorial,(0,0))
        if pygame.mouse.get_pressed()[0]:
            
                
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        pygame.draw.circle(screen, ball.color, buraco.pos, buraco.radius)
        screen.blit(ball_jpg,ball.pos+np.array([-(ball.radius),-(ball.radius)]))
        for planet in planets:
            pygame.draw.circle(screen, ball.color, planet.pos, 50)
        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes):
            pygame.draw.circle(screen, (200,150,200), pos_lifebar, 10)
            pos_lifebar += np.array([30,0])
        
        pygame.display.update()


    return running, window





def nivel_2(running, window):
    ball = Ball()
    planets = [Planet(100, np.array([WIDTH/2,HEIGHT/2]))]
    buraco = Buraco(np.array([WIDTH/2,60]))
    toque_valido = False
    start_pos = ball.pos


    print ("nivel 2")
    while window == "nivel_2":
        if ball.lifes == 0:
            window = "inicial"
            break
        
        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.lifes -=1
                ball.launched = False



        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.lifes -=1
            ball.launched = False
        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.lifes -= 1
            ball.velocity = np.array([0, 0])
            ball.launched = False

        
        if buraco.acerto(ball):
            window = "nivel_3"
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.QUIT:
                running = False
                return running, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
                start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP and toque_valido == True:
                # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
                end_pos = pygame.mouse.get_pos()
                force_vector = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]
                if force_vector == [0,0] :
                    force_vector = [1,1]
                force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
                force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
                ball.velocity = [force_normalized[0]*force_magnitude/BALL_MASS*0.003*(-1), force_normalized[1]*force_magnitude/BALL_MASS*(-1)*0.003]
                ball.launched = True
            elif event.type == pygame.MOUSEBUTTONUP:
                toque_valido = True

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        

        screen.fill((0,0,0))

        
        if pygame.mouse.get_pressed()[0]:
            
                
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        pygame.draw.circle(screen, ball.color, ball.pos, ball.radius)
        pygame.draw.circle(screen, ball.color, buraco.pos, buraco.radius)
        for planet in planets:
            pygame.draw.circle(screen, ball.color, planet.pos, planet.radius)
        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes):
            pygame.draw.circle(screen, (200,150,200), pos_lifebar, 10)
            pos_lifebar += np.array([30,0])
        pygame.display.update()



    return running, window






def nivel_3(running, window):
    ball = Ball()
    planets = [Planet(300, np.array([WIDTH/2,HEIGHT/2]))]
    buraco = Buraco(np.array([WIDTH/2,60]))
    minhoca = BuracoDeMinhoca(np.array([ball.pos[0]+100,ball.pos[1]]), np.array([200,60]))

    start_pos = ball.pos

    print ("nivel 3")
    while window == "nivel_3":
        if ball.lifes == 0:
            window = "inicial"
            break



        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.lifes -=1
                ball.launched = False


        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.lifes -=1
            ball.launched = False
        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.lifes -= 1
            ball.velocity = np.array([0, 0])
            ball.launched = False

        minhoca.teleport(ball)

        if buraco.acerto(ball):
            window = "nivel_4"
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.QUIT:
                running = False
                return running, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
                start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
                end_pos = pygame.mouse.get_pos()
                force_vector = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]
                if force_vector == [0,0] :
                    force_vector = [1,1]
                force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
                force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
                ball.velocity = [force_normalized[0]*force_magnitude/BALL_MASS*0.003*(-1), force_normalized[1]*force_magnitude/BALL_MASS*(-1)*0.003]
                ball.launched = True

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        

        screen.fill((0,0,0))

        
        if pygame.mouse.get_pressed()[0]:
            
                
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        pygame.draw.circle(screen, ball.color, ball.pos, ball.radius)
        pygame.draw.circle(screen, ball.color, buraco.pos, buraco.radius)
        pygame.draw.circle(screen, "blue", minhoca.entrada, minhoca.radius)
        pygame.draw.circle(screen, "red", minhoca.saida, minhoca.radius)
        for planet in planets:
            pygame.draw.circle(screen, ball.color, planet.pos, planet.radius)
        pygame.display.update()


    return running, window







def nivel_4(running, window):
    ball = Ball()
    planets = [Planet(222, np.array([181,520])),Planet(206, np.array([512,324]))]
    buraco = Buraco(np.array([586,115]))

    start_pos = ball.pos

    print ("nivel 4")
    while window == "nivel_4":
        if ball.lifes == 0:
            window = "inicial"
            break



        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.lifes -=1
                ball.launched = False


        if ball.pos[0]> WIDTH-ball.radius or ball.pos[0] < ball.radius:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.lifes -=1
            ball.launched = False
        if ball.pos[1]> HEIGHT-ball.radius or ball.pos[1] < ball.radius :
            ball.pos = np.array([350,650])
            ball.lifes -= 1
            ball.velocity = np.array([0, 0])
            ball.launched = False


        if buraco.acerto(ball):
            window = "inicial"
            
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    ball.pos[0] += 100
            elif event.type == pygame.QUIT:
                running = False
                return running, False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            # Quando o mouse é pressionado, armazena a posição inicial
                start_pos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                # Quando o mouse é solto, calcula a força e a velocidade e aplica na bola
                end_pos = pygame.mouse.get_pos()
                force_vector = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]
                if force_vector == [0,0] :
                    force_vector = [1,1]
                force_magnitude = min(math.sqrt(force_vector[0]**2 + force_vector[1]**2), FORCE_MAX)
                force_normalized = [force_vector[0]/force_magnitude, force_vector[1]/force_magnitude]
                ball.velocity = [force_normalized[0]*force_magnitude/BALL_MASS*0.003*(-1), force_normalized[1]*force_magnitude/BALL_MASS*(-1)*0.003]
                ball.launched = True

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        

        screen.fill((0,0,0))

        
        if pygame.mouse.get_pressed()[0]:
            
                
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        pygame.draw.circle(screen, ball.color, ball.pos, ball.radius)
        pygame.draw.circle(screen, ball.color, buraco.pos, buraco.radius)
        for planet in planets:
            pygame.draw.circle(screen, ball.color, planet.pos, planet.radius)
        pygame.display.update()


    return running, window