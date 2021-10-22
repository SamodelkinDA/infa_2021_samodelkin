import math
import random
import pygame
import pathlib

FPS = 60

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
    def __init__(self, speed, an,  x=20, y=450, r=10):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.radius = r
        self.x = x
        self.y = y
        self.color = random.choice(GAME_COLORS)
        self.live = FPS * 3
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

    def should_del(self):
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
        x, y, r = obj.get_param()
        if (x - self.x) ** 2 + (y - self.y) ** 2 < (self.radius + r) ** 2:
            return True
        return False

class Gun:
    def __init__(self, x=40, y=450, ang=0, tip=0):
        self.x = x
        self.y = y
        self.tip = tip
        self.f2_power = 10
        self.f2_on = 0
        self.an = ang
        self.last_shoot = 0
        self.bullets = 10000

    def fire2_start(self):
        self.f2_on = 1

    def set_defolt(self):
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if (event.pos[0]-self.x) != 0:
                self.an = math.atan((event.pos[1]-self.y) / (event.pos[0]-self.x))
            else:
                self.an = math.pi / 2
        
    def change_type(self, event):
        global gun
        
        if event.key == pygame.K_LEFT:
            self.tip -= 1
        if event.key == pygame.K_RIGHT:
            self.tip += 1
        if self.tip < 0:
            self.tip = 0
        elif self.tip > 2:
            self.tip = 2
        gun = GUN_TIPS[str(self.tip)](ang=self.an, tip=self.tip)
    
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
        self.shooting()

class Canon(Gun):
    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.f2_power, self.an)
        balls.append(new_ball)
        self.set_defolt()

    def draw(self):
        # FIXIT don't know how to do it - FIXED
        """
        self.surf_orig = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.surf_orig.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, self.color , [100 , 95, 30 + self.f2_power / 2, 10])
        """
        self.surf = pygame.transform.rotate(
            canon_imgs[self.f2_power // 7 - 1], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))
    def shooting(self):
        pass

class Shootgun(Gun):
    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        now = pygame.time.get_ticks()
        if now - self.last_shoot > 2000:
            self.last_shoot = now
            for i in range(self.f2_power // 5):
                ang = self.an + (random.random() - 0.5) * self.f2_power / 200
                new_ball = Ball(random.randint(50, 100), ang, r=3)
                balls.append(new_ball)
    
        self.set_defolt()

    def draw(self):
        # FIXIT don't know how to do it - FIXED
        """
        self.surf_orig = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.surf_orig.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, self.color , [100 , 95, 30 + self.f2_power / 2, 10])
        """
        self.surf = pygame.transform.rotate(
            canon_imgs[self.f2_power // 7 - 1], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        pass

class Minigun(Gun):
    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.set_defolt()

    def draw(self):
        # FIXIT don't know how to do it - FIXED
        """
        self.surf_orig = pygame.Surface((200, 200), pygame.SRCALPHA)
        self.surf_orig.fill((0, 0, 0, 0))
        pygame.draw.rect(self.surf, self.color , [100 , 95, 30 + self.f2_power / 2, 10])
        """
        self.surf = pygame.transform.rotate(
            mini_imgs[self.bullets % 2], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        global balls
        now = pygame.time.get_ticks()
        if now - self.last_shoot > 500000 / self.f2_power ** 2 and self.f2_on:
            self.bullets -= 1
            self.last_shoot = now
            ang = self.an + (random.random() - 0.5) * self.f2_power / 500
            new_ball = Ball(80, ang, r=5)
            balls.append(new_ball)

class Target:
    # self.points = 0
    # self.live = 1
    # FIXME: don't work!!! How to call this functions when object is created?
    # self.new_target()
    def __init__(self):
        self.img = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.hp = random.randint(1, 3)
        self.x = random.randint(600, 780)
        self.y = random.randint(100, 500)
        self.r = random.randint(5, 50)
        self.color = random_colour()
        self.img.fill((0, 0, 0, 0))
        pygame.draw.circle(self.img, self.color, (50, 50), self.r)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        global score, gun
        self.hp -= points
        crack = pygame.transform.rotate(
            pygame.transform.scale(
                random.choice(crack_imgs), (4 * self.r, 4 * self.r)
            ), random.randint(0, 359)
        )
        crack_rect = crack.get_rect()
        self.img.blit(crack, (50 - crack_rect.width / 2, 50 - crack_rect.height / 2))
        if self.hp <= 0:
            self.new_target()
            score += 1

    def move(self):
        self.x += random.randint(-2, 2) * 60 / FPS
        self.y += random.randint(-2, 2) * 60 / FPS
        if not ((500 < self.x < 780) and (100 < self.y < 500)):
            self.new_target()

    def get_param(self):
        return self.x, self.y, self.r

    def draw(self):
        screen.blit(self.img, (self.x - 50, self.y - 50))
        #pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

def random_colour():
    return tuple( [random.randint(20, 240) for i in range(3)])

def draw_text(text, size, x, y, colour):
    """ Функция рисует текст, заданного размера и цвета 
    Опрорной точкой х, у является центр верха текста. 
    """
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


GUN_TIPS = {"0": Canon,
            "1": Minigun,
            "2": Shootgun
        }

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
balls = []
target = []
score = 0

canon_imgs = []
for i in range(14):
    canon_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
        pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'cannon{}.png'.format(i)
        )), (150, 150)).convert())
    canon_imgs[i].set_colorkey(WHITE)
crack_imgs = []
for i in range(3):
    crack_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
        pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'crack{}.png'.format(i)
        )), (400, 400)).convert())
    crack_imgs[i].set_colorkey(WHITE)
mini_imgs = []
for i in range(2):
    mini_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
        pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'minigun{}.png'.format(i)
        )), (200, 200)).convert())
    mini_imgs[i].set_colorkey(WHITE)

clock = pygame.time.Clock()
gun = Shootgun()
target.append(Target())
target.append(Target())
finished = False


while not finished:
    screen.fill(WHITE)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end()
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            gun.change_type(event)

    for b in balls:
        b.move()
        rem = False
        for t in target:
            if b.hittest(t) and (not rem) :
                t.hit()
                rem = True
        if b.should_del():
            rem = True
        if rem == True:
            balls.remove(b)
        b.draw()
    for t in target:
        t.move()
        t.draw()
    gun.draw()
    draw_text(str(score), 50, 50, 50, RED )
    pygame.display.flip()
    gun.power_up()


pygame.quit()
