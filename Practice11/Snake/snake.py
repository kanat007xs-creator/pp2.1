import pygame, sys, random, time

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()

snake = [(100,100), (80,100), (60,100)]
direction = (20, 0)

score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

# ================= FOOD SYSTEM =================
food = None
food_value = 1
food_spawn_time = 0
food_lifetime = 5

def generate_food():
    global food, food_value, food_spawn_time, food_lifetime

    while True:
        pos = (random.randrange(0, WIDTH, CELL),
               random.randrange(0, HEIGHT, CELL))
        if pos not in snake:
            food = pos
            break

    # 🎯 случайный вес
    food_value = random.choice([1, 2, 3])

    # ⏱ таймер жизни
    food_spawn_time = time.time()
    food_lifetime = random.randint(3, 7)

# первый спавн еды
generate_food()

# ================= GAME LOOP =================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL):
                direction = (0, -CELL)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL):
                direction = (0, CELL)
            elif event.key == pygame.K_LEFT and direction != (CELL, 0):
                direction = (-CELL, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL, 0):
                direction = (CELL, 0)

    # новая голова
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # 💥 столкновение со стеной
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        pygame.quit()
        sys.exit()

    # 💥 столкновение с собой
    if head in snake[1:]:
        pygame.quit()
        sys.exit()

    # 🍎 съели еду
    if head == food:
        score += food_value
        generate_food()

        # 📈 уровень и скорость
        if score % 5 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    # ⏱ исчезновение еды
    if time.time() - food_spawn_time > food_lifetime:
        generate_food()

    # ===== РЕНДЕР =====
    screen.fill((0,0,0))

    # змейка
    for segment in snake:
        pygame.draw.rect(screen, (0,255,0), (*segment, CELL, CELL))

    # 🎯 цвет еды по весу
    if food_value == 1:
        color = (255,0,0)
    elif food_value == 2:
        color = (255,165,0)
    else:
        color = (0,0,255)

    pygame.draw.rect(screen, color, (*food, CELL, CELL))

    # текст
    text = font.render(f"Score: {score}  Level: {level}", True, (255,255,255))
    screen.blit(text, (10,10))

    pygame.display.flip()
    clock.tick(speed)