import pygame
import math
from collections import deque

def get_color(mode):
    return {
        'blue': (0, 0, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0)
    }[mode]


def draw_line(surface, color, start, end, size):
    pygame.draw.line(surface, color, start, end, size)


def draw_rect(surface, color, start, end, size):
    pygame.draw.rect(surface, color,
        pygame.Rect(start, (end[0]-start[0], end[1]-start[1])), size)


def draw_circle(surface, color, start, end, size):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    r = int((dx**2 + dy**2) ** 0.5)
    pygame.draw.circle(surface, color, start, r, size)


def draw_square(surface, color, start, end, size):
    side = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
    pygame.draw.rect(surface, color, pygame.Rect(start, (side, side)), size)


def draw_right_triangle(surface, color, start, end, size):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, color, points, size)


def draw_equilateral_triangle(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end
    side = abs(x2 - x1)
    height = side * math.sqrt(3) / 2

    p1 = (x1, y1)
    p2 = (x1 + side, y1)
    p3 = (x1 + side/2, y1 - height)

    pygame.draw.polygon(surface, color, [p1, p2, p3], size)


def draw_rhombus(surface, color, start, end, size):
    x1, y1 = start
    x2, y2 = end

    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2

    points = [(cx, y1),(x2, cy),(cx, y2),(x1, cy)]
    pygame.draw.polygon(surface, color, points, size)


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))
    if target_color == new_color:
        return

    w, h = surface.get_size()
    queue = deque([(x, y)])

    while queue:
        px, py = queue.popleft()

        if px < 0 or px >= w or py < 0 or py >= h:
            continue
        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        queue.append((px+1, py))
        queue.append((px-1, py))
        queue.append((px, py+1))
        queue.append((px, py-1))