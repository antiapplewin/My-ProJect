import socket
from _thread import *
from player import Player
import pickle

server = "192.168.0.50"
port = 28578

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # No Argument : Unlimited
print("Waiting For a Connection, Server Started")

players = [] # Player(0, 0, 50, 50, (255, 0, 0), 3, "P1")
for i in range(4) :
    players.append(Player(0, 0, 50, 50, (0, 255, 0), 5, f"P{i+1}"))

def ThreadedClient(conn, player) :
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True :
        try :
            data = pickle.loads(conn.recv(2048)) # Error Occures -> increase 2048'
            players[player] = data

            if not data :
                print("Disconnected")
                currentPlayer -= 1
                break
            else :
                if player == 1 :
                    reply = players[0]
                else :
                    reply = players[1]
                
                print("Received : ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except :
            break

currentPlayer = 0
while True :
    conn, addr = s.accept()
    print("Connected to : ", addr)

    start_new_thread(ThreadedClient, (conn, currentPlayer))

    currentPlayer += 1