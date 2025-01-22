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
playersChat = [("", "", False), ("", "", False), ("", "", False), ("", "", False)]
for i in range(4) :
    players.append(Player(0, 0, 50, 50, (0, 255, 0), 5, f"P{i+1}"))
messageLog = []

def ThreadedClient(conn, player) :
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True :
        try :
            data = pickle.loads(conn.recv(2048)) # Error Occures -> increase 2048'
            players[player] = data
            message = players[player].chat()

            mess = ("", "", False)
            if (message not in messageLog and not(message[2]=="" or message[0]=="")) :
                messageLog.append(message)
                mess = (message[2], message[0], True)

            playersChat[player] = mess

            if not data :
                print("Disconnected")
                currentPlayer -= 1
                break
            else :
                reply = []
                for i in range(4) :
                    if player == i :
                        reply.append([])
                        reply.append([])
                        for j in range(4) :
                            if i!=j :
                                reply[0].append(players[j])
                                reply[1].append(playersChat[j])
                
                if not(mess[0]=="") :
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