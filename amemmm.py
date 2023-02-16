import pygame
import math
import numpy as np
# Define a constante gravitacional (em m^3 / kg s^2)
G = 600

class Object:
    def __init__(self, mass, pos, vel, acc):
        self.mass = mass
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def update(self, dt):
        # Atualiza a posição e a velocidade do objeto
        c = np.empty_like(self.vel, dtype=int)
        b = self.acc * dt
        np.add(self.vel, b, out=c, casting='unsafe')
        self.vel = c

        c = np.empty_like(self.pos, dtype=int)
        b = self.vel * dt
        np.add(self.pos, b, out=c, casting='unsafe')
        self.pos = c


    def apply_force(self, force):
        # Aplica uma força ao objeto
        c = np.empty_like(self.acc, dtype=int)
        b = force / self.mass
        np.add(self.acc, b, out=c, casting='unsafe')
        self.acc =c 

    def distance_to(self, other):
        # Calcula a distância entre este objeto e outro objeto
        dx = other.pos[0] - self.pos[0]
        dy = other.pos[1] - self.pos[1]
        return math.sqrt(dx**2 + dy**2)

    def gravitational_force_from(self, other):
        # Calcula a força gravitacional entre este objeto e outro objeto
        dist = self.distance_to(other)
        force_magnitude = G * (self.mass * other.mass) / dist**2
        force_direction = (other.pos - self.pos) / dist
        force = force_direction * force_magnitude
        return force

# Inicializa o Pygame
pygame.init()

# Cria a janela do jogo
window = pygame.display.set_mode((800, 600))

# Cria dois objetos (por exemplo, planetas)
object1 = Object(mass=100, pos=np.array([200, 300]), vel=np.array([0, 0]), acc=np.array([0, 0]))
object2 = Object(mass=1000, pos=np.array([600, 300]), vel=np.array([0, 0]), acc=np.array([0, 0]))

# Loop principal do jogo
clock = pygame.time.Clock()
while True:
    # Processa os eventos do Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Calcula a força gravitacional entre os objetos
    force1 = object1.gravitational_force_from(object2)
    force2 = object2.gravitational_force_from(object1)

    # Aplica as forças aos objetos
    object1.apply_force(force1)
    object2.apply_force(force2)

    # Atualiza a posição dos objetos
    object1.update(0.01)
    object2.update(0.01)

    # Limpa a janela do jogo
    window.fill((0, 0, 0))

    # Desenha os objetos na janela do jogo
    pygame.draw.circle(window, (255, 255, 255), (int(object1.pos[0]), int(object1.pos[1])), 10)
    pygame.draw.circle(window, (255, 255, 255), (int(object2.pos[0]), int(object2.pos[1])), 20)

    # Atualiza a janela do jogo
    pygame.display.update()

    # Limita o número de quadros por segundo
    clock.tick(60)
