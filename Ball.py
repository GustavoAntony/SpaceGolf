import pygame
import numpy as np 

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((20,20))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.pos = np.array([350,700])
        self.rect.topleft = [self.pos[0]-10,self.pos[1]-10]
        self.velocity = np.array([0, 0])
        self.color = (255, 255, 0)
        self.mass = 10
        self.launched = False
        self.lifes = 3
        self.radius = (self.surf.get_rect()[2])/2

    def pos_u (self):
        self.rect.topleft = self.pos()