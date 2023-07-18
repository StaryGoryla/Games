import socket
from _thread import *
import sys
import random

server = "localhost"
port = 9990

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

connections = []
addresses = []
nicknames = []

def start_server():
    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    print("Server is listening")


def accept_players():
    try:
        for i in range(2):
            global connection
            connection, address = s.accept()
            print("Connected to: ", address)
            message = "Welcome to the server"
            connection.send(message.encode())
            connections.append(connection)
    except socket.error as e:
        print(e)


def setup():
    random.shuffle(connections)
    for i in range(2):
        player = connections[i]
        player.send("NICKNAME".encode())
        nickname = player.recv(1024)
        nicknames.append(nickname)


def broadcast(message, clients):
    for client in clients:
        client.send(message.encode())


def game():
    current_turn = 0
    while True:
        player = connections[current_turn]
        player.send("INPUT".encode())
        response = player.recv(1024).decode()
        print(f"{nicknames[current_turn]} chose {response}.")
        message = f"{nicknames[current_turn]} chose {response}"
        broadcast(message, connections)
        current_turn = (current_turn + 1) % 2


start_server()
accept_players()
setup()
game()
