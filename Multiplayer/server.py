import socket, os
from _thread import *
from player import *
from SubserverClass import *
import pickle, random
from IPsafe import IPSafe

IP = input("Input short IP : ")

server = IPSafe().GetIP(IP)
port = 28578

players = []
playersChat, ChatLog, images, playings = [], [], [], []
turn, playing = 0, False
pokerGame = {'maincards1':[], 'maincards2':[], "turn":0, 'pot':0, 'ava':True}
SilenceGame = {'maincards2':[], 'checkchip':0}

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
                for i in range(8) :
                    self.cards.append(f"{i+2}{sh}")
                self.cards.append(f"T{sh}")
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
    
    def Combination(pcard, mcard) :
        cards = pcard + mcard
        kind, kicar = "HighCard", ""
        numcardcnt = [] # 문양 / 숫자 / 연속된 숫자
        for _ in range(13) : numcardcnt.append(0)

        for card in cards :
            try :
                numcardcnt[int(card[1])-2] += 1
            except :
                if (card[1]=='T') :numcardcnt[8]+=1
                elif (card[1]=='J') : numcardcnt[9] += 1
                elif (card[1]=='Q') : numcardcnt[10] += 1
                elif (card[1]=='K') : numcardcnt[11] += 1
                else : numcardcnt[12] += 1

        for i in range(13) :
            if (numcardcnt[i]==2) :
                kind = "OnePair"

        return kind

class GameServer :
    def TestPlace(conn, player) :
        global turn, pokerGame, SilenceGame, playing
        avaMove = ['raise', 'bet', 'call', 'all-in', 'all in', 'fold']
        while True :
            try :
                data = pickle.loads(conn.recv(4096)) # Error Occures -> increase 4096

                message, mess = data['message'], (0, "", False)
                if (message not in ChatLog and not(message[0]=="")) :
                    ChatLog.append(message)
                    mess = (player, message[0], True)
                
                playersChat[player] = mess
                Smess = ""

                if ("SP" in players[player].RecvInfo('CurrentKey') and player==0 and not(playing)) :
                    turn = 0
                    playing = True
                    su.SuffleCard(4)
                    for pl in players :
                        if (pl.RecvInfo('SR')['card']==[]) :
                            cards = su.getCard(4)
                            pl.update({"card":cards})
                            pl.update({'showingCard':["CB", "CB", 'CB', 'CB']})
                
                if (playing) :
                    if (players[player].RecvInfo('action')!=() and turn==player) :
                        act = players[player].RecvInfo('action')
                        pokerGame['ava'] = True
                        print(act, turn)
                        if (act[0] not in avaMove) :
                            pokerGame['ava'] = False
                        else :
                            chips = act[1]
                            if (chips!=-1) :
                                try :
                                    if (act[0]=='raise') : SilenceGame['checkchip'] += int(chips)
                                    elif (act[0]=='bet') : SilenceGame['checkchip'] += int(chips)
                                    else : pokerGame['ava'] = False
                                except ValueError :
                                    pokerGame['ava'] = False
                        
                        if (pokerGame['ava']) :
                            pokerGame['pot'] += SilenceGame['checkchip']
                            Smess = "turn passed"
                            turn += 1
                        
                        if (turn>=currentPlayer) :
                            turn = 0
                            if (pokerGame['turn']==0) :
                                pokerGame['maincards1'] = su.getCard(3)
                                pokerGame['maincards2'] = ["CB", "CB", "CB"]
                                SilenceGame['maincards2'] = su.getCard(3)
                                SilenceGame['checkchip'] = 0
                            elif (pokerGame['turn']==1 or pokerGame['turn']==2) :
                                pokerGame['maincards1'].append(su.getCard(1)[0])
                                pokerGame["maincards2"].append('CB')
                                SilenceGame['maincards2'].append(su.getCard(1)[0])
                                SilenceGame['checkchip'] = 0
                            elif (pokerGame['turn']==3) :
                                SilenceGame['checkchip'] = 0
                                for pl in players :
                                    print(ServerClass.Combination(pl.RecvInfo('card'), pokerGame['maincards1']))
                                pokerGame['maincards1'] = []
                                pokerGame['maincards2'] = SilenceGame['maincards2']
                            else :
                                SilenceGame['maincards2'] = []
                                pokerGame['maincards2'] = []
                                pokerGame['turn'] = -1
                                SilenceGame['checkchip'] = 0
                                turn = -1
                                for pl in players :
                                    pl.update({'card':[], 'showingCard':[]})
                                su.SetCards()
                                playing = False
                            pokerGame['turn']+=1
                else :
                    SilenceGame['maincards2'] = []
                    pokerGame['maincards2'] = []
                    pokerGame['turn'] = 0
                    SilenceGame['checkchip'] = 0
                    turn = -1
                    playing = False

                # print(turn)

                recvData = {"self":{}, 'other':[], 'server':[]}

                for i in range(currentPlayer) :
                    if i!=player :
                        temprecv = players[i].RecvData()
                        temprecv['message'] = playersChat[i]
                        if (playersChat[i][2]) :
                            print(temprecv)
                        recvData['other'].append(temprecv)
                recvData['self'] = players[player].RecvPlayer()
                recvData['server'] = {"turn":turn, "mess":Smess, "Info":pokerGame}

                players[player].update(data)
                conn.sendall(pickle.dumps(recvData))
            except :
                break

gs, su = GameServer, ServerClass.ServerUpdate()

def ThreadedClient(conn, player) :
    global currentPlayer
    
    target_folder = "Multiplayer/images"
    img_paths = [os.path.join(target_folder, f) for f in os.listdir(target_folder) if f.endswith(".png")]
    print(img_paths)

    for img_path in img_paths :
        file_size = os.path.getsize(img_path)
        file_size_byte=file_size.to_bytes(4, "big")
         
        print(f"전송 중: {img_path} ({file_size_byte} bytes)")

        #time.sleep(0.1)
        conn.sendall(file_size_byte) 
         
        with open(img_path, 'rb') as f :
             
            while chunk := f.read(4096) :
                conn.sendall(chunk)
                # print(chunk[:16])

        #conn.sendall(b"__END__")
        time.sleep(0.1)


    time.sleep(0.5)
    conn.sendall(b"ImgD")
    print("Every IMG Send")

    time.sleep(0.5)
    conn.sendall(pickle.dumps(img_paths))
    
    gs.TestPlace(conn, player)
    
    players.remove(players[player])
    currentPlayer -= 1

def befSet() :
    pass

befSet()

currentPlayer = 0
while True :
    conn, addr = s.accept()
    print("Connected to : ", addr)
    players.append(PlayerInfo(currentPlayer))
    playersChat.append((currentPlayer, "", False))
    playings.append(False)

    start_new_thread(ThreadedClient, (conn, currentPlayer))

    currentPlayer += 1

'''
목표 없이 방랑하는 느낌이 너무 강하게 든다
그래서 남은 시간동안은 목표를 만들어야겠다

퀘스트
1. 새 퀘스트 기다리기
2. 새 퀘스트 기다리기
3. 새 퀘스트 기다리기
4. 새 퀘스트 기다리기
5. 텍스트로 구분 귀찮다
6. 새 퀘스트 기다리기
7. 플레이어의 돈 저장하기
8. 조합 확인하기
9. 승리 확인하기
10. 팟 나누기
11. 파일로 저장하기

다음 과정은 돈이 소요될 수도 있기에 오늘내로 끝내지 못할 수도 있다

12. 온라인으로 올리기
13. 친구랑 하기
'''