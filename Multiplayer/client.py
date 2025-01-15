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
        player.draw(win)
    players[0].write(win, Font)
    pygame.display.update()

def main() :
    run = True
    n = Network()
    players = []
    players.append(n.getP())
    for i in range(3) :
        players.append(n.send(players[0]))
    clock = pygame.time.Clock()

    print(players)

    while run :
        clock.tick(60)
        for i in range(3) :
            players[i+1] = n.send(players[0])

        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False
                pygame.quit()

        players[0].move()
        redrawWindow(win, players)
main()