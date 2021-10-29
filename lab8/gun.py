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

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Ball:
    def __init__(self, speed, an,  x=40, y=450, r=10, damag=1):
        """ Конструктор класса ball
        Args:
        speed - Начальная скорость вылета шарика 
        an - Угол вылета шарика
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - 
        damag - урон наносимый данным шариком цели
        """
        self.damage = damag
        self.radius = r
        self.x = x
        self.y = y
        self.color = random.choice(GAME_COLORS)
        self.live = FPS * 3
        self.vx = speed * math.cos(an)
        self.vy = speed * math.sin(an)
        Game.balls.append(self)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        Также ведется счетчик времени для уничтожения шарика по прошествии 3 секунд
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
        """ ФУнкция возвращает надо ли перестать обрабатывать данный шарик - 
        Прошло ли время его жизни
        """
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
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (self.radius + r) ** 2

class Gun:
    """ Недокласс, использует параметры своих наследников.
    САМОСТОЯТЕЛЬНОГО ВЫЗОВА НЕ ПОДРАЗУМЕВАЕТ
    """
    def __init__(self, x=40, y=450, ang=0):
        self.x = x
        self.y = y
        
        self.f2_power = 10
        self.f2_on = 0
        self.an = ang
        self.last_shoot = 0
        self.speed = 0

    def fire2_start(self):
        self.f2_on = 1

    def set_defolt(self):
        """ Устанавливает эти параметры на начальные значения"""
        self.f2_on = 0
        self.f2_power = 10

    def move(self):
        """Перемещение пушки по вертикали"""
        self.y += self.speed
        if self.y > 500:
            self.y = 500
        if self.y < 100:
            self.y = 100 
        self.speed = 0

    def targetting(self, x, y):
        """Прицеливание. Зависит от положения мыши."""
        if (x-self.x) != 0:
            self.an = math.atan((y-self.y) / (x-self.x))
        else:
            self.an = math.pi / 2
        
    def change_type(self, k):
        self.tip += k
        if self.tip < 0:
            self.tip = 0
        elif self.tip > 2:
            self.tip = 2
        Game.gun = Game.GUN_TIPS[str(self.tip)](x=self.x, y=self.y, ang=self.an)
    
    def set_speed(self, speed):
        self.speed += speed

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

