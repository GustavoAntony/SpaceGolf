import pygame

class Planet(pygame.sprite.Sprite):
    def __init__(self):
        super(Planet, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect()
