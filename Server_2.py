import socket
from _thread import *
import sys
import random

server = "localhost"
port = 9999

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
            connection, address = s.accept()
            print("Connected to: ", address)
            connection.send("NICKNAME".encode())
            nickname = connection.recv(1024)
            message = "Welcome to the server, " + str(nickname)
            connection.send(message.encode())
            addresses.append(address)
            connections.append(connection)
            nicknames.append(nickname)
    except socket.error as e:
        print(e)


def game(i):
    for i in range(2):
        while True:
            player = connections[i]
            player.send("INPUT".encode())
            data = player.recv(1024)
            print(data)


start_server()
accept_players()
print(connections)
print(addresses)
print(nicknames)
game(random.randint(0, 1))
