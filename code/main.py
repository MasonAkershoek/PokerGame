import pygame
from mainmenu import MainMenu
import settings
from table import Table
from debug import debug
from game import *

pygame.init()

#display
pygame.display.set_caption("Mason's Poker")
pygame.display.set_icon(pygame.image.load('../graphics/cards/cardClubs1.png'))
screen = pygame.display.set_mode((settings.width,settings.height))
clock = pygame.time.Clock()
phase = 1

running = True

main_menu = MainMenu()
main_menu_active = True
menu_active = False

font = pygame.font.Font(None, 25)

# Copyright
cw = font.render('©Mason Akershoek', True, 'black')
cw_rect = cw.get_rect(topleft = (10,10))

# Version Number
version = font.render(' Version: Alpha 1.0', True, 'black')
version_rect = version.get_rect(topleft = (10,30))

while running:
    
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Toggle degug screen
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                if settings.show_debug == True:
                    settings.show_debug = False
                else:
                    settings.show_debug = True

        # Toggle Main menu
        if main_menu_active == False:
            table.game.input(event, table)
            if event.type == EndGame:
                table.music.stop()
                del table
                main_menu_active = True
                main_menu.music.play()

        
        if main_menu_active:
            if event.type == FiveCardButtonActive:
                table = Table(screen, FiveCardDraw)
                main_menu.music.stop()
                main_menu_active = False

        
        
                    
    if main_menu_active:
        main_menu.update()
        screen.blit(cw, cw_rect)
        screen.blit(version, version_rect)
    else:
        table.update()
    

    
    pygame.display.update()
    clock.tick(60)