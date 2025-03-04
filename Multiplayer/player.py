import pygame
import time
import random

class PygameSYS :
    def keyPress() :
        keys = pygame.key.get_pressed()
        moves = []

        if keys[pygame.K_LEFT] :
            moves.append("AL")
        if keys[pygame.K_UP] :
            moves.append("AU")
        if keys[pygame.K_DOWN] :
            moves.append("AD")
        if keys[pygame.K_RIGHT] :
            moves.append("AR")
        if keys[pygame.K_t] :
            moves.append("Kt")
        if keys[pygame.K_r] :
            moves.append("Kr")
        if keys[pygame.K_q] :
            moves.append("Kq")

        return moves

class GameSYS :
    def __init__(self) :
        self.message = ""
        self.time = 0
        self.typing = False

    def ChatInput(self) :
        if not(self.typing) :
            self.typing = True
            self.message = input("type : ")
            if (self.message!="") :
                print(f"You : {self.message}")
            self.typing = False
            self.time = time.time()

    def GetMess(self) :
        tempTup = (self.message, self.time)
        return tempTup

'''

<chat system>

self.message = [messagePrompt, time, who]
return self.message

'''