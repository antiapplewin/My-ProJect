from tkinter import *
from random import *
import random
from tkinter import messagebox

# forced blocked item : 🚫

# var, list, etc...
game_map_pp, game_map_mp, game_map_pm, game_map_mm = [], [], [], []
colors = ["⬜", "🟥", "🟧","🟨","🟩","🟦","🟫","⬛"] # 🟪
color_dictionary = {"🟥":"#87ff54", "⬜":"#a3ff52", "🟧":"#63ed28", "🟨":"#cef542", "🟩":"#90f542", "🟦":"#83f71e", "🟪":"#c242f5", "🟫":"#c2ff61", "⬛":"#9dff00"}
farm_biome = ["⬜", "🟥", "🟧","🟨","🟩","🟦","🟫","⬛"]
biomes = ["farm"] # GLITCH ISLAND
biome_match = {'⬜':"farm", '⬛':"farm", '🟧':'farm', '🟥':'farm', '🟩':'farm', '🟦':'farm', '🟫':'farm', '🟨':'farm'}
start_map = []
x, y = 0, 0

# IndexError : OutOfBound

# Define

def BringSquare(camX, camY) :
    print(abs(camX), abs(camY))
    if (camX>=0) :
        if (camY>=0) :
            print(len(game_map_pp[camX]))
            return game_map_pp[camX][camY]
        else :
            print(len(game_map_mp[camX]))
            return game_map_mp[camX][-1*camY]
    else :
        if (camY>=0) :
            print(len(game_map_pm[abs(camX)]))
            return game_map_pm[-1*camX][camY]
        else :
            print(len(game_map_mm[abs(camX)]))
            return game_map_mm[-1*camX][-1*camY]

def LoadingWorld(X, Y) :
    for i in range(-2, 3) :
        if (X+i>=0) :
            if Y+2>=0 :
                try :
                    game_map_pp[X+i][Y+3]
                except IndexError :
                    game_map_pp[X+i].append(random.choice(colors))
            if Y-2<=0 :
                try :
                    game_map_mp[X+i][abs(Y-3)]
                except IndexError :
                    game_map_mp[X+i].append(random.choice(colors))
        if (X+i<=0) :
            if Y+2>=0 :
                try :
                    game_map_pm[abs(X+i)][Y+3]
                except IndexError :
                    game_map_pm[abs(X+i)].append(random.choice(colors))

            if Y-2<=0 :
                try :
                    game_map_mm[abs(X+i)][abs(Y-3)]
                except IndexError :
                    game_map_mm[abs(X+i)].append(random.choice(colors))

    if Y+2>=0 :
        if X+2>=0 : 
            if (len(game_map_pp[X+3])<Y+3) :
                for i in range(Y+3-len(game_map_pp[X+3])) :
                    game_map_pp[X+3].append(random.choice(colors))
        if X-2<=0 :
            if (len(game_map_pm[abs(X-3)])<Y+3) :
                for i in range(Y+3-len(game_map_pm[abs(X-3)])) :
                    game_map_pm[abs(X-3)].append(random.choice(colors)) # 

    if Y-2<=0 :
        if X+2>=0 :
            if (len(game_map_mp[X+3])<abs(Y-3)) :
                for i in range(abs(Y-3)-len(game_map_mp[X+3])) :
                    game_map_mp[X+3].append(random.choice(colors)) # 
        if X-2<=0 :
            if (len(game_map_mm[abs(X-3)])<abs(Y-3)) :
                for i in range(abs(Y-3)-len(game_map_mm[abs(X-3)])) :
                    game_map_mm[abs(X-3)].append(random.choice(colors)) # 


def SettingWorld() :
    global x, y
    
    if (x+3>=len(game_map_pp)) :
        game_map_pp.append([])

    if (x+3>=len(game_map_mp)) :
        game_map_mp.append([])

    if (abs(x-3)>=len(game_map_pm)) :
        game_map_pm.append([])

    if (abs(x-3)>=len(game_map_mm)) :
        game_map_mm.append([])
    
    LoadingWorld(x, y)

def SetDisplay(X, Y) :
    for j in range(5) :
        for i in range(5) :
            canvas.create_rectangle(i*100, j*100, i*100+100, j*100+100, fill=color_dictionary[BringSquare(2-i+X, 2-j+Y)], outline=color_dictionary[BringSquare(2-i+X, 2-j+Y)])

def move(event) :
    global x, y

    if (event.keysym=="Up") :
        y+=1
        SetDisplay(x, y)
        SettingWorld()
    
    if (event.keysym=="Down") :
        y-=1
        SetDisplay(x, y)
        SettingWorld()

    if (event.keysym=="Right") :
        x-=1
        SetDisplay(x, y)
        SettingWorld()
    
    if (event.keysym=="Left") :
        x+=1
        SetDisplay(x, y)
        SettingWorld()

# starting settings

start_biome = random.choice(biomes)

for i in range(5) :
    start_map.append([])
    for j in range(5) :
        if start_biome == "farm" :
            start_map[i].append(random.choice(farm_biome))

for i in range(3) :
    game_map_pp.append([])
    for j in range(3) :
        game_map_pp[i].append(start_map[2-i][2-j])

for i in range(3) :
    game_map_pm.append([])
    for j in range(3) :
        game_map_pm[i].append(start_map[2-i][2+j])

for i in range(3) :
    game_map_mp.append([])
    for j in range(3) :
        game_map_mp[i].append(start_map[2+i][2-j])

for i in range(3) :
    game_map_mm.append([])
    for j in range(3) :
        game_map_mm[i].append(start_map[2+i][2+j])

SettingWorld()

# tkinter PART

win = Tk()

win.title("BRUH")

canvas = Canvas(win, bg = "#ffffff", width = 500, height = 500)

SetDisplay(x, y)

canvas.bind_all("<KeyPress-Up>", move)
canvas.bind_all("<KeyPress-Down>", move)
canvas.bind_all("<KeyPress-Right>", move)
canvas.bind_all("<KeyPress-Left>", move)

canvas.grid(row=0, column=1)

win.mainloop()