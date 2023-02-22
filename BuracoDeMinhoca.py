import pygame 
import numpy as np


class BuracoDeMinhoca(pygame.sprite.Sprite):
    def __init__(self, entrada, saida):
        super(BuracoDeMinhoca, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect()
        self.entrada = entrada
        self.rect.topleft = entrada
        self.saida = saida
    def teleport(self, ball):

        if  self.rect.colliderect(ball.rect):
            ball.pos = self.saida
