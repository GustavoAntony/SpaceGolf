import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Verifica se o botão direito do mouse está pressionado
    if pygame.mouse.get_pressed()[2]:
        print("Botão direito do mouse pressionado")

    window.fill((255, 255, 255))
    pygame.display.update()