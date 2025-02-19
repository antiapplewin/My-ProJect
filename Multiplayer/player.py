import pygame
import time
import random

class PygameSYS :
    def keyPress() :
        keys = pygame.key.get_pressed()
        moves = []

        if keys[pygame.K_LEFT] :
            moves.append("KL")

        return moves

'''

<chat system>

self.message = [messagePrompt, time, who]
return self.message

'''