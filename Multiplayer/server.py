import socket
from _thread import *
from player import *
import pickle
from IPsafe import IPSafe
import random

IP = input("Input short IP : ")

server = IPSafe().GetIP(IP)
port = 28578

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # No Argument : Unlimited
print("Waiting For a Connection, Server Started")

MainPlayerFile, players = [], []
GameIPs = ['2:Number']
playersChat = [("", "", False), ("", "", False), ("", "", False), ("", "", False)]
# players.append(Player(0, 0, 50, 50, (0, 255, 0), 5, f"P1"))
MainPlayerFile.append(Player({"GameIP":"2:Number", "playerSetting":{'IsOwner':True, 'PNumber':"P1"}}))
MainPlayerFile.append(Player({"GameIP":"2:Number", "playerSetting":{'IsOwner':False, 'PNumber':"P2"}}))
players.append(MainPlayerFile[0].GetGameAddress())
players.append(MainPlayerFile[1].GetGameAddress())
messageLog = []

def ThreadedClient(conn, player) :
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    while True :
        try :
            reply = [[], []]
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
                break
            else :
                for i in range(currentPlayer) :
                    if player == i :
                        reply.append([])
                        reply.append([])
                        for j in range(currentPlayer) :
                            if i!=j and MainPlayerFile[i].GetGameIP() == MainPlayerFile[j].GetGameIP() :
                                reply[0].append(players[j])
                            if MainPlayerFile[i].GetGameIP() == MainPlayerFile[j].GetGameIP() :
                                reply[1].append(playersChat[j])
                
                if not(mess[0]=="") :
                    print("Received : ", data)
                    print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except :
            break
    
    currentPlayer -= 1

print(players)

currentPlayer = 0
while True :
    conn, addr = s.accept()
    print("Connected to : ", addr)
    MainPlayerFile.append(Player({"GameIP":random.choice(GameIPs), "playerSetting":{'IsOwner':False, 'PNumber':f"P{currentPlayer+3}"}}))
    players.append(MainPlayerFile[currentPlayer+2].GetGameAddress())

    start_new_thread(ThreadedClient, (conn, currentPlayer))

    currentPlayer += 1

# "rect":(0, 0, 50, 50),"extra":[(0, 255, 0), 5, f"P{currentPlayer+3}"]