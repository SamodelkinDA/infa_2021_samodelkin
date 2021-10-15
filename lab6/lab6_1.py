import pygame
from pygame.draw import *
import random
pygame.init()
import pathlib

FPS = 30
WIDTH = 1200
HEIGHT = 800
TIME_LIVE = 500
MAX_SPEED = 5
PLAY_TIME = 20000

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
    """ Функция рисует текст, заданного размера и цвета 
    Опрорной точкой х, у является центр верха текста. 
    """
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)

def finish(score):
    """ Финальное окно. Обращается к файлу с таблицей результатов"""
    close = False
    list_best = open(pathlib.Path(pathlib.Path.home(),"infa_2021_samodelkin", "lab6", "best_pl.txt"), 'r')
    mass = [0] * 6
    k = 0
    for i in range(5):
        current = int(list_best.readline().rstrip())
        if current <= score and k == 0:
            k = 1
            mass[i] = int(score)
        mass[i + k] = current
    list_best.close()
    screen.fill(BLACK)
    list_best = open(pathlib.Path(pathlib.Path.home(), "infa_2021_samodelkin", "lab6", "best_pl.txt"), 'w')
    for i in range(5):
        list_best.write(str(mass[i]) + "\n")
    list_best.close()
    pygame.display.flip()
    while not close:
        click = False
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    click = True 
        x, y = pygame.mouse.get_pos()
        screen.fill(BLACK)
        draw_text("Your score: " + str(int(score)), 50, WIDTH / 2, 20, WHITE)
        draw_text("Best scores:", 50, WIDTH / 2, 120, WHITE)
        for i in range(5):
            draw_text(str(mass[i]), 50, WIDTH / 2, i * 100 + 220, WHITE)
        if (WIDTH / 2 - x) ** 2 < 2500 and (740 - y) ** 2 < 900:
            draw_text("EXIT", 50, WIDTH / 2, 720, RED) 
            if click == True:
                close = True
        else:
            draw_text("EXIT", 50, WIDTH / 2, 720, WHITE) 
        pygame.display.flip()
    
def new_ball():
    """ Создается шарик случайного цвета и положения.
    Так же случайно выбирается время жизни, радиус и скорость.
    """
    dict = {
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "vx": random.randint(-MAX_SPEED, MAX_SPEED),
        "vy": random.randint(-MAX_SPEED, MAX_SPEED),
        "clr": COLORS[random.randint(0, 5)],
        "r": random.randint(30, 50),
        "sp_time": pygame.time.get_ticks(),
        "time_live": random.randint(TIME_LIVE , 2 * TIME_LIVE)
    }
    return dict
    
def new_rect():
    """ Создается квадратик случайного цвета и положения.
    Так же случайно выбирается время жизни, радиус и скорость.
    """
    dict = {
        "x": random.randint(50, WIDTH - 50),
        "y": random.randint(50, HEIGHT - 50),
        "vx": random.randint(-1, 1),
        "vy": random.randint(-1, 1),
        "clr": COLORS[random.randint(0, 5)],
        "sp_time": pygame.time.get_ticks(),
        "time_live": 3000
    }
    return dict

def update(x ,y, balls, rects):
    """  Основная часть. Обновление положений всех элементов 
    Проводит расчет очков и добавляет
    """
    global time_play
    global score
    global finished
    massiv = []
    now = pygame.time.get_ticks()
    for i in rects:
        delet = False
        
        if (i.get("x") - x) ** 2 < 400 and (i.get("y") - y) ** 2 < 400:
            score += 50
            i["vx"] = i["vx"] * random.randint(-3, 3) - 1
            i["vy"] = i["vy"] * random.randint(-3, 3) + 1
        if now - i.get("sp_time") > i.get("time_live"):
            delet = True
        i["x"] += i.get("vx")
        i["y"] += i.get("vy")
        i["clr"] = COLORS[random.randint(0, 5)],
        rect(screen, i.get("clr"), [i.get("x") - 20, i.get("y") - 20, 40, 40])
        rects = ()
        if not delet:
            rects = (i,)


    for i in balls:
        if (i.get("x") - x) ** 2 + (i.get("y") - y) ** 2 < i.get("r") ** 2:
            ds = (60 - i.get("r")) * ((now - i.get("sp_time")) / i.get("time_live")) ** 2
            score += ds * 1000 / i.get("time_live")
            time_play += ds * 100
        elif now - i.get("sp_time") > i.get("time_live"):
            pass
        else: 
            i["x"] += i.get("vx")
            i["y"] += i.get("vy")
            if i.get("x") < 50:
                i["x"] = 50
                i["vx"] = random.randint(1, MAX_SPEED)
            if i.get("x") > WIDTH - 50:
                i["x"] = WIDTH - 50
                i["vx"] = random.randint(-MAX_SPEED, -1)
            if i.get("y") < 50:
                i["y"] = 50
                i["vy"] = random.randint(1, MAX_SPEED)
            if i.get("y") > HEIGHT - 50:
                i["y"] = HEIGHT - 50
                i["vy"] = random.randint(-MAX_SPEED, -1)
            circle(screen, GREY, (i.get("x"), i.get("y")),
                i.get("r")*(2 - (now - i.get("sp_time")) / i.get("time_live"))
                )
            circle(screen, i.get("clr"), (i.get("x"), i.get("y")), i.get("r"))
            massiv.append(i)
    draw_text(str((int(time_play - now)) / 1000), 30, WIDTH / 5, 20, WHITE)
    if len(massiv) <= 3 :
        massiv.append(new_ball())
    draw_text(str(int(score)), 30, WIDTH / 2, 20, WHITE)
    if len(rects) == 0:
        if random.randint(1, 1000) < 10:
            rects = (new_rect(),)
    if time_play < now:
        finish(score)
        finished = True
    return tuple(massiv), rects
        
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
start = False
balls = ()
rects = ()
score = 0

""" Стартовое меню """
while not start:
    click = False
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = True
            finished = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                click = True 
    x, y = pygame.mouse.get_pos()
    screen.fill(BLACK)
    if (WIDTH / 2 - x) ** 2 < 10000 and (HEIGHT / 2 - y) ** 2 < 900:
        draw_text("START", 50, WIDTH / 2, HEIGHT / 2 - 20, RED) 
        if click == True:
            start = True
    else:
        draw_text("START", 50, WIDTH / 2, HEIGHT / 2 - 20, WHITE) 
    pygame.display.flip()


time_play = pygame.time.get_ticks() + PLAY_TIME

while not finished:
    """ Основное тело игры """
    clock.tick(FPS)
    x, y = (0, 0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
    screen.fill(BLACK)
    balls, rects = update(x, y, balls, rects)
    
    pygame.display.flip()

pygame.quit()