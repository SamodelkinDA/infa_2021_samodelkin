import math
import random
import pygame


FPS = 30

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 203, 31)
GREEN = (0, 255, 0)
MAGENTA = (255, 3, 184)
CYAN = (0, 255, 204)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (125, 125, 125)
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600


class Ball:
    radius = 10
    def __init__(self, speed, an,  x=20, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.color = random.choice(GAME_COLORS)
        self.live = FPS 
        self.vx = speed * math.cos(an)
        self.vy = speed * math.sin(an)

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.y > 500: 
            self.vy *= -0.8
            self.vx *= 0.8
            self.y = 500
        else:
            self.vy += 2 * 30 / FPS
            if self.x > WIDTH:
                self.x = WIDTH 
                self.vx *= -1 
        self.x += self.vx * 30 / FPS
        self.y += self.vy * 30 / FPS
        self.live -= 1

    def shoul_del(self):
        return self.live < 0

    def draw(self):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.radius
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return False

class Gun:
    def __init__(self, x=20, y=450):
        self.x = x
        self.y = y
        self.f2_power = 10
        self.f2_on = 0
        self.an = 0
        self.color = GREY
        self.surf_orig = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.surf_orig.fill((0, 0, 0, 0))

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.f2_power, self.an)

        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        # FIXIT don't know how to do it - FIXED
        self.surf = self.surf_orig.copy()
        pygame.draw.rect(self.surf, self.color , [100 , 95, 30 + self.f2_power / 2, 10])
        self.surf = pygame.transform.rotate(self.surf, - self.an * 180 / math.pi)
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))
        #(self.x, self.y)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self):
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 550)
        self.r = random.randint(5, 50)
        self.color = random_colour()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = random.randint(600, 780)
        self.y = random.randint(300, 500)
        self.r = random.randint(5, 50)
        self.color = random_colour()

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

def random_colour():
    return tuple( [random.randint(20, 240) for i in range(3)])

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun()
target = Target()
finished = False


while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()
    pygame.display.flip()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
    gun.power_up()

pygame.quit()
