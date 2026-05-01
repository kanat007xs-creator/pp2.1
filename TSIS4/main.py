import pygame, sys
from game import Game
from db import *
from config import *

pygame.init()

screen = pygame.display.set_mode((600,600))
font = pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()

settings = load_settings()

state = "menu"
username = ""
game = None
pid = None
best = 0


def text(t,x,y):
    screen.blit(font.render(t,True,(255,255,255)),(x,y))


while True:
    screen.fill((0,0,0))

    # ================= MENU =================
    if state == "menu":
        text("ENTER NAME:",200,200)
        text(username,200,240)
        text("ENTER = PLAY | L = LEADERBOARD | S = SETTINGS",50,300)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN and username:
                    pid = get_player(username)
                    best = best_score(pid)
                    game = Game(settings)
                    state = "game"

                elif e.key == pygame.K_l:
                    state = "leaderboard"

                elif e.key == pygame.K_s:
                    state = "settings"

                elif e.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                else:
                    username += e.unicode

    # ================= GAME =================
    elif state == "game":
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    game.dir = (0,-20)
                if e.key == pygame.K_DOWN:
                    game.dir = (0,20)
                if e.key == pygame.K_LEFT:
                    game.dir = (-20,0)
                if e.key == pygame.K_RIGHT:
                    game.dir = (20,0)

        if not game.update():
            save_game(pid, game.score, game.level)
            state = "gameover"

        game.draw(screen)

        text(f"Score:{game.score}",10,10)
        text(f"Level:{game.level}",10,40)
        text(f"Best:{best}",10,70)

        clock.tick(game.speed)

    # ================= GAME OVER =================
    elif state == "gameover":
        text("GAME OVER",220,200)
        text(f"SCORE {game.score}",220,250)
        text("R = RESTART | M = MENU",180,300)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    game.reset()
                    state = "game"
                if e.key == pygame.K_m:
                    state = "menu"
                    username = ""

    # ================= LEADERBOARD =================
    elif state == "leaderboard":
        text("TOP 10",250,20)
        data = leaderboard()

        y = 60
        for i,row in enumerate(data):
            text(f"{i+1}. {row[0]} {row[1]} pts L{row[2]}",50,y)
            y += 30

        text("B = BACK",250,550)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_b:
                    state = "menu"

    # ================= SETTINGS =================
    elif state == "settings":
        text("SETTINGS",250,50)
        text("G = GRID TOGGLE",200,120)
        text("S = SAVE & BACK",200,160)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_g:
                    settings["grid"] = not settings["grid"]

                if e.key == pygame.K_s:
                    save_settings(settings)
                    state = "menu"

    pygame.display.flip()