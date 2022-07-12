from lib2to3.refactor import MultiprocessRefactoringTool
import pygame

width = 1500
height = 958

card_speed = 5

show_debug = True

table_default = pygame.image.load("../graphics/table/table1.jpg")

card_spawn_y = -100


#user events
DealButtonActive = pygame.USEREVENT + 1 
BetButtonActive = pygame.USEREVENT + 2
FoldButtonActive = pygame.USEREVENT + 3
MenuButtonActive = pygame.USEREVENT + 4
FiveCardButtonActive = pygame.USEREVENT + 5
EndGame = pygame.USEREVENT + 6
MusicToggle = pygame.USEREVENT + 7
ROH = pygame.USEREVENT + 8