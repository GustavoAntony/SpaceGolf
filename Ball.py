import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.x = 500
        self.y = 350