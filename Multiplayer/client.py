import pygame
import time
from _thread import *
from network import Network
from player import *

width, height = 500, 500

def main() :
    n = Network(IPtool)
    ClientP = n.getP()
    ClientPISend = {'CurrentKey':[]}

    # recved = n.recv()

    run = True
    while run :
        # recved = n.send(ClientPISend)
        # print(recved)

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()

        PK = PygameSYS.keyPress()
        if (PK!=[]) :
            ClientPISend['CurrentKey'] = PK
            n.send(ClientPISend)

        win.fill((255, 255, 255))
        pygame.display.update()

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