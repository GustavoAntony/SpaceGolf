import pygame

import numpy as np 
import math

class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, pos):
        super(Planet, self).__init__()
        self.surf = pygame.Surface((mass, mass))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.topleft = [self.pos[0]-(mass/2),self.pos[1]-(mass/2)]
        self.radius = (self.surf.get_rect()[2])/2
        self.mass = mass

    def atract(self, other):

        C = other.mass*self.mass*0.01

        direction = (self.pos - other.pos)
        
        distance = np.linalg.norm(direction)


        modulo = direction/distance

        if distance == 0 :
            magnitute = C/1
        else :
            magnitute = C/distance**2

        force = modulo * magnitute
        

        return force
    

    def colidiu(self, ball):

        x1 = self.pos[0]
        x2 = ball.pos[0]
        y1 = self.pos[1]
        y2 = ball.pos[1]


        distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        if distancia <= (self.radius+ball.radius):
            return True
        else :
            return False
