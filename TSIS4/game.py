import pygame, random

CELL = 20
W, H = 600, 600

class Game:
    def __init__(self, settings):
        self.settings = settings
        self.reset()

    def reset(self):
        self.snake = [(100,100),(80,100),(60,100)]
        self.dir = (CELL,0)

        self.score = 0
        self.level = 1
        self.speed = 10

        self.food = None
        self.poison = None

        self.power = None
        self.power_pos = None
        self.power_spawn_time = 0

        self.speed_boost = False
        self.slow_mode = False
        self.shield = False
        self.shield_used = False

        self.obstacles = []

        self.spawn_food()
        self.spawn_poison()

    # ---------- FOOD ----------
    def spawn_food(self):
        while True:
            p = (random.randrange(0,W,CELL), random.randrange(0,H,CELL))
            if p not in self.snake:
                self.food = p
                break

    def spawn_poison(self):
        self.poison = (random.randrange(0,W,CELL),
                       random.randrange(0,H,CELL))

    # ---------- POWER ----------
    def spawn_power(self):
        self.power = random.choice(["speed","slow","shield"])
        self.power_pos = (random.randrange(0,W,CELL),
                          random.randrange(0,H,CELL))
        self.power_spawn_time = pygame.time.get_ticks()

    # ---------- OBSTACLES SAFE ----------
    def generate_obstacles(self):
        self.obstacles = []
        if self.level < 3:
            return

        for _ in range(15):
            while True:
                p = (random.randrange(0,W,CELL),
                     random.randrange(0,H,CELL))

                # avoid spawn near snake head (simple safety)
                hx, hy = self.snake[0]
                if abs(p[0]-hx) < 60 and abs(p[1]-hy) < 60:
                    continue

                if p not in self.snake:
                    self.obstacles.append(p)
                    break

    # ---------- UPDATE ----------
    def update(self):
        head = (self.snake[0][0]+self.dir[0],
                self.snake[0][1]+self.dir[1])

        # wall
        if not (0<=head[0]<W and 0<=head[1]<H):
            return False

        # self
        if head in self.snake[1:] and not self.shield_used:
            return False

        # obstacles
        if head in self.obstacles:
            return False

        self.snake.insert(0, head)

        # food
        if head == self.food:
            self.score += 1
            self.spawn_food()

            if self.score % 5 == 0:
                self.level += 1
                self.speed += 2
                self.generate_obstacles()

        else:
            self.snake.pop()

        # poison
        if head == self.poison:
            self.snake = self.snake[:-2]
            if len(self.snake) <= 1:
                return False
            self.spawn_poison()

        # power pickup
        if self.power and head == self.power_pos:
            if self.power == "speed":
                self.speed_boost = True
            elif self.power == "slow":
                self.slow_mode = True
            elif self.power == "shield":
                self.shield = True
            self.power = None

        # power timeout (8 sec)
        if self.power and pygame.time.get_ticks() - self.power_spawn_time > 8000:
            self.power = None

        return True

    # ---------- DRAW ----------
    def draw(self, screen):
        screen.fill((0,0,0))

        for s in self.snake:
            pygame.draw.rect(screen, self.settings["snake_color"], (*s,CELL,CELL))

        pygame.draw.rect(screen,(0,255,0),(*self.food,CELL,CELL))
        pygame.draw.rect(screen,(139,0,0),(*self.poison,CELL,CELL))

        for o in self.obstacles:
            pygame.draw.rect(screen,(120,120,120),(*o,CELL,CELL))

        if self.power:
            color = (0,255,255) if self.power=="speed" else (255,255,0)
            pygame.draw.rect(screen,color,(*self.power_pos,CELL,CELL))