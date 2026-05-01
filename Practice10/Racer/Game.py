import pygame, sys
from pygame.locals import *
import random, time, os

pygame.init()

# FPS
FPS = 60
clock = pygame.time.Clock()

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Paths
BASE_DIR = os.path.dirname(__file__)

def load_image(name):
    return pygame.image.load(os.path.join(BASE_DIR, "images", name))

# Load background
background = load_image("AnimatedStreet.png")

# Fonts
font_small = pygame.font.SysFont("Verdana", 20)
font_big = pygame.font.SysFont("Verdana", 60)

# Game variables
SPEED = 5
COINS = 0

# ================= PLAYER =================
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("Player.png")
        self.rect = self.image.get_rect(center=(160,520))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5,0)
        if keys[K_RIGHT] and self.rect.right < WIDTH:
            self.rect.move_ip(5,0)

# ================= ENEMY =================
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = load_image("Enemy.png")
        self.rect = self.image.get_rect(center=(random.randint(40,360),0))

    def move(self):
        self.rect.move_ip(0, SPEED)

        if self.rect.bottom > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40,360),0)

# ================= COINS =================
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 🎯 случайный "вес" монеты
        self.value = random.choice([1, 2, 5])

        self.image = load_image("coin.png")
        self.image = pygame.transform.scale(self.image, (40,40))

        self.rect = self.image.get_rect(
            center=(random.randint(40,360), 0)
        )

    def move(self):
        self.rect.move_ip(0, 4)

        if self.rect.bottom > HEIGHT:
            self.respawn()

    def respawn(self):
        # новая позиция + новый вес
        self.rect.top = 0
        self.rect.center = (random.randint(40,360), 0)
        self.value = random.choice([1,2,5])

# ================= INIT =================
player = Player()
enemy = Enemy()
coin = Coin()

# ================= GAME LOOP =================
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # движение
    player.move()
    enemy.move()
    coin.move()

    # 🎯 сбор монет
    if player.rect.colliderect(coin.rect):
        COINS += coin.value   # добавляем "вес" монеты
        coin.respawn()

        # 🔥 увеличение скорости врага
        SPEED += 0.3

    # 💥 столкновение
    if player.rect.colliderect(enemy.rect):
        screen.fill(RED)
        text = font_big.render("Game Over", True, BLACK)
        screen.blit(text, (50,250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # отрисовка
    screen.blit(background, (0,0))
    screen.blit(player.image, player.rect)
    screen.blit(enemy.image, enemy.rect)
    screen.blit(coin.image, coin.rect)

    # UI
    score_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    speed_text = font_small.render(f"Speed: {round(SPEED,1)}", True, BLACK)

    screen.blit(score_text, (10,10))
    screen.blit(speed_text, (10,30))

    pygame.display.update()
    clock.tick(FPS)