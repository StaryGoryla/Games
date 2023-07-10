import socket
import threading
import random

host = "192.168.8.155"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

clients = []
nicknames = []
symbols = ["X", "O"]
num_clients = 0
running = True
turn_counter = 1


def client_accepting():
    global num_clients

    while running:
        if num_clients < 2:
            client, address = server.accept()
            print("Connected with ", client)
            client.send(f"Connected to the server!".encode())
            clients.append(client)
            num_clients += 1
        else:
            break
    print("Two players connected, starting the game.")

def broadcast(message):
    for client in clients:
        client.send(message.encode())


def setup():
    random.shuffle(clients)
    print(clients)
    for client in clients:
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()
        nicknames.append(nickname)
        print(nicknames)


def run():
    while True:
        for i in range(num_clients):
            client = clients[i]
            nickname = nicknames[i]
            symbol = symbols[i]
            client.send("INPUT".encode())
            cords = client.recv(1024).decode()
            print(nickname, "chose ", symbol, "in ", cords)


server.listen(2)
client_accepting()
setup()
print(clients, nicknames)
broadcast(f"{nicknames[0]} playing as X vs {nicknames[1]} playing as O!")
run()
