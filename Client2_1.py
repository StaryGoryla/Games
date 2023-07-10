import socket
import threading
import pygame

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("192.168.8.155", 9999))

WIDTH, HEIGHT = 912, 1012


def communicate():
    while True:
        message = client.recv(1024).decode("utf-8")
        if message == "NICK":
            client.send(nickname.encode())
        if message == "INPUT":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        start_x, start_y = event.pos
                        x = start_x % 304
                        y = start_y % 304
                    cords = f"{x}, {y}"
                    client.send(cords.encode())

def run():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        xfield = pygame.image.load("graphics/o1.png").convert_alpha()
        ofield = pygame.image.load("graphics/x1.png").convert_alpha()
        background = pygame.image.load("graphics/tictactoebg.png").convert_alpha()
        pygame.display.set_caption("TTT")
        screen.blit(background, (0, 0))
        pygame.display.update()


communicate_thread = threading.Thread(target=communicate)
run_thread = threading.Thread(target=run)

pygame.init()
communicate_thread.start()
#run_thread.start()