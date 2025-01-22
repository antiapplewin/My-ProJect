import pygame
from network import Network
from player import Player

width, height = 500, 500

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")
pygame.init()

def redrawWindow(win, players) :
    win.fill((255, 255, 255))
    Font = pygame.font.SysFont("arial", 30, True, False)
    for player in players :
        if (players.index(player) == 0) :
            player.draw(win)
        else :
            for play in player :
                play.draw(win)
    players[0].write(win, Font)
    pygame.display.update()

def main() :
    run = True
    n = Network()
    players = []
    players.append(n.getP())
    receive = n.send(players[0])
    for i in range(3) :
        players.append(receive[0])
    clock = pygame.time.Clock()

    while run :
        clock.tick(60)
        receive = n.send(players[0])
        for i in range(3) :
            players[i+1] = receive[0]

        message = receive[1]
        for mess in message :
            if (mess[2]) :
                print(f"{mess[0]} : {mess[1]}")

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()

        players[0].move()
        redrawWindow(win, players)
main()