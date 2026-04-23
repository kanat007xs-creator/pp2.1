import pygame
import sys
from clock import MickeyClock
 
 
def main():
    pygame.init()
 
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 640
    FPS = 60
 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Mickey's Clock 🎉")
 
    # Иконка окна — маленький круг (если нет .ico файла)
    try:
        icon = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.circle(icon, (0, 0, 0), (16, 16), 15)
        pygame.draw.circle(icon, (255, 248, 220), (16, 16), 12)
        pygame.display.set_icon(icon)
    except Exception:
        pass
 
    clock = MickeyClock(SCREEN_WIDTH, SCREEN_HEIGHT - 40)
    tick = pygame.time.Clock()
 
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    running = False
 
        # Отрисовка
        clock.draw(screen)
        pygame.display.flip()
        tick.tick(FPS)
 
    pygame.quit()
    sys.exit()
 
 
if __name__ == "__main__":
    main()