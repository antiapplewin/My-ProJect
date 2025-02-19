import socket
from _thread import *
from player import *
from SubserverClass import *
import pickle
from IPsafe import IPSafe

IP = input("Input short IP : ")

server = IPSafe().GetIP(IP)
port = 28578

players = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # No Argument : Unlimited
print("Waiting For a Connection, Server Started")

GameIPs = ['1:test']
messageLog, DidRandom, DRcount = [], [], 0

TPGD = {}

class ServerUpdate :
    pass

class GameServer :
    def TestPlace(conn, player) :
        global DRcount
        while True :
            try :
                data = pickle.loads(conn.recv(2048)) # Error Occures -> increase 2048

                print(data)

                if (data==-1) :
                    # recvData = {"self":[], 'other':[]}

                    # for i in range(currentPlayer) :
                    #     if i!=player :
                    #         recvData['other'].append(players[i].RecvData())

                    conn.sendall(pickle.dumps(1))
                else :
                    players[0].update(data)
            except :
                break

gs = GameServer

def ThreadedClient(conn, player) :
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    
    gs.TestPlace(conn, player)
    
    currentPlayer -= 1


currentPlayer = 0
while True :
    conn, addr = s.accept()
    print("Connected to : ", addr)
    players.append(PlayerInfo(currentPlayer))

    start_new_thread(ThreadedClient, (conn, currentPlayer))

    currentPlayer += 1

# "rect":(0, 0, 50, 50),"extra":[(0, 255, 0), 5, f"P{currentPlayer+3}"]