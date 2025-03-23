import pygame
import os
import fileUpload
import sys

avamap1 = []
scroll = 0

class Menu :
    def menu() :
        global scroll, avamap1
        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        clock = pygame.time.Clock()
        easy, normal, hard, insane = pygame.image.load("easy.png"), pygame.image.load("normal.png"), pygame.image.load("hard.png"), pygame.image.load("insane.png")
        easy = pygame.transform.scale(easy, (400, 256))
        normal = pygame.transform.scale(normal, (400, 256))
        hard = pygame.transform.scale(hard, (400, 256))
        insane = pygame.transform.scale(insane, (400, 256))

        def imgPicker(diff) :
            if diff>=20 :
                return insane
            elif diff >= 15 :
                return hard
            elif diff >= 5 :
                return normal
            else :
                return easy


        pygame.init()
        pygame.display.set_caption("Menu")

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        done = False

        fonts = []

        avamap = []
        for item in avamap1 :
            avamap.append(item)
        avamap.append(avamap1[0])
        avamap.append(avamap1[1])
        avamap.append(avamap1[2])
        avamap.append(avamap1[3])

        for item in avamap :
            fonts.append(item['name'])
        for i in range(4) :
            fonts.append(avamap[i]['name'])

        dscroll = 0
        speed = 0

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                    return "Exit-1!"
                if event.type == pygame.KEYDOWN: #game의 event type이 키보드를 누른 상태일 때
                    if event.key == pygame.K_UP:
                        dscroll = -1
                    elif event.key == pygame.K_DOWN:
                        dscroll = 1
                    elif event.key == pygame.K_SPACE:
                        return avamap1[scroll]['fileName']
                elif event.type == pygame.KEYUP :
                    dscroll = 0
                    speed = 0
                
            
            if speed %10 ==0:
                scroll += dscroll
                if scroll+4 >= len(avamap) :
                    scroll = 0
                elif scroll < 0 :
                    scroll = len(avamap)-5
            speed += 1
            font = pygame.font.Font(None, 40)

            screen.fill("WHITE")
            screen.blit(font.render(avamap[scroll]['name'], True, "black"), [100, 100])
            screen.blit(font.render(f"Difficulty:{str(avamap1[scroll]['difficulty'])}", True, "BLACK"), [100, 500])
            screen.blit(imgPicker(int(avamap[scroll]['difficulty'])), [320, 10])
            screen.blit(font.render(fonts[scroll], True, "black"), [370, 112])
            screen.blit(imgPicker(int(avamap[scroll+1]['difficulty'])), [320, 90])
            screen.blit(font.render(fonts[scroll+1], True, "black"), [370, 192])
            screen.blit(imgPicker(int(avamap[scroll+2]['difficulty'])), [320, 170])
            screen.blit(font.render(fonts[scroll+2], True, "black"), [370, 272])
            screen.blit(imgPicker(int(avamap[scroll+3]['difficulty'])), [320, 250])
            screen.blit(font.render(fonts[scroll+3], True, "black"), [370, 352])
            screen.blit(imgPicker(int(avamap[scroll+4]['difficulty'])), [320, 330])
            screen.blit(font.render(fonts[scroll+4], True, "black"), [370, 432])

            pygame.display.flip()



        pygame.quit()
    
    def ADD(name) :
        global avamap1
        F = fileUpload.File.Load(name)
        avamap1.append({"name":F["setting"]["name"], "difficulty":F["setting"]["difficulty"], "fileName":name})