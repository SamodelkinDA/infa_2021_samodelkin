import pygame  
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
circle(screen, (200, 200, 200), (200, 200), 500)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (255, 0, 0), (150, 180), 15)
circle(screen, (255, 0, 0), (250, 180), 20)
rect(screen, (0, 0, 0), (195,165, 2,50))
rect(screen, (0, 0, 0), (150,250, 100,20))
polygon(screen, (0, 0, 0), [(180,170), (190,160), (110,130), (100,140)])
polygon(screen, (0, 0, 0), [(220,170), (210,160), (270,130), (280,140)])
circle(screen, (0, 0, 0), (150, 180), 5)
circle(screen, (0, 0, 0), (250, 180), 5)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()