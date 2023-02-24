import pygame
from Ball import Ball
from Planet import Planet
from Buraco import Buraco
from BuracoDeMinhoca import BuracoDeMinhoca
import math
import numpy as np
import sys
HEIGHT = 900
WIDTH = 700
FORCE_MAX = 10.0
BALL_MASS = 1.0
INITIAL_VELOCITY = 0.3
import random


screen= pygame.display.set_mode((WIDTH,HEIGHT))

# CARREGANDO TODAS AS IMAGENS E AUDIOS DO GAME
background_inicial = pygame.image.load("images\space_golf.png")
background_tutorial = pygame.image.load("images\load_tutorial.jpg")
levels_background = pygame.image.load("images\levels_background.jpg")
ball_jpg = pygame.image.load("images\golf_ball.png")
small_planet = pygame.image.load("images/small_planet.png")
big_planet = pygame.image.load("images/big_planet.png")
terra = pygame.image.load("images/terra.png")
venus = pygame.image.load("images/venus.png")
flag = pygame.image.load("images/flag.png")
wormhole = pygame.image.load("images\wormhole.png")
game_over_jpg = pygame.image.load("images\gameover.jpg")
winner_jpg = pygame.image.load("images/winner.jpg")

pygame.mixer.init()

coin_sound = pygame.mixer.Sound("music/success-fanfare-trumpets-6185.wav")
batida = pygame.mixer.Sound("music/hurt_c_08-102842.mp3")
# Sound Effect from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=music&amp;utm_content=98269">Pixabay</a>
#TELA INICIAL





#Tela inicial
def inicial_screen(running, window):
    window = 'inicial'

    pygame.init()

    #Cria tela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))


    # Botoes da tela inicial
    start_button = pygame.Rect(170, 375, 360, 110)
    tutorial_button = pygame.Rect(217,572,265,81)
    exit_button = pygame.Rect(217,691,265,81)

    # Loop que tem em cada tela do game
    while window == "inicial":


        # Captura eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



            # Captura evento de tecla para baixo
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_ENTER or event.key == pygame.K_RETURN:
                    window = "nivel_2"

            # Captura evento de click de mouse 
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_2"
                elif tutorial_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_1"
                elif exit_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    pygame.quit()
                    sys.exit()

        # Pinta fundo
        screen.blit(background_inicial, (0,0))


        #Atualiza a tela
        pygame.display.update()

    return True, window
    
# Fução que roda a fase 1 
def nivel_1(running, window):
    ball = Ball()
    planets = []
    buraco = Buraco(np.array([WIDTH/2,360]))
    back_button = pygame.Rect(40,789,200,63)
    

    # Validação para verificar se o toque foi na tela atual
    toque_valido = False
    start_pos = ball.pos

    while window == "nivel_1":
        if ball.lifes == 0:
            window = "gameover"
            break


        #Verifica colisão na parede e nos planetas e cria gatilho para caso ele tenha apenas uma vida dê game over.
        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes == 1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()

        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()

        #Verifica acerto no buraco
        if buraco.acerto(ball):
            # Faz som de acerto
            coin_sound.play()
            window = "nivel_2"
            
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
                if back_button.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="inicial"
                    break
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
                ball.lifes -= 1
            elif event.type == pygame.MOUSEBUTTONUP:
                toque_valido = True


        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        

        
        # Pinta fundo
        screen.blit(background_tutorial,(0,0))
        if pygame.mouse.get_pressed()[0]:
            #desenha a linha que representa o vetor no qual será lançada a bolinha
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        #adiciona os elementos da tela (bola, bandeira, planetas e vidas)
        screen.blit(flag,buraco.pos+np.array([-(buraco.radius),-(buraco.radius)]))

        screen.blit(ball_jpg,ball.pos+np.array([-(ball.radius),-(ball.radius)]))
        for planet in planets:
            screen.blit(small_planet,planet.pos+np.array([-(planet.radius),-(planet.radius)]))

        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes-1):
            screen.blit(ball_jpg,pos_lifebar+np.array([-(ball.radius),-(ball.radius)]))
            pos_lifebar += np.array([30,0])


        #Atualiza a tela
        pygame.display.update()


    return running, window



