import pygame
from Ball import Ball
from Button import Button

HEIGHT = 900
WIDTH = 700
screen= pygame.display.set_mode((WIDTH,HEIGHT))


#TELA INICIAL
def inicial_screen(running, window):
    window = 'inicial'
    import pygame
    import sys

    pygame.init()

    screen_width = 700
    screen_height = 900
    background_color = (255, 255, 255)

    screen = pygame.display.set_mode((screen_width, screen_height))

    start_button_width = 200
    start_button_height = 50
    start_button_x = (screen_width - start_button_width) // 2
    start_button_y = screen_height // 2 - 50
    start_button = pygame.Rect(start_button_x, start_button_y, start_button_width, start_button_height)

    exit_button_width = 200
    exit_button_height = 50
    exit_button_x = (screen_width - exit_button_width) // 2
    exit_button_y = screen_height // 2 +25
    exit_button = pygame.Rect(exit_button_x, exit_button_y, exit_button_width, exit_button_height)

    font = pygame.font.Font(None, 36)
    start_text = font.render("Start", True, (0, 0, 0))
    exit_text = font.render("Sair", True, (0, 0, 0))

    while window == "inicial":
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and start_button.collidepoint(event.pos):
                print("Botão Start clicado!")
                window = "nivel_1"

            if event.type == pygame.MOUSEBUTTONDOWN and exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        screen.fill(background_color)
        pygame.draw.rect(screen, (255, 0, 0), start_button) # desenha o botão "Start"
        pygame.draw.rect(screen, (255, 0, 0), exit_button) # desenha o botão "Sair"
        screen.blit(start_text, (start_button.x + 70, start_button.y + 15)) # desenha o texto "Start"
        screen.blit(exit_text, (exit_button.x + 80, exit_button.y + 15)) # desenha o texto "Sair"
        pygame.display.update()

    return True, window
    
    
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