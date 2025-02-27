import socket
from _thread import *
from player import *
from SubserverClass import *
import pickle, random
from IPsafe import IPSafe

IP = input("Input short IP : ")

server = IPSafe().GetIP(IP)
port = 28578

players = []
playersChat, ChatLog, images = [], [], []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try :
    s.bind((server, port))
except socket.error as e:
    print(str(e))

s.listen() # No Argument : Unlimited
print("Waiting For a Connection, Server Started")

GameIPs = ['1:test']

class ServerClass :
    class ServerUpdate :
        def __init__(self) :
            self.cards = []
            self.SetCards()

        def SetCards(self) :
            self.cards = []
            shape = ["♥️", "♠️", "♦️", "♣️"]
            for sh in shape :
                self.cards.append(f"A{sh}")
                for i in range(9) :
                    self.cards.append(f"{i+2}{sh}")
                self.cards.append(f"J{sh}")
                self.cards.append(f"Q{sh}")
                self.cards.append(f"K{sh}")

        def getCard(self, number) :
            card = []
            for _ in range(number) :
                card.append(self.cards[0])
                self.cards.remove(self.cards[0])
            return card
        
        def SuffleCard(self, much) :
            for _ in range(much) :
                random.shuffle(self.cards)

class GameServer :
    def TestPlace(conn, player) :
        print(player)
        while True :
            try :
                data = pickle.loads(conn.recv(2048)) # Error Occures -> increase 2048

                if (players[player].RecvInfo('CurrentKey')) :
                    print(f"{player} : {players[player].RecvPlayer()}")

                message, mess = data['message'], (0, "", False)
                if (message not in ChatLog and not(message[0]=="")) :
                    ChatLog.append(message)
                    mess = (player, message[0], True)
                
                playersChat[player] = mess

                if ("Kr" in players[player].RecvInfo('CurrentKey')) :
                    su.SuffleCard(4)
                    print("!!!")
                    for pl in players :
                        if (pl.RecvInfo('ServerRecv')['card']==[]) :
                            cards = su.getCard(4)
                            pl.update({"card":cards})
                        print(pl.RecvInfo('ServerRecv'))
                if ("Kq" in players[player].RecvInfo('CurrentKey')) :
                    players[player].update({"card":[]})
                    su.SetCards()
                    print(player)

                players[player].update({'cardsImg':images[0]})

                recvData = {"self":{}, 'other':[]}

                for i in range(currentPlayer) :
                    if i!=player :
                        temprecv = players[i].RecvData()
                        temprecv['message'] = playersChat[i]
                        if (playersChat[i][2]) :
                            print(temprecv)
                        recvData['other'].append(temprecv)
                recvData['self'] = players[player].RecvPlayer()

                players[player].update(data)
                conn.sendall(pickle.dumps(recvData))
            except :
                break

gs, su = GameServer, ServerClass.ServerUpdate()

def ThreadedClient(conn, player) :
    global currentPlayer
    conn.send(pickle.dumps(players[player]))
    
    gs.TestPlace(conn, player)
    
    currentPlayer -= 1

def befSet() :
    with open("Multiplayer/images/PokerTable.png", 'rb') as f :
        images.append(f.read())

befSet()

currentPlayer = 0
while True :
    conn, addr = s.accept()
    print("Connected to : ", addr)
    players.append(PlayerInfo(currentPlayer))
    playersChat.append((currentPlayer, "", False))

    start_new_thread(ThreadedClient, (conn, currentPlayer))

    currentPlayer += 1

# "rect":(0, 0, 50, 50),"extra":[(0, 255, 0), 5, f"P{currentPlayer+3}"]