# Funcão que roda a fase 2
def nivel_2(running, window):
    #Criando os objetos da fase
    ball = Ball()
    planets = [Planet(100, np.array([WIDTH/2,HEIGHT/2]), small_planet)]
    buraco = Buraco(np.array([WIDTH/2,60]))
    # Validação para verificar se o toque foi na tela atual
    toque_valido = False
    start_pos = ball.pos


    while window == "nivel_2":
        if ball.lifes == 0:
            window = "gameover"
            break


        #Verifica colisão na parede e nos planetas e cria gatilho para caso ele tenha apenas uma vida dê game over.
        
        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.launched = False
                if ball.lifes ==1 :
                    ball.lifes = 0
                # Faz som de colisão    
                batida.play()

        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()

        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()


        #Verifica acerto no buraco
        if buraco.acerto(ball):
            # Faz som de acerto
            coin_sound.play()
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
                ball.lifes -= 1
            elif event.type == pygame.MOUSEBUTTONUP:
                toque_valido = True

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        
        # Pinta fundo
        screen.blit(levels_background, (0,0))
        

        
        if pygame.mouse.get_pressed()[0]:
            #desenha a linha que representa o vetor no qual será lançada a bolinha
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        #adiciona os elementos da tela (bola, bandeira, planetas e vidas)
        screen.blit(ball_jpg,ball.pos+np.array([-(ball.radius),-(ball.radius)]))
        screen.blit(flag,buraco.pos+np.array([-(buraco.radius),-(buraco.radius)]))
        for planet in planets:

            screen.blit(planet.image,planet.pos+np.array([-(planet.radius),-(planet.radius)]))

        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes-1):
            screen.blit(ball_jpg,pos_lifebar+np.array([-(ball.radius),-(ball.radius)]))
            pos_lifebar += np.array([30,0])


        #Atualiza a tela
        pygame.display.update()



    return running, window




# Função da fase 3

def nivel_3(running, window):
    #Criando os objetos da fase
    ball = Ball()
    planets = [Planet(300, np.array([WIDTH/2,HEIGHT/2]),big_planet)]
    buraco = Buraco(np.array([WIDTH/2,60]))
    minhoca = BuracoDeMinhoca(np.array([ball.pos[0]+100,ball.pos[1]]), np.array([200,60]))

    start_pos = ball.pos

    while window == "nivel_3":
        if ball.lifes == 0:
            window = "gameover"
            break


        #Verifica colisão na parede e nos planetas e cria gatilho para caso ele tenha apenas uma vida dê game over.
        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.launched = False
                if ball.lifes ==1 :
                    ball.lifes = 0
                # Faz som de colisão   
                batida.play()

        if ball.pos[0]> WIDTH-20 or ball.pos[0] < 20:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()

        if ball.pos[1]> HEIGHT-20 or ball.pos[1] < 20 :
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()


        minhoca.teleport(ball)


        #Verifica acerto
        if buraco.acerto(ball):
            # Faz som de acerto
            coin_sound.play()
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
                ball.lifes -= 1

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        
        # Pinta fundo
        screen.blit(levels_background, (0,0))
        

        
        if pygame.mouse.get_pressed()[0]:
            #desenha a linha que representa o vetor no qual será lançada a bolinha
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        #adiciona os elementos da tela (bola, bandeira, planetas e vidas)
        screen.blit(ball_jpg,ball.pos+np.array([-(ball.radius),-(ball.radius)]))
        screen.blit(flag,buraco.pos+np.array([-(buraco.radius),-(buraco.radius)]))
        screen.blit(wormhole,minhoca.entrada+np.array([-(minhoca.radius),-(minhoca.radius)]))
        screen.blit(wormhole,minhoca.saida+np.array([-(minhoca.radius),-(minhoca.radius)]))
        for planet in planets:
            screen.blit(planet.image,planet.pos+np.array([-(planet.radius),-(planet.radius)]))
        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes-1):
            screen.blit(ball_jpg,pos_lifebar+np.array([-(ball.radius),-(ball.radius)]))
            pos_lifebar += np.array([30,0])

        #Atualiza a tela
        pygame.display.update()



    return running, window


