import pygame
import numpy as np 

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.surf = pygame.Surface((50,50))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.pos = np.array([350,650])
        self.velocity = np.array([0, 0])
        self.color = (255, 255, 0)
        self.mass = 10
        self.launched = False