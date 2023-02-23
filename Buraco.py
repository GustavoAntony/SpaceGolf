import pygame 
import numpy as np


class Buraco(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Buraco, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.topleft = [pos[0]-20,pos[1]-20]
        self.radius = (self.surf.get_rect()[2])/2

    def acerto(self, ball):

        if  self.rect.colliderect(ball.rect):
            return True
        else :
            return False
