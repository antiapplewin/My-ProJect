import mapPlayer
import Menu
import fileUpload
import pygame

screen=pygame.display.set_mode((800, 600))

Menu.Menu.ADD("test")
Menu.Menu.ADD("test6")
Menu.Menu.ADD("test2")
Menu.Menu.ADD("rick")
Menu.Menu.ADD("test5")
Menu.Menu.ADD("test4")

a = Menu.Menu.menu()

while a!="Exit-1!" :
    mapPlayer.player.play(screen, a)
    a = Menu.Menu.menu()