import pygame
import time, io
import threading
from network import Network
from player import *
from PIL import Image

width, height = 1000, 750

recvedImg, imagesName = [], []

class SYS :
    def SetTlistSYS(List, ti) :
        t = int(time.time()*100)/100
        for i in List :
            if t - i[1] >= ti :
                List.remove(i)
            else : break
        
        return List
    
    def DisplayGame(win, cards, x, y) :
        global imagesName, recvedImg
        if not(cards == []) :
            tc = 0
            for card in cards :
                index = imagesName.index(card+".png")
                win.blit(recvedImg[index], (x+60*tc, y))
                tc += 1

def main() :
    global imagesName, recvedImg
    n = Network(IPtool)
    g = GameSYS()
    ClientP = n.getP()
    ClientPISend = {'CurrentKey':[], "message":("", 0)}
    keyHistory, scroll = [], 0

    image_number = 0

    while True :
        file_size_bytes = n.temprecv(4, use_pickle=False)
        if not file_size_bytes:
            break
        file_size = int.from_bytes(file_size_bytes, 'big')

        recvedData = file_size_bytes #file_size_bytes
        while len(recvedData) < file_size :
            packet = n.temprecv(4096, use_pickle=False)
            if not packet:
                break
            recvedData += packet

            # 종료 신호를 받으면 중단
            if b"__END__" in packet:
                recvedData = recvedData.replace(b"__END__", b"")
                image_number+=1
                break
            
        try :
            image = Image.open(io.BytesIO(recvedData)).convert('RGB')
            img = pygame.image.fromstring(image.tobytes(), image.size, image.mode)
            recvedImg.append(img)
            print(f"Total Img : {len(recvedImg)}")
        except Exception as e :
            print(e)
            with open(f"recvedimg_{image_number}.png", 'wb') as f :
                f.write(recvedData)

        done_signal = n.temprecv(8, use_pickle=False)
        if done_signal == b"Img_Done" :
            print("Every Img Recieved")
            break

    imagesName = n.temprecv(4096, use_pickle=True)
    for i in range(len(imagesName)) :
        imagesName[i] = imagesName[i].replace("Multiplayer/images\\", "")
    print(imagesName)

    run = True
    while run : # GAME DISPLAY!!!
        # Recv Part

        recved = n.recv(ClientPISend)
        GotPInfo, GotOInfo = recved['self'], recved['other']

        # print(GotPInfo)

        for i in GotOInfo :
            if (i['message'][1]!="") :
                print(f"Player : {i['message'][1]}")

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()

        # Sending Part

        PK = PygameSYS.keyPress()
        if ("Kt" in PK) :
            threading.Thread(target=g.ChatInput, args=()).start()
        if ("AU" in PK) :
            if (scroll>0) : scroll-=1
        if ("AD" in PK) :
            if (scroll<len(GotOInfo)-2) : scroll+=1
        if ((PK, int(time.time()*100)/100) not in keyHistory) :
            keyHistory.append((PK, int(time.time()*100)/100))
            ClientPISend['CurrentKey'] = PK
        else :
            ClientPISend['CurrentKey'] = []

        ClientPISend["message"] = g.GetMess()

        # # update code
        pygame.display.update()
        keyHistory = SYS.SetTlistSYS(keyHistory, 1)
        SYS.DisplayGame(win, GotPInfo['SR']['card'], 0, 0)
        if (len(GotOInfo)<=3) :
            for i in range(len(GotOInfo)) :
                SYS.DisplayGame(win, GotOInfo[i]['showingCard'], 0, 198+198*i)
        else :
            for i in range(3) :
                SYS.DisplayGame(win, GotOInfo[scroll+i]['showingCard'], 0, 198+198*i)

IPtool = input("Input IP : ")

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.init()

main()

'''
def redrawWindow(win, players) :
    win.fill((255, 255, 255))
    Font = pygame.font.SysFont("arial", 14, True, False)
    for player in players :
        if (players.index(player) == 0) :
            player.draw(win)
            player.write(win, Font)
        else :
            for play in player :
                play.draw(win)
                play.write(win, Font)
    # players[0].write(win, Font) # outside the for : only private text
    pygame.display.update()

def main() :
    run = True
    n = Network(IPtool)
    players = []
    players.append(n.getP())
    receive = n.send(players[0])
    for i in range(3) :
        players.append(receive[0])

    playerInfo = players[0].GetPlayerInfo()
    
    clock = pygame.time.Clock()

    while run :
        clock.tick(60)
        receive = n.send(players[0])
        for i in range(3) :
            players[i+1] = receive[0]

        message = receive[1]
        for mess in message :
            SelfText = ""
            if playerInfo['P_number'] == mess[0] :
                SelfText = "(You)"
            if (mess[2]) :
                print(f"{mess[0]}{SelfText} : {mess[1]}")

        if receive[2][0]+1 :
            print(receive[2][0])

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()

        players[0].move()
        redrawWindow(win, players)
'''