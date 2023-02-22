import pygame 
import numpy as np


class Buraco(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Buraco, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.topleft = pos
    def acerto(self, ball):

        if  self.rect.colliderect(ball.rect):
            return True
        else :
            return False
