import pygame
import time

class Player() :
    def __init__(self, x, y, width, height, color, speed, number) :
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = speed
        self.text = number
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
        win.blit(text, (100, 100))

    def chat(self) :
        return self.message