class Canon(Gun):
    def __init__(self, x=40, y=450, ang=0):
        """ Создание объекта CANON
        Вызывает инициализатор родительского класса"""
        Gun.__init__(self, x, y, ang)
        self.tip = 0
        #self.change_type(1)

    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        Ball(self.f2_power, self.an, x=self.x, y=self.y, damag=4)
        self.set_defolt()

    def draw(self):
        """
        Орисовка пушки.
        """
        self.surf = pygame.transform.rotate(
            Game.canon_imgs[self.f2_power // 7 - 1], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        pass

class Shootgun(Gun):
    DELAY = 1000
    def __init__(self, x=40, y=450, ang=0):
        """ Создание объекта SHOOTGUN 
        Вызывает инициализатор родительского класса"""
        Gun.__init__(self, x, y, ang)
        self.tip = 2

    def fire2_end(self):
        """Выстрел картечью.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости картечи vx и vy зависят от положения мыши
        и случайной добавки разброса.
        """
        global balls
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.DELAY:
            self.last_shoot = now
            for i in range(self.f2_power // 5):
                ang = self.an + (random.random() - 0.5) * self.f2_power / 200
                Ball(random.randint(50, 100), ang, x=self.x, y=self.y, r=3)
        self.set_defolt()

    def draw(self):
        """ Отрисовка картечницы.
        """
        self.surf = pygame.transform.rotate(
            Game.canon_imgs[self.f2_power // 7 - 1], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        pass

class Minigun(Gun):
    def __init__(self, x=40, y=450, ang=0):
        """ Создание объекта MINIGUN 
        Вызывает инициализатор родительского класса"""
        Gun.__init__(self, x, y, ang)
        self.tip = 1
        self.heat = 0
        self.bullets = 10000

    def fire2_end(self):
        """Окончание стрельбы."""
        self.set_defolt()

    def draw(self):
        """
        Рисует миниган. Смена картинки происходит циклически при выстрелах.
        """
        self.surf = pygame.transform.rotate(
            Game.mini_imgs[self.bullets % 2], - self.an * 180 / math.pi
            )
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))
        pygame.draw.rect(screen, BLUE, [20, 20 , 100, 5])
        pygame.draw.rect(screen, RED, [20, 20 , 2 * self.heat, 5])

    def shooting(self):
        global balls
        now = pygame.time.get_ticks()
        if now - self.last_shoot > 500000 / self.f2_power ** 2 and self.f2_on and self.heat < 50:
            self.heat += 1
            self.last_shoot = now
            self.bullets -= 1
            ang = self.an + (random.random() - 0.5) * self.f2_power / 500
            Ball(80, ang, x=self.x, y=self.y, r=5)
        if self.f2_on:
            self.heat -= 0.1
        else:
            self.heat -= 0.1
        if self.heat < 0:
            self.heat = 0

class Target:
    def __init__(self):
        """Создание новой цели."""
        self.img = pygame.Surface((100, 100), pygame.SRCALPHA)
        self.new_target()

    def new_target(self):
        """ Задание положения и параметров новой цели. """
        self.hp = random.randint(3, 8)
        self.x = random.randint(600, 780)
        self.y = random.randint(100, 500)
        self.r = random.randint(5, 50)
        self.color = random_colour()
        self.img.fill((0, 0, 0, 0))
        pygame.draw.circle(self.img, self.color, (50, 50), self.r)

    def hit(self, points=1):
        """Попадание шарика в цель.
        При попаданиях на цель накладываются изображения трещин.
        Points - урон наносимый цели"""
        global score
        self.hp -= points
        crack = pygame.transform.rotate(
            pygame.transform.scale(
                random.choice(Game.crack_imgs), (4 * self.r, 4 * self.r)
            ), random.randint(0, 359)
        )
        crack_rect = crack.get_rect()
        self.img.blit(crack, (50 - crack_rect.width / 2, 50 - crack_rect.height / 2))
        if self.hp <= 0:
            self.new_target()
            Game.score += 1

    def move(self):
        """ Задает движения шариков. Пока что это броуновское движение """
        self.x += random.randint(-2, 2) * 60 / FPS
        self.y += random.randint(-2, 2) * 60 / FPS
        if not ((500 < self.x < 780) and (100 < self.y < 500)):
            self.new_target()

    def get_param(self):
        """Возвращает нужные параметры x, y, r"""
        return self.x, self.y, self.r

    def draw(self):
        """ Отрисовка цели """
        screen.blit(self.img, (self.x - 50, self.y - 50))

class Game():
    GUN_TIPS = {"0": Canon,
            "1": Minigun,
            "2": Shootgun
        }
    balls = []
    targets = []
    score = 0
    gun = None
    canon_imgs = []
    mini_imgs = []
    crack_imgs = []

    def __init__(self):
        self.load_imgs()
        self.menu()
        
    def menu(self):
        self.new_game()

    def new_game(self):
        Game.balls = []
        Game.targets = []
        Game.score = 0
        self.clock = pygame.time.Clock()
        Game.gun = Canon()
        self.targets.append(Target())
        self.targets.append(Target())
        finished = False
        while not finished:
            screen.fill(WHITE)
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.gun.fire2_start()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.gun.fire2_end()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.gun.change_type(-1)
                    if event.key == pygame.K_RIGHT:
                        self.gun.change_type(1)
            self.gun.targetting(*pygame.mouse.get_pos())
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_DOWN]:
                self.gun.set_speed(1)
            if keystate[pygame.K_UP]:
                self.gun.set_speed(-1)
            self.gun.move()
            for b in self.balls:
                b.move()
                rem = False
                for t in self.targets:
                    if b.hittest(t) and (not rem) :
                        t.hit(b.damage)
                        rem = True
                if b.should_del():
                    rem = True
                if rem == True:
                    self.balls.remove(b)
                b.draw()
            for t in self.targets:
                t.move()
                t.draw()
            self.gun.draw()
            draw_text(str(self.score), 50, 50, 50, RED )
            pygame.display.flip()
            self.gun.shooting()
            self.gun.power_up()

    def load_imgs(self):
        for i in range(14):
            Game.canon_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'cannon{}.png'.format(i)
                )), (150, 150)).convert())
            Game.canon_imgs[i].set_colorkey(WHITE)
        
        for i in range(2):
            Game.mini_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'minigun{}.png'.format(i)
                )), (200, 200)).convert())
            Game.mini_imgs[i].set_colorkey(WHITE)
        for i in range(3):
            Game.crack_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'crack{}.png'.format(i)
                )), (400, 400)).convert())
            Game.crack_imgs[i].set_colorkey(WHITE)

def random_colour():
    """ Функция возвращает кортеж из трех случайных чисел от 20 до 240,
    задающих некоторый случайный цвет"""
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


Game()

pygame.quit()
