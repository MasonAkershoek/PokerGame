import pygame
from mainmenu import MainMenu
from settings import *
from table import Table
from debug import debug
from game import *
import game_data

pygame.init()

#display
pygame.display.set_caption("Mason's Poker")
pygame.display.set_icon(pygame.image.load('../graphics/cards/cardClubs1.png'))
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
phase = 1

running = True

main_menu = MainMenu()
main_menu_active = True
menu_active = False

while running:
    
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
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
    else:
        table.update()
    
    debug('phase: ' + str(game_data.phase))
    
    
    pygame.display.update()
    clock.tick(60)