import pygame 
import numpy as np
import math


class BuracoDeMinhoca(pygame.sprite.Sprite):
    def __init__(self, entrada, saida):
        super(BuracoDeMinhoca, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.radius = (self.surf.get_rect()[2])/2
        self.rect = self.surf.get_rect()
        self.entrada = entrada
        self.rect.topleft = [entrada[0]-(50/2),entrada[1]-(50/2)]
        self.saida = saida


    def teleport(self, ball):

        x1 = self.entrada[0]
        x2 = ball.pos[0]
        y1 = self.entrada[1]
        y2 = ball.pos[1]


        distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if distancia <= (self.radius+ball.radius):
            ball.pos = self.saida