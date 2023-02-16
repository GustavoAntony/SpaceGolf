import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.pos = [350,450]
        self.velocity = [0, 0]
        self.color = (255, 255, 0)