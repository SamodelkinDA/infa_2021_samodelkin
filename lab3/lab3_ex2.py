"""Эта программа рисует красивые картинки.
   На данный момент она может нарисовать далеких птиц и
   глаз, плавник рыбы
"""


import pygame
import random
import numpy
from pygame import draw  
from pygame.draw import *

#--------------- LITTLE Bird ----------

def draw_little_bird(x_little_bird, y_little_bird, size_of_little_bird, angle_of_little_bird):
    bird_surface = pygame.Surface((size_of_little_bird*2, size_of_little_bird), pygame.SRCALPHA)
    bird_surface.fill((0, 0, 0, 0))
    arc(bird_surface, (255, 255, 255), 
        [size_of_little_bird, 0, size_of_little_bird, size_of_little_bird/2],
        numpy.pi/2, numpy.pi, 3)
    arc(bird_surface, (255, 255, 255), 
        [0, 0, size_of_little_bird, size_of_little_bird/2], 
        0, numpy.pi / 2, 3)
    screen.blit(pygame.transform.rotate(bird_surface, angle_of_little_bird), (x_little_bird - size_of_little_bird, y_little_bird))
    return

# ------------- FISH -----------

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
    fish_surface.set_alpha(128)
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

#-------------- Big Bird ------------------

def birds_beak(beak_size, beak_flap_bool):
    bird_beak_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
    bird_beak_surface.fill((0, 0, 0, 0))
    massive_beak=[(50, 90), (70, 91), (100, 92), (115, 91), (120, 90), (130, 88), (140, 85),
                 (150, 80),  (148, 86), (143, 99), (135, 107), (130, 109),
                 (115, 111), (100, 112), (70, 111), (55, 110)
                 ]
    polygon(bird_beak_surface, (200,200,0), massive_beak)
    polygon(bird_beak_surface, (0,0,0), massive_beak, 2)
    return pygame.transform.scale(
        pygame.transform.flip(
            bird_beak_surface, 0, beak_flap_bool
        ), (beak_size, beak_size))

def draw_oval(x_long, y_short , tetta_rotat):
    Oval_surf = pygame.Surface((200, 200), pygame.SRCALPHA)
    Oval_surf.fill((0, 0, 0, 0))    
    ellipse(Oval_surf, (250, 250, 250), [100 - x_long/2, 100 - y_short/2, x_long, y_short])
    return pygame.transform.rotate(
            Oval_surf, tetta_rotat
        )   

def bird_claw(claw_size):
    bird_claw_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
    bird_claw_surface.fill((0, 0, 0, 0))
    massive_claw=[(52, 190), (50, 200),(49, 210), (50, 280), (88, 173), (90, 171), (94, 166), (150, 140),
                 (250, 170), (350, 220), (270, 160), (210, 135), (260, 140), (370, 180), (290,125), (240, 110), 
                 (290, 110), (380, 140), (320, 100),
                 (290, 90), (200, 80), (107, 95), (80, 110),  (72, 122)
                 ]
    polygon(bird_claw_surface, (200,200,100), massive_claw)
    polygon(bird_claw_surface, (0,0,0), massive_claw, 2)
    return pygame.transform.scale(
        pygame.transform.rotate(
        bird_claw_surface, 10
        ), (claw_size, claw_size)
    )    

def bird_leg(leg_size):
    bird_leg_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
    bird_leg_surface.fill((0, 0, 0, 0))   
    bird_leg_surface.blit(bird_claw(120),(220,155)) 
    bird_leg_surface.blit(draw_oval(100, 50 , 115),(0,0))
    bird_leg_surface.blit(draw_oval(120, 30 , 168),(78,68))
    return pygame.transform.scale(
            bird_leg_surface, (leg_size, leg_size)
        )    

