"""Эта программа рисует красивые картинки.
   На данный момент она может нарисовать далеких птиц и
   глаз, плавник рыбы
"""


import pygame
import numpy
from pygame import draw  
from pygame.draw import *

def draw_bird(x_bird, y_bird, size_of_bird, angle_of_bird):
    bird_surface = pygame.Surface((size_of_bird*2, size_of_bird), pygame.SRCALPHA)
    bird_surface.fill((0, 0, 0, 0))
    arc(bird_surface, (255, 255, 255), 
        [size_of_bird, 0, size_of_bird, size_of_bird/2],
        numpy.pi/2, numpy.pi, 3)
    arc(bird_surface, (255, 255, 255), 
        [0, 0, size_of_bird, size_of_bird/2], 
        0, numpy.pi / 2, 3)
    screen.blit(pygame.transform.rotate(bird_surface, angle_of_bird), (x_bird - size_of_bird, y_bird))
    return


def fishs_fin(fin_size, fin_tetta, fin_flip_bool):
    fish_fin_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    fish_fin_surface.fill((0, 0, 0, 0))
    massive_fish_fin=[(120, 180), (130, 165), (137, 150), (142, 135),
                      (145, 120), (148, 110), (150, 90), (145, 70),
                      (140, 60), (40, 60), (50, 65), (60, 72), (70, 81),
                      (80, 91),(90, 102),(100, 114),(110, 135), 
                      (115, 155)]
    polygon(fish_fin_surface, (200,100,100), massive_fish_fin)
    polygon(fish_fin_surface, (0,0,0), massive_fish_fin, 4)
    return (pygame.transform.scale(
        pygame.transform.flip(
            pygame.transform.rotate(
                fish_fin_surface, fin_tetta
            ),
            fin_flip_bool, 0
        ),
        (fin_size, fin_size))
    )

def fishs_eye(fish_eye_scale):
    fish_eye_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    fish_eye_surface.fill((0, 0, 0, 0))
    fish_eye_blic_surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    fish_eye_blic_surface.fill((0, 0, 0, 0))

    circle(fish_eye_surface, (0, 0, 250), (100, 100), 50)
    circle(fish_eye_surface, (10, 30, 30), (110, 110), 20)
    ellipse(fish_eye_blic_surface, (230, 230, 230, 178), [20, 20, 15, 40], 0)
    fish_eye_surface.blit(pygame.transform.rotate(fish_eye_blic_surface, 45), (44, 16))
    return pygame.transform.scale(
        fish_eye_surface, (fish_eye_scale, fish_eye_scale)
    )

def draw_fish(x_fish, y_fish, size_of_fish):
    fish_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    fish_surface.fill((0, 0, 0, 0))
    fish_surface.blit(fishs_fin(70, -5, 0), (80, 50))
    fish_surface.blit(fishs_fin(40, 190, 0), (120, 100))
    fish_surface.blit(fishs_fin(40, 190, 1), (75, 95))
    massive_fish_body=[(170, 100), (165, 94), (160, 90), (150, 86), (140, 83), 
                 (130, 81), (120, 81), (110, 83), (100, 86), (90, 90), (80, 94),    
                 (70, 100), (80, 104), (90, 110), (100, 114), (110, 117), (120, 119),
                 (130, 119), (140, 117), (150, 114), (160, 110), (165, 106) 
                 ]
    massive_fish_tale=[(70, 100), (35, 120), (30, 90), (35, 93), (40, 95), (50, 98), (60, 99) ]

    polygon(fish_surface, (50,100,150), massive_fish_body)
    polygon(fish_surface, (0,0,0), massive_fish_body, 1)
    polygon(fish_surface, (200,100,100), massive_fish_tale)
    polygon(fish_surface, (0,0,0), massive_fish_tale, 1)
    for i in range(0, 5, 1):
        line(fish_surface, (0,0,0), (70, 100), (31 + i, 96 + 6*i), 1)

    fish_surface.blit(fishs_eye(30), (130, 85))
    
    screen.blit(pygame.transform.scale(
        fish_surface, (size_of_fish, size_of_fish)), 
        (x_fish, y_fish)
    )
    return 

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
circle(screen, (100, 100, 100), (200, 200), 2000)
draw_fish(0, 0, 200)



#draw_bird(400, 400, 100, 30)
"""
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
"""

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()