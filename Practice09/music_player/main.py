import pygame
import sys
import os
from player import MusicPlayer

def main():
    pygame.init()

    WIDTH, HEIGHT = 600, 300
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Music Player")

    font = pygame.font.SysFont(None, 36)

    music_folder = os.path.join(os.path.dirname(__file__), "music")
    player = MusicPlayer(music_folder)

    clock = pygame.time.Clock()

    running = True
    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    player.play()
                elif event.key == pygame.K_s:
                    player.stop()
                elif event.key == pygame.K_n:
                    player.next_track()
                elif event.key == pygame.K_b:
                    player.prev_track()
                elif event.key == pygame.K_q:
                    running = False

        # Текущий трек
        track_text = font.render(f"Track: {player.get_current_track_name()}", True, (255, 255, 255))
        screen.blit(track_text, (20, 50))

        # Позиция
        pos = player.get_position()
        time_text = font.render(f"Time: {pos} sec", True, (200, 200, 200))
        screen.blit(time_text, (20, 100))

        # Управление
        controls = [
            "P - Play",
            "S - Stop",
            "N - Next",
            "B - Previous",
            "Q - Quit"
        ]

        for i, text in enumerate(controls):
            ctrl_text = font.render(text, True, (150, 150, 150))
            screen.blit(ctrl_text, (20, 150 + i * 25))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()