#Função da fase 4
def nivel_4(running, window):
    #Criando objetos da fase
    ball = Ball()
    planets = [Planet(222, np.array([181,520]),terra),Planet(206, np.array([512,324]),venus)]
    buraco = Buraco(np.array([586,115]))

    start_pos = ball.pos

    while window == "nivel_4":
        if ball.lifes == 0:
            window = "gameover"
            break


        #Verifica colisão na parede e nos planetas e cria gatilho para caso ele tenha apenas uma vida dê game over.
        for planet in planets :

            if planet.colidiu(ball):
                ball.pos = np.array([350,650])
                ball.velocity = np.array([0, 0])
                ball.launched = False
                if ball.lifes ==1 :
                    ball.lifes = 0
                # Faz som de colisão    
                batida.play()

        if ball.pos[0]> WIDTH-ball.radius or ball.pos[0] < ball.radius:
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()

        if ball.pos[1]> HEIGHT-ball.radius or ball.pos[1] < ball.radius :
            ball.pos = np.array([350,650])
            ball.velocity = np.array([0, 0])
            ball.launched = False
            if ball.lifes ==1 :
                ball.lifes = 0
            # Faz som de colisão    
            batida.play()


        #Verifica acerto
        if buraco.acerto(ball):
            # Faz som de acerto
            coin_sound.play()
            window = "winner"
            
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
                ball.lifes -= 1

        
        # Atualiza a posição da bola de acordo com a velocidade
        ball.pos = (ball.pos[0] + ball.velocity[0], ball.pos[1] + ball.velocity[1]) 
        ball.rect.topleft = ball.pos

        if ball.launched:

            for planet in planets :
                ball.velocity = ball.velocity + planet.atract(ball)
                ball.pos = ball.pos + ball.velocity*0.001
        
        # Pinta fundo
        screen.blit(levels_background, (0,0))
        

        
        if pygame.mouse.get_pressed()[0]:
            #desenha a linha que representa o vetor no qual será lançada a bolinha   
            start_pos2 = np.array(pygame.mouse.get_pos())
            endpos2 = ball.pos+(start_pos-start_pos2)
            pygame.draw.line(surface= screen, color='white', start_pos= (ball.pos),end_pos=endpos2)
        
        #adiciona os elementos da tela (bola, bandeira, planetas e vidas)
        screen.blit(ball_jpg,ball.pos+np.array([-(ball.radius),-(ball.radius)]))
        screen.blit(flag,buraco.pos+np.array([-(buraco.radius),-(buraco.radius)]))

        for planet in planets:
            screen.blit(planet.image,planet.pos+np.array([-(planet.radius),-(planet.radius)]))
        pos_lifebar = np.array([550,830])
        for i in range(ball.lifes-1):
            screen.blit(ball_jpg,pos_lifebar+np.array([-(ball.radius),-(ball.radius)]))
            pos_lifebar += np.array([30,0])

        #Atualiza a tela
        pygame.display.update()


    return running, window


# Função da tela de game over
def game_over(running, window):
    rect_exit = pygame.Rect(229,625,259,84)
    rect_restart = pygame.Rect(182,457,351,116)
    while window == "gameover":
        screen.blit(game_over_jpg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_exit.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    return False,False
                if rect_restart.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_2"
            elif event.type == pygame.QUIT:
                return False, False
            

        #Atualiza a tela
        pygame.display.update()
    return running,window


# Função da tela de vitória
def winner(running, window):
    rect_exit = pygame.Rect(229,625,259,84)
    rect_restart = pygame.Rect(182,457,351,116)
    while window == "winner":
        screen.blit(winner_jpg, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_exit.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    return False,False
                if rect_restart.colliderect(pygame.Rect(pygame.mouse.get_pos(),(1,1))):
                    window ="nivel_2"
            elif event.type == pygame.QUIT:
                return False, False
            
        #Atualiza a tela
        pygame.display.update()
    return running,window




