import pygame 
import numpy as np
import math


class Buraco(pygame.sprite.Sprite):
    def __init__(self, pos):
        super(Buraco, self).__init__()
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.topleft = [pos[0]-20,pos[1]-20]
        self.radius = (self.surf.get_rect()[2])/2

    def acerto(self, ball):

        x1 = self.pos[0]
        x2 = ball.pos[0]
        y1 = self.pos[1]
        y2 = ball.pos[1]


        distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if distancia <= (self.radius+ball.radius):
            return True
        else :
            return False
