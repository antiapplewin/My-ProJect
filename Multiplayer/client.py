import pygame
import time, io
import threading
from network import Network
from player import *

width, height = 1000, 750

class SYS :
    def SetTlistSYS(List, ti) :
        t = int(time.time()*100)/100
        for i in List :
            if t - i[1] >= ti :
                List.remove(i)
            else : break
        
        return List
    
    def DisplayGame(win, cards) :
        if not(cards == []) :
            images = []
            for card in cards :
                img = pygame.image.load(f'./Multiplayer/images/{card}.png')
                img = pygame.transform.scale(img, (img.get_size()[0]*2/3, img.get_size()[1]*2/3))
                print(img.get_size())
                images.append(img)

            for i in range(4) :
                win.blit(images[i], ((width-60-img.get_size()[1])/2+20*i, 600))

def main() :
    n = Network(IPtool)
    g = GameSYS()
    ClientP = n.getP()
    ClientPISend = {'CurrentKey':[], "message":("", 0)}
    keyHistory = []

    recved = n.recv(ClientPISend)
    print(recved['self']['Nickname'])

    run = True
    while run :
        # Recv Part

        recved = n.recv(ClientPISend)
        GotPInfo, GotOInfo = recved['self'], recved['other']

        # print(GotPInfo)

        img = pygame.image.load(io.BytesIO(recved['self']['ServerRecv']['cardsImg']))
        win.blit(img, (0, 0))

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
        if ((PK, int(time.time()*100)/100) not in keyHistory) :
            keyHistory.append((PK, int(time.time()*100)/100))
            ClientPISend['CurrentKey'] = PK
        else :
            ClientPISend['CurrentKey'] = []

        ClientPISend["message"] = g.GetMess()

        # update code
        pygame.display.update()
        keyHistory = SYS.SetTlistSYS(keyHistory, 1)
        SYS.DisplayGame(win, recved['self']['ServerRecv']['card'])

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