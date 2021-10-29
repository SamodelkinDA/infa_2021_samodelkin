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


WIDTH = 1400
HEIGHT = 600

class Bomb():
    def __init__(self, speed_x, x=40, y=450, r=10, damag=10):
        """ Конструктор класса Bomb
        Args:
        speed - Начальная скорость вылета шарика 
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        r - 
        damag - урон наносимый данным шариком цели
        """
        self.damage = damag
        self.radius = 5
        self.x = x
        self.y = y
        self.live = FPS * 3
        self.vx = speed_x
        self.vy = 0
        Game.bombs.append(self)

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        Также ведется счетчик времени для уничтожения шарика по прошествии 3 секунд
        """
        if self.y > 500: 
            self.live = 0
        else:
            self.vy += 2 * 30 / FPS
        self.x += self.vx * 30 / FPS
        self.y += self.vy * 30 / FPS
        self.live -= 1

    def should_del(self):
        """ ФУнкция возвращает надо ли перестать обрабатывать данный шарик - 
        Прошло ли время его жизни
        """
        return self.live <= 0

    def draw(self):
        pygame.draw.circle(
            screen,
            BLACK,
            (self.x, self.y),
            self.radius
        )

    def hittest(self, x, y, r):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (self.radius + r) ** 2

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

    def hittest(self, x, y ,r):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        return (x - self.x) ** 2 + (y - self.y) ** 2 < (self.radius + r) ** 2

class Gun:
    """ Недокласс, использует параметры своих наследников.
    САМОСТОЯТЕЛЬНОГО ВЫЗОВА НЕ ПОДРАЗУМЕВАЕТ
    """
    def __init__(self, x=40, y=450, ang=0):
        self.x = x
        self.y = y
        self.r = 15
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
        self.x -= self.speed
        if self.x > WIDTH:
            self.x = WIDTH
        if self.x < 10:
            self.x = 10
        self.speed = 0

    def targetting(self, x, y):
        """Прицеливание. Зависит от положения мыши."""
        if (y-self.y) != 0:
            self.an = 3 * math.pi / 2 -  math.atan((x-self.x) / (y-self.y))
        else:
            self.an = 0
        
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

    def get_param(self):
        return self.x, self.y, self.r

class Canon(Gun):
    def __init__(self, x=40, y=480, ang=0):
        """ Создание объекта CANON
        Вызывает инициализатор родительского класса"""
        Gun.__init__(self, x, y, ang)
        self.tip = 0
        self.heat = 0
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
        screen.blit(Game.lafit_img, (self.x - 30, self.y - 40))
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        self.heat = 50 / 90 * (self.f2_power -10)

class Shootgun(Gun):
    DELAY = 1000
    def __init__(self, x=40, y=480, ang=0):
        """ Создание объекта SHOOTGUN 
        Вызывает инициализатор родительского класса"""
        Gun.__init__(self, x, y, ang)
        self.tip = 2
        self.heat = 0

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
        screen.blit(Game.lafit_img, (self.x - 30, self.y - 40))
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        self.heat = 50 / 90 * (self.f2_power -10)

class Minigun(Gun):
    def __init__(self, x=40, y=480, ang=0):
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
        if self.an > 3 * math.pi / 2:
            self.surf = pygame.transform.rotate(
                Game.mini_imgs[self.bullets % 2], - self.an * 180 / math.pi
            )
        else:
            self.surf = pygame.transform.flip(pygame.transform.rotate(
                Game.mini_imgs[self.bullets % 2], math.pi + self.an * 180 / math.pi
            ), False, True)
        screen.blit(Game.lafit_img, (self.x - 30, self.y - 40))
        
        self.surf_rect = self.surf.get_rect()
        screen.blit(self.surf, (
            self.x - self.surf_rect.width / 2,
            self.y - self.surf_rect.height / 2
            ))

    def shooting(self):
        #global balls
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
        self.img = pygame.Surface((400, 400), pygame.SRCALPHA)
        self.new_target()

    def new_target(self):
        """ Задание положения и параметров новой цели. """
        self.hp = random.randint(3, 8)
        self.x = random.randint(200, WIDTH - 200)
        self.y = random.randint(100, 500)
        self.r = random.randint(5, 50)
        self.color = random_colour()
        self.img.fill((0, 0, 0, 0))
        pygame.draw.circle(self.img, self.color, (50, 50), self.r)

    def hit(self, points):
        """Попадание шарика в цель.
        При попаданиях на цель накладываются изображения трещин.
        Points - урон наносимый цели"""
        self.hp -= points
        if self.hp <= 0:
            self.new_target()
            Game.score += 1

    def get_param(self):
        """Возвращает нужные параметры x, y, r"""
        return self.x, self.y, self.r

    def draw(self):
        """ Отрисовка цели """
        screen.blit(self.img, (self.x - 50, self.y - 50))

class Broun(Target):
    def move(self):
        """ Задает движения шариков. Пока что это броуновское движение """
        self.x += random.randint(-5, 5) * 60 / FPS
        self.y += random.randint(-5, 5) * 60 / FPS
        if not ((50 < self.x < WIDTH - 50) and (50 < self.y < 450)):
            self.new_target()
    
    def hit(self, point=1):
        Target.hit(self, point)
        crack = pygame.transform.rotate(
            pygame.transform.scale(
                random.choice(Game.crack_imgs), (4 * self.r, 4 * self.r)
            ), random.randint(0, 359)
        )
        crack_rect = crack.get_rect()
        self.img.blit(crack, (50 - crack_rect.width / 2, 50 - crack_rect.height / 2))

class Bomber(Target):
    def new_target(self):
        self.hp = random.randint(5, 8)
        self.y = random.randint(100, 300)
        self.r = 25
        self.FR = random.randint(FPS//3, FPS)
        self.count = self.FR - 7
        self.zn =  random.randint(0, 1) * 2 - 1
        self.speed_x = random.randint(5, 7) * self.zn
        self.x = WIDTH * (1 - self.zn) / 2
        self.img.fill((0, 0, 0, 0))
        if self.zn < 0:
            self.img.blit(Game.bomber_img, (0, 0))
        else:
            self.img.blit(pygame.transform.flip(Game.bomber_img, True, False),(0, 0))
        #pygame.draw.circle(self.img, RED, (50, 50), self.r)

    def move(self):
        self.count += 1
        if self.count > self.FR:
            self.count = 0
            Bomb(self.speed_x, self.x, self.y)
        """ Задает движения шариков. Пока что это броуновское движение """
        self.x += self.speed_x * 60 / FPS
        self.y += 0 * 60 / FPS
        if not (0 < self.x < WIDTH) :
            self.new_target()

class Bot():
    FIRE_DELAY = 5000
    def __init__(self, x, fird = - 5000):
        self.gun = Minigun(x, ang = -1)
        Game.bots.append(self)
        self.stop_fire = fird

    def update(self):
        self.gun.draw()
        self.targ = random.choice(Game.targets)
        d = (self.targ.x - self.gun.x) ** 2 + (self.targ.y - self.gun.y) ** 2
        for i in Game.targets:
            if (i.x - self.gun.x) ** 2 + (i.y - self.gun.y) ** 2 < d:
                self.targ = i
                d = (self.targ.x - self.gun.x) ** 2 + (self.targ.y - self.gun.y) ** 2
        self.gun.targetting(self.targ.x, self.targ.y)
        now = pygame.time.get_ticks()
        if now - self.stop_fire > self.FIRE_DELAY:
            if self.gun.heat > 45:
                self.gun.fire2_end()
                self.stop_fire = now
            else:
                self.gun.fire2_start()
                self.gun.power_up()
        self.gun.shooting()
        


class Game():
    GUN_TIPS = {"0": Canon,
            "1": Minigun,
            "2": Shootgun
        }
    balls = []
    bombs = []
    bots = []
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
        Game.bots = []
        Game.bombs = []
        Game.targets = []
        Game.score = 0
        self.clock = pygame.time.Clock()
        Game.gun = Canon(x=900)
        self.targets.append(Broun())
        self.bots.append(Bot(100))
        self.targets.append(Bomber())
        self.targets.append(Bomber())
        self.targets.append(Bomber())
        finished = False
        while not finished:
            screen.fill(WHITE)
            pygame.draw.rect(screen, GREY, [0, 500, WIDTH, 100])
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
                    if b.hittest(*t.get_param()) and (not rem) :
                        t.hit(b.damage)
                        rem = True
                if b.should_del():
                    rem = True
                if rem == True:
                    self.balls.remove(b)
                b.draw()
            for bmb in Game.bombs:
                bmb.move()
                bmb.draw()
                rem = False
                if bmb.hittest(*Game.gun.get_param()) and (not rem) :
                    Game.score -= 20
                    if Game.score < 0:
                        Game.score = 0
                    rem = True
                for bot in Game.bots:
                    if bmb.hittest(*Game.gun.get_param()) and (not rem) :
                        Game.score -= 5
                        if Game.score < 0:
                            Game.score = 0
                        rem = True
                if bmb.should_del():
                    rem = True
                if rem == True:
                    self.bombs.remove(bmb)
            for bot in Game.bots:
                bot.update()
            for t in self.targets:
                t.move()
                t.draw()
            self.gun.draw()
            draw_text(str(self.score), 50, 50, 50, RED )
            pygame.draw.rect(screen, BLUE, [20, 20 , 100, 5])
            pygame.draw.rect(screen, RED, [20, 20 , 2 * self.gun.heat, 5])
            pygame.display.flip()
            self.gun.shooting()
            self.gun.power_up()

    def load_imgs(self):
        Game.lafit_img = pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'lafit.png'
                )), (60, 60)).convert()
        Game.lafit_img.set_colorkey(WHITE)
        Game.bomber_img = pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'bomber.png'
                )), (100, 100)).convert()
        Game.bomber_img.set_colorkey(WHITE)
        for i in range(14):
            Game.canon_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'cannon{}.png'.format(i)
                )), (150, 150)).convert())
            Game.canon_imgs[i].set_colorkey(WHITE)
        
        for i in range(2):
            Game.mini_imgs.append(pygame.transform.scale(pygame.image.load(pathlib.Path(
                pathlib.Path.home(),"infa_2021_samodelkin", "lab8", "images", 'minigun{}.png'.format(i)
                )), (100, 100)).convert())
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

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

Game()

pygame.quit()
