import pygame
import math
from sys import exit

pygame.init()
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
screen.fill("White")

clock = pygame.time.Clock()

font = pygame.font.Font("font/Pixeltype.ttf", 50)

pygame.display.set_caption("Pixel counter")

start_x = None
start_y = None
end_x = None
end_y = None
start = False
end = False
line_anchor = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()

            if event.key == pygame.K_SPACE:
                start_x = None
                start_y = None
                end_x = None
                end_y = None
                start = False
                end = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and start is False:
                start_x, start_y = event.pos
                start = True

            if event.button == 3 and end is False:
                end_x, end_y = event.pos
                end = True

    if start is False and end is False:
        screen.fill("White")   #NIE UMIM REFRESZA TO ROBIĘ TAK
        instruction_surf = font.render("LMB - start, PMB - end, ESC - exit", False, "Black")
        instruction_rect = instruction_surf.get_rect(midbottom=screen.get_rect().midbottom)
        screen.blit(instruction_surf, instruction_rect)

    if start is True and end is False:
        pygame.draw.line(screen, "Red", (start_x, start_y), pygame.mouse.get_pos(), 10)

    if start is True and end is True:
        screen.fill("White")  #TU TEŻ
        result_w = end_x - start_x
        result_h = end_y - start_y
        result_ac = int(math.sqrt(result_w**2 + result_h**2))
        result_surf = font.render(f"L -> R: {result_w}, U -> D: {result_h}, Diagonal: {result_ac}, space - restart", False, "Black")
        result_rect = result_surf.get_rect(midtop=screen.get_rect().midtop)
        screen.blit(result_surf, result_rect)

    pygame.display.update()
    clock.tick(60)