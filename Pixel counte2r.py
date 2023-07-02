import pygame
import math
from sys import exit

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

screen.fill((255, 255, 255))

pygame.display.set_caption("Pixel counter")
clock = pygame.time.Clock()

instruction_font = pygame.font.Font(None, 50)

result_w = 0
result_h = 0
result_ac = 0

start_x = None
start_y = None
end_x = None
end_y = None
start = False
end = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
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
                print(start_x)
                print(start_y)
            if event.button == 3 and end is False:
                end_x, end_y = event.pos
                end = True

    print(start)
    print(end)
    if start is True and end is True:
        result_w = end_x - start_x
        result_h = end_y - start_y
        print(result_w)
        print(result_h)
        result_ac = int(math.sqrt(result_w**2 + result_h**2))
        result_surf = instruction_font.render(f"L -> R: {result_w}, U -> D: {result_h}, Diagonal: {result_ac}", False,
                                              "Black")
        result_rect = result_surf.get_rect(midtop=screen.get_rect().midtop)
        screen.blit(result_surf, result_rect)

    if start is False and end is False:
        instruction_surf = instruction_font.render("LMB - start, PMB - end, ESC - exit, space - restart", False,
                                                   "Black")
        instruction_rect = instruction_surf.get_rect(midbottom=screen.get_rect().midbottom)
        screen.blit(instruction_surf, instruction_rect)



    pygame.display.update()
    clock.tick(60)