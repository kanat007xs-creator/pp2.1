import pygame
from datetime import datetime
import tools

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Paint TSIS 2")
    clock = pygame.time.Clock()

    canvas = pygame.Surface((800, 600))
    canvas.fill((255, 255, 255))

    font = pygame.font.SysFont(None, 24)

    mode = 'blue'
    tool = 'brush'

    brush_sizes = [2, 5, 10]
    brush_index = 1
    size = brush_sizes[brush_index]

    drawing = False
    start_pos = None
    last_pos = None
    preview = canvas.copy()

    typing = False
    text_input = ""
    text_pos = None

    while True:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return

            # ========= KEYBOARD =========
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    if typing:
                        typing = False
                        text_input = ""
                    else:
                        return

                # COLORS
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_b:
                    mode = 'blue'

                # BRUSH SIZE
                if event.key == pygame.K_1:
                    brush_index = 0
                if event.key == pygame.K_2:
                    brush_index = 1
                if event.key == pygame.K_3:
                    brush_index = 2

                size = brush_sizes[brush_index]

                # TOOLS
                if event.key == pygame.K_q:
                    tool = 'brush'
                if event.key == pygame.K_w:
                    tool = 'line'
                if event.key == pygame.K_e:
                    tool = 'rect'
                if event.key == pygame.K_c:
                    tool = 'circle'
                if event.key == pygame.K_x:
                    tool = 'eraser'
                if event.key == pygame.K_f:
                    tool = 'fill'
                if event.key == pygame.K_t:
                    tool = 'text'
                if event.key == pygame.K_5:
                    tool = 'square'
                if event.key == pygame.K_6:
                    tool = 'right_triangle'
                if event.key == pygame.K_7:
                    tool = 'equilateral_triangle'
                if event.key == pygame.K_8:
                    tool = 'rhombus'

                # SAVE
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                    pygame.image.save(canvas, filename)
                    print("Saved:", filename)

                # TEXT
                if typing:
                    if event.key == pygame.K_RETURN:
                        text_surface = font.render(text_input, True, tools.get_color(mode))
                        canvas.blit(text_surface, text_pos)
                        typing = False
                        text_input = ""
                    elif event.key == pygame.K_BACKSPACE:
                        text_input = text_input[:-1]
                    else:
                        text_input += event.unicode

            # ========= MOUSE DOWN =========
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                last_pos = event.pos

                if tool == 'fill':
                    tools.flood_fill(canvas, *event.pos, tools.get_color(mode))

                elif tool == 'text':
                    typing = True
                    text_pos = event.pos
                    text_input = ""

                else:
                    drawing = True
                    preview = canvas.copy()

            # ========= MOUSE UP =========
            if event.type == pygame.MOUSEBUTTONUP:
                drawing = False
                end_pos = event.pos
                color = tools.get_color(mode)

                if tool == 'line':
                    tools.draw_line(canvas, color, start_pos, end_pos, size)
                elif tool == 'rect':
                    tools.draw_rect(canvas, color, start_pos, end_pos, size)
                elif tool == 'circle':
                    tools.draw_circle(canvas, color, start_pos, end_pos, size)
                elif tool == 'square':
                    tools.draw_square(canvas, color, start_pos, end_pos, size)
                elif tool == 'right_triangle':
                    tools.draw_right_triangle(canvas, color, start_pos, end_pos, size)
                elif tool == 'equilateral_triangle':
                    tools.draw_equilateral_triangle(canvas, color, start_pos, end_pos, size)
                elif tool == 'rhombus':
                    tools.draw_rhombus(canvas, color, start_pos, end_pos, size)

            # ========= MOUSE MOVE =========
            if event.type == pygame.MOUSEMOTION and drawing:
                color = tools.get_color(mode)

                if tool == 'brush':
                    pygame.draw.line(canvas, color, last_pos, event.pos, size)
                    last_pos = event.pos

                elif tool == 'eraser':
                    pygame.draw.circle(canvas, (255,255,255), event.pos, size*2)

                else:
                    canvas = preview.copy()
                    end_pos = event.pos

                    if tool == 'line':
                        tools.draw_line(canvas, color, start_pos, end_pos, size)
                    elif tool == 'rect':
                        tools.draw_rect(canvas, color, start_pos, end_pos, size)
                    elif tool == 'circle':
                        tools.draw_circle(canvas, color, start_pos, end_pos, size)

        # ========= DRAW =========
        screen.blit(canvas, (0, 0))

        if typing:
            text_surface = font.render(text_input, True, tools.get_color(mode))
            screen.blit(text_surface, text_pos)

        pygame.display.flip()
        clock.tick(60)

main()