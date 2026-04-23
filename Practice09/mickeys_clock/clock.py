import pygame
import math
import datetime
import os
 
 
class MickeyClock:
    """
    Mickey Mouse Clock.
    Правая рука = минуты, Левая рука = секунды.
    """
 
    def __init__(self, screen_width=600, screen_height=600):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2
 
        self.WHITE      = (255, 255, 255)
        self.BLACK      = (0,   0,   0  )
        self.CREAM      = (255, 248, 220)
        self.DARK_GRAY  = (60,  60,  60 )
        self.RED        = (200, 30,  30 )
        self.LIGHT_GRAY = (200, 200, 200)
 
        self.clock_radius = 240
 
        pygame.font.init()
        self.font_large  = pygame.font.SysFont("Arial", 32, bold=True)
        self.font_medium = pygame.font.SysFont("Arial", 22, bold=True)
        self.font_small  = pygame.font.SysFont("Arial", 16)
 
        # Загружаем изображения рук (70x154 px)
        self.right_hand_img = self._load_image("images/right_hand.png", (70, 154))
        self.left_hand_img  = self._load_image("images/left_hand.png",  (70, 154))
 
    # ------------------------------------------------------------------ #
    def _load_image(self, rel_path, size):
        """Ищет PNG рядом с этим файлом или в mickeys_clock/."""
        base = os.path.dirname(os.path.abspath(__file__))
        candidates = [
            os.path.join(base, rel_path),
            rel_path,
            os.path.join("mickeys_clock", rel_path),
        ]
        for p in candidates:
            if os.path.exists(p):
                try:
                    img = pygame.image.load(p).convert_alpha()
                    img = pygame.transform.smoothscale(img, size)
                    print(f"  OK: {p}")
                    return img
                except Exception as e:
                    print(f"  ERR {p}: {e}")
        print(f"  NOT FOUND: {rel_path}")
        return None
 
    # ------------------------------------------------------------------ #
    def get_time(self):
        now = datetime.datetime.now()
        return now.hour, now.minute, now.second
 
    @staticmethod
    def _minute_angle(minutes, seconds):
        """0 мин → 0° (вверх), по часовой стрелке."""
        return (minutes * 60 + seconds) / 3600.0 * 360.0
 
    @staticmethod
    def _second_angle(seconds):
        return seconds / 60.0 * 360.0
 
    # ------------------------------------------------------------------ #
    def _draw_hand(self, surface, img, angle_deg, pivot):
        """
        Рисует руку.
 
        Наш PNG устроен так:
          - верх (y=0)        → кончики пальцев (далеко от центра)
          - низ (y=height-1)  → запястье / точка крепления к телу
 
        Поворот: angle_deg=0 → рука указывает ВВЕРХ (на 12 часов).
        Поворот по часовой стрелке.
        """
        if img:
            self._draw_rotated_hand(surface, img, angle_deg, pivot)
        else:
            self._draw_line_hand(surface, angle_deg, pivot)
 
    def _draw_rotated_hand(self, surface, img, angle_deg, pivot):
        """
        Вращаем изображение так, чтобы запястье (низ PNG) находилось
        в точке pivot, а пальцы смотрели в нужном направлении.
 
        Алгоритм:
          1. pygame.transform.rotate поворачивает вокруг центра изображения.
          2. Мы вычисляем, куда сдвинулся центр картинки относительно запястья
             после поворота, и позиционируем blit так, чтобы запястье = pivot.
        """
        iw, ih = img.get_size()          # 70, 154
 
        # Вектор «от запястья до центра изображения» в локальных координатах
        # (при angle=0 изображение стоит прямо: пальцы вверх, запястье внизу)
        #   центр px = (iw/2, ih/2)   запястье = (iw/2, ih)
        #   вектор = (0, -ih/2)  т.е. прямо вверх
        local_cx = 0.0
        local_cy = -ih / 2.0
 
        # После поворота на angle_deg по часовой стрелке:
        rad = math.radians(angle_deg)
        rot_cx =  local_cx * math.cos(rad) + local_cy * math.sin(rad)
        rot_cy = -local_cx * math.sin(rad) + local_cy * math.cos(rad)
 
        # Центр повёрнутого изображения в экранных координатах
        draw_center = (pivot[0] + rot_cx, pivot[1] + rot_cy)
 
        rotated = pygame.transform.rotate(img, -angle_deg)
        rect = rotated.get_rect(center=(int(draw_center[0]), int(draw_center[1])))
        surface.blit(rotated, rect)
 
    def _draw_line_hand(self, surface, angle_deg, pivot):
        """Запасная стрелка — линия с белым шариком на конце."""
        rad = math.radians(angle_deg - 90)
        length = 155
        ex = pivot[0] + length * math.cos(rad)
        ey = pivot[1] + length * math.sin(rad)
        tx = pivot[0] - 35 * math.cos(rad)
        ty = pivot[1] - 35 * math.sin(rad)
        pygame.draw.line(surface, self.BLACK, (int(tx), int(ty)), (int(ex), int(ey)), 10)
        pygame.draw.line(surface, self.WHITE, (int(tx), int(ty)), (int(ex), int(ey)), 6)
        pygame.draw.circle(surface, self.WHITE, (int(ex), int(ey)), 13)
        pygame.draw.circle(surface, self.BLACK, (int(ex), int(ey)), 13, 2)
 
    # ------------------------------------------------------------------ #
    def draw_clock_face(self, surface):
        cx, cy = self.center_x, self.center_y
        r = self.clock_radius
 
        # Ободок
        pygame.draw.circle(surface, (180, 180, 185), (cx, cy), r + 18)
        pygame.draw.circle(surface, (220, 220, 225), (cx, cy), r + 12)
        pygame.draw.circle(surface, (40,  40,  45 ), (cx, cy), r + 8)
        pygame.draw.circle(surface, self.CREAM,       (cx, cy), r)
 
        # Лучи
        for i in range(24):
            a = math.radians(i * 15 - 90)
            r1, r2 = r * 0.35, r * 0.92
            pygame.draw.line(surface, (230, 220, 180),
                             (int(cx + r1*math.cos(a)), int(cy + r1*math.sin(a))),
                             (int(cx + r2*math.cos(a)), int(cy + r2*math.sin(a))), 2)
 
        # Цифры 1–12
        for h in range(1, 13):
            a = math.radians(h * 30 - 90)
            txt = self.font_large.render(str(h), True, self.DARK_GRAY)
            surface.blit(txt, txt.get_rect(
                center=(int(cx + r*0.80*math.cos(a)), int(cy + r*0.80*math.sin(a)))))
 
        # Риски
        for m in range(60):
            a = math.radians(m * 6 - 90)
            if m % 5 == 0:
                r1, r2, col, w = 0.88, 0.97, self.DARK_GRAY, 3
            else:
                r1, r2, col, w = 0.92, 0.97, (130, 130, 130), 1
            pygame.draw.line(surface, col,
                             (int(cx + r*r1*math.cos(a)), int(cy + r*r1*math.sin(a))),
                             (int(cx + r*r2*math.cos(a)), int(cy + r*r2*math.sin(a))), w)
 
    # ------------------------------------------------------------------ #
    def draw_mickey_body(self, surface):
        cx, cy = self.center_x, self.center_y
 
        # Туловище
        pygame.draw.ellipse(surface, self.RED,   pygame.Rect(cx-45, cy-10, 90, 80))
        pygame.draw.ellipse(surface, self.BLACK, pygame.Rect(cx-45, cy-10, 90, 80), 2)
        for bx in [cx-12, cx+12]:
            pygame.draw.circle(surface, (240, 240, 255), (bx, cy+30), 6)
            pygame.draw.circle(surface, self.BLACK, (bx, cy+30), 6, 1)
 
        # Ноги / ботинки
        for lx in [cx-22, cx+22]:
            pygame.draw.ellipse(surface, self.BLACK, pygame.Rect(lx-14, cy+60, 28, 55))
            pygame.draw.ellipse(surface, self.BLACK, pygame.Rect(lx-22, cy+100, 44, 24))
            pygame.draw.ellipse(surface, self.WHITE, pygame.Rect(lx-20, cy+102, 40, 20))
 
        # Голова
        pygame.draw.circle(surface, self.BLACK, (cx, cy-55), 52)
        pygame.draw.circle(surface, (245, 220, 195), (cx, cy-55), 48)
        for ex in [cx-42, cx+42]:
            pygame.draw.circle(surface, self.BLACK, (ex, cy-95), 28)
 
        # Глаза
        for dx in [-15, 15]:
            pygame.draw.ellipse(surface, self.WHITE, pygame.Rect(cx+dx-10, cy-68, 20, 22))
            pygame.draw.circle(surface, self.BLACK, (cx+dx, cy-58), 6)
            pygame.draw.circle(surface, self.WHITE, (cx+dx+2, cy-61), 2)
 
        # Нос, улыбка, рот
        pygame.draw.ellipse(surface, self.BLACK, pygame.Rect(cx-10, cy-44, 20, 13))
        pygame.draw.arc(surface, self.BLACK, pygame.Rect(cx-20, cy-38, 40, 25),
                        math.radians(200), math.radians(340), 3)
        pygame.draw.ellipse(surface, self.WHITE, pygame.Rect(cx-15, cy-30, 30, 14))
        pygame.draw.line(surface, self.BLACK, (cx, cy-30), (cx, cy-16), 1)
        pygame.draw.ellipse(surface, self.RED, pygame.Rect(cx-10, cy-23, 20, 10))
 
    # ------------------------------------------------------------------ #
    def draw(self, surface):
        hours, minutes, seconds = self.get_time()
 
        surface.fill((240, 240, 245))
        self.draw_clock_face(surface)
        self.draw_mickey_body(surface)
 
        # Точка вращения — центр тела Микки
        pivot = (self.center_x, self.center_y - 20)
 
        # Правая рука = МИНУТЫ
        self._draw_hand(surface, self.right_hand_img,
                        self._minute_angle(minutes, seconds), pivot)
 
        # Левая рука = СЕКУНДЫ
        self._draw_hand(surface, self.left_hand_img,
                        self._second_angle(seconds), pivot)
 
        # Центральная точка поверх рук
        pygame.draw.circle(surface, self.BLACK,  pivot, 10)
        pygame.draw.circle(surface, (80, 80, 80), pivot, 6)
 
        # Цифровое время
        ts = self.font_medium.render(
            f"{hours:02d}:{minutes:02d}:{seconds:02d}", True, self.DARK_GRAY)
        surface.blit(ts, ts.get_rect(center=(self.center_x, self.screen_height - 30)))
 
        lbl = self.font_small.render(
            "← секунды  |  минуты →", True, (120, 120, 120))
        surface.blit(lbl, lbl.get_rect(center=(self.center_x, self.screen_height - 12)))
