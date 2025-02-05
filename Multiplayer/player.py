import pygame
import time
import random

class Player() :
    def __init__(self, playerInfo) :
        self.playerInfo = playerInfo
    
    def GetGameAddress(self) :
        if (self.playerInfo['GameIP'] == "0:test") :
            return TestPlayer(self.playerInfo['playerSetting'])
        if (self.playerInfo['GameIP'] == "1:test") :
            return TestPlayer(self.playerInfo['playerSetting'])
        if (self.playerInfo['GameIP'] == "2:Number") :
            return TheNumberGame(self.playerInfo['playerSetting'])
        
    def GetGameIP(self) :
        return self.playerInfo['GameIP']

class TestPlayer :
    def __init__(self, playerInfo) :
        self.x = playerInfo['rect'][0]
        self.y = playerInfo['rect'][1]
        self.width = playerInfo['rect'][2]
        self.height = playerInfo['rect'][3]
        self.color = playerInfo['extra'][0]
        self.rect = playerInfo['rect']
        self.vel = playerInfo['extra'][1]
        self.text = playerInfo['extra'][2]
        self.message = ["", 0, self.text]

    def draw(self, win) :
        pygame.draw.rect(win, self.color, self.rect)

    def move(self) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] :
            self.x -= self.vel
        if keys[pygame.K_RIGHT] :
            self.x += self.vel
        if keys[pygame.K_UP] :
            self.y -= self.vel
        if keys[pygame.K_DOWN] :
            self.y += self.vel
        if keys[pygame.K_t] :
            self.message[0] = input("type : ")
            self.message[1] = time.time()

        self.update()

    def update(self) :
        self.rect = (self.x, self.y, self.width, self.height)
    
    def write(self, win, font) :
        text = font.render(self.text, False, (0, 0, 0))
        win.blit(text, (self.rect[0]+10, self.rect[1]-25))

    def chat(self) :
        return self.message
    
    def GetPlayerInfo(self) :
        return {"P_number" : self.text}
    
class TheNumberGame :
    playing = False
    GameInfo = {}

    def __init__(self, playerInfo) :
        self.IsOwner = playerInfo['IsOwner']
        self.message = ["", 0, playerInfo['PNumber']]
        self.PlayerGame = {}

    def KeyPress(self) :
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q] :
            self.DisplayGame()

    def IsGameStarting(self, turn) :
        if (self.IsOwner) :
            TheNumberGame.GameInfo['turn'] = (0, turn)
            TheNumberGame.GameInfo['VictoryCard'] = random.randint(1, 7)
            TheNumberGame.playing = True
            return True

    def PreparingGame(self) :
        self.PlayerGame['NumberCard'] = []
        self.PlayerGame['ActingCard'] = []

        for i in range(3) :
            self.PlayerGame["NumberCard"].append(random.randint(-25, 50))
        for i in range(5) :
            self.PlayerGame["NumberCard"].append(random.randint(1, 3))

    def Game(self) :
        self.DisplayGame()

    def DisplayGame(self) :
        for card in self.PlayerGame['NumberCard'] :
            print(card, end=" ")
        
        print("")
        for card in self.PlayerGame['ActingCard'] :
            print(card, end=" ")

    def GetData(self) :
        return self.IsOwner
    
    def chat(self) :
        return self.message