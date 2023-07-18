import socket
import threading
import pygame
import time

server = "localhost"
port = 9997

running = True
WIDTH, HEIGHT = 912, 1012
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#xfield = pygame.image.load("graphics/o1.png").convert_alpha()
#ofield = pygame.image.load("graphics/x1.png").convert_alpha()
#background = pygame.image.load("graphics/tictactoebg.png").convert_alpha()
#pygame.display.set_caption("TTT")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((server, port))
    print("Connected to " + server)
    message = s.recv(1024)
    print(message)
except:
    print("An error occurred")


def create_thread(target):
    t = threading.Thread(target = target)
    t.daemon = True
    t.start()


def communication():
    while True:
            ser_cli = s.recv(1024).decode()
            if ser_cli == "NICKNAME":
                client_input = input("What's your nickname? ")
                s.send(client_input.encode())
                break
            if ser_cli == "INPUT":
                #for event in pygame.event.get():
                    #if event.type == pygame.MOUSEBUTTONDOWN:
                        #if event.button == 1:
                            #start_x, start_y = event.pos
                            #x = start_x % 304
                            #y = start_y % 304
                            y = input("go")
                            s.send(y.encode())
            else:
                print(ser_cli)


def game():
    create_thread(communication)
    while True:
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #pygame.quit()
        print("Waiting 7 seconds")
        time.sleep(7)


communication()
#pygame.init()
#screen.blit(background, (0, 0))
#pygame.display.update()
game()
