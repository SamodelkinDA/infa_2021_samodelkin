import pygame
from pygame.draw import *
import random
pygame.init()

FPS = 30
WIDTH = 1200
HEIGHT = 800
TIME_LIVE = 1000

GREY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def draw_text(text, size, x, y, colour):
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def new_ball():
    dict = {
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "vx": random.randint(-2, 2),
        "vy": random.randint(-2, 2),
        "clr": COLORS[random.randint(0, 5)],
        "r": random.randint(30, 50),
        "sp_time": pygame.time.get_ticks()
    }
    return dict
    
def update(x ,y, balls):
    massiv = []
    now = pygame.time.get_ticks()
    for i in balls:
        if (i.get("x") - x) ** 2 + (i.get("y") - y) ** 2 < i.get("r") ** 2:
            score += 60 - i.get("r")
        elif now - i.get("sp_time") > TIME_LIVE:
            pass
        else: 
            circle(screen, GREY, (i.get("x"), i.get("y")),
                i.get("r")*(2 - (now - i.get("sp_time")) // TIME_LIVE)
                )
            circle(screen, i.get("clr"), (i.get("x"), i.get("y")), i.get("r"))
            massiv.append(i)
    if len(massiv) <= 5 :
        massiv.append(new_ball())
    return tuple(massiv)
        


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = ()
score = 0

while not finished:
    clock.tick(FPS)
    x, y = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
    screen.fill(BLACK)
    balls = update(x, y, balls)
    draw_text(str(score), 30, WIDTH / 2, 20, WHITE)
    pygame.display.flip()

pygame.quit()