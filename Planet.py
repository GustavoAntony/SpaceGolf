import pygame

import numpy as np 


class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, pos):
        super(Planet, self).__init__()
        self.surf = pygame.Surface((mass, mass))
        self.rect = self.surf.get_rect()
        self.pos = pos
        self.rect.topleft = [pos[0]-(mass/2),pos[1]-(mass/2)]
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

        if  self.rect.colliderect(ball.rect):
            return True
        else :
            return False