def bird_wing(wing_size, wing_tetta):
    bird_wing_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
    bird_wing_surface.fill((0, 0, 0, 0))
    massive_wing=[(360, 320), (358, 300), (350, 250), (340, 227), (330, 210),
                 (320, 196), (310, 183), (305, 175), (300, 172),(297, 171), 
                 (295, 169), (260, 153), (225, 145), (215, 144), (150, 143), 
                 (140, 140), (135, 139), (120, 135), (100, 127), (80, 115),
                 (60, 101), (55, 100), (53, 102), (54, 110), (56, 115), (68, 140),
                 (80, 160), (100, 175), (130, 190), (160, 197), (190, 210), 
                 (205, 230), (218, 256), (220, 260), (224, 265), (260, 300), (285, 320)
                 ]
    polygon(bird_wing_surface, (250,250,250), massive_wing)
    polygon(bird_wing_surface, (0,0,0), massive_wing, 2)
    return pygame.transform.scale(
        pygame.transform.rotate(
        bird_wing_surface,  wing_tetta
        ), (wing_size, wing_size)
    )    

def bird_tale(tale_size, tale_tetta):
    bird_tale_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
    bird_tale_surface.fill((0, 0, 0, 0))
    massive_tale=[(320, 230), (280, 200), (240, 165), (200, 120), (155, 35), (152, 30), (150, 29), (148, 30), (145, 33), 
                 (130, 60), (110, 100), (90, 145), (70, 200), (63, 240), 
                 (62, 250), (65, 255), (115, 276), (165, 287), (215, 294), (265, 298), (320, 300)
                 ]
    polygon(bird_tale_surface, (250,250,250), massive_tale)
    polygon(bird_tale_surface, (0,0,0), massive_tale, 2)
    return pygame.transform.scale(
        pygame.transform.rotate(
        bird_tale_surface,  tale_tetta
        ), (tale_size, tale_size)
    ) 
    pass

def draw_bird(x_bird, y_bird, size_of_bird, bird_flit_bool):
    bird_surface = pygame.Surface((800, 800), pygame.SRCALPHA)
    bird_surface.fill((0, 0, 0, 0))
    bird_surface.blit(bird_tale(200, 0), (135,272))
    bird_surface.blit(birds_beak(120, 0), (600,312))
    bird_surface.blit(birds_beak(120, 1), (600,300))
    bird_surface.blit(bird_leg(400), (260,310))
    bird_surface.blit(bird_leg(400), (240,340))
    bird_surface.blit(bird_wing(400, -15), (105,60))
    bird_surface.blit(bird_wing(400, 10), (35,110))
    
    ellipse(bird_surface, (250, 250, 250), [280, 350, 240, 100])
    ellipse(bird_surface, (250, 250, 250), [480, 370, 120, 40])
    ellipse(bird_surface, (250, 250, 250), [560, 340, 80, 50])
    ellipse(bird_surface, (0, 0, 0), [606, 356, 10, 10])
    screen.blit(pygame.transform.scale(
        pygame.transform.flip(
            bird_surface, bird_flit_bool, 0
        ), (size_of_bird, size_of_bird)), 
        (x_bird, y_bird)
    )

#------------------- draw -------------

def draw_background():
    rect(screen, (33, 33, 120), (0,0, 600 , 80))
    rect(screen, (141, 95, 211), (0, 80, 600,40))
    rect(screen, (205, 135, 222), (0, 120, 600,70))
    rect(screen, (222, 135, 170), (0, 190, 600,100))
    rect(screen, (255, 153, 85), (0, 290, 600,80))
    rect(screen, (0, 102, 128), (0, 370, 600,360))

def draw_picture1():
    draw_background()
    draw_bird(0,280,500,0)
    draw_fish(250, 560, 200)
    draw_little_bird(120, -10, 150, 15)
    draw_little_bird(300, 140, 150, 0)
    draw_little_bird(130, 200, 150, -15)

def draw_picture2():
    draw_background()
    for i in range(10):
        draw_little_bird(random.randint(0,500), random.randint(0,300), 50, random.randint(-15, 15))
    draw_bird(-50,280,500,0)
    draw_bird(330,330,200,1)
    draw_bird(220,360,100,0)
    draw_fish(300, 560, 200)
    draw_fish(320, 450, 200)
    draw_fish(20, 580, 200)
    draw_little_bird(120, -10, 150, 15)
    draw_little_bird(300, 140, 150, 0)
    draw_little_bird(130, 200, 150, -15)
# -------------------- main ---------------


pygame.init()
FPS = 30
screen = pygame.display.set_mode((520, 730))
draw_picture1()

I=1
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while I<5:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            draw_picture2()
            I+=1
            pygame.display.flip()
            

pygame.quit()