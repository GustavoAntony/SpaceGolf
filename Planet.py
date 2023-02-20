import pygame

import numpy as np 


class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, pos):
        super(Planet, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect()
        self.mass = mass
        self.pos = pos
    def atract(self, other):


        # C = 1000
        # direcao_a = planeta - s[i]
        # d = np.linalg.norm(direcao_a)
        # direcao_a = direcao_a /d

        # mag_a = C / d**2
        # a = direcao_a * mag_a


        C = 100

        direction = (self.pos - other.pos)
        
        distance = np.linalg.norm(direction)


        direction = direction/distance

        if distance == 0 :
            magnitute = C/1
        else :
            magnitute = C/distance**2

        force = direction * magnitute
        

        return force