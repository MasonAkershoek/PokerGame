from re import T
from numpy import imag
import pygame
from settings import *
import random
import os

class Deck:
    def __init__(self):
        self.cards = self.get_cards()
        self.used_cards = []
    
    def get_cards(self):
        cards = []
        suits = ['Clubs','Diamonds','Hearts','Spades']

        #iterate through all card images
        for x in os.scandir('../graphics/cards'):
            card = []
            path = x.path

            #get suit
            for s in suits:
                if s in x.path:
                    suit = s
            
            card_num = path[-5]
            #get card number
            try:
                if isinstance(int(path[-6]), int):
                    card_num = path[-6] + path[-5]
            except:
                pass

            #append card info to list
            card.append(path)
            card.append(suit)
            card.append(card_num)

            #apend card info list to main list
            cards.append(card)
        return cards
        
    def deal_card(self):
        card = random.randint(0,51)
        while card in self.used_cards:
            card = random.randint(0,51)
        self.used_cards.append(card)
        return self.cards[card]

    def get_card(self, card_num, suit):
        for x in self.cards:
            if x[1] == suit:
                if int(x[2]) == int(card_num):
                    return x

            

class Card(pygame.sprite.Sprite):
    def __init__(self, card_num, suit, path, pos, destination, dely):
        super().__init__()
        self.card_num = card_num
        self.suit = suit
        self.deal_sound = pygame.mixer.Sound('../music/deal.mp3')
        self.deal_sound.set_volume(.2)
        self.icons = self.get_image(path)
        self.image = self.icons[1]
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2((0,0))
        self.click_cooldown = 0
        self.hold = True
        self.destination = destination
        self.deal_delay = dely

    def get_image(self, path):
        icons = []
        icons.append(pygame.image.load(path).convert_alpha())
        icons.append(pygame.image.load('../graphics/back/cardBack_blue3.png').convert_alpha())
        return icons

    def move(self):
        if self.deal_delay == 0:
            if self.rect.centery != self.destination:
                if self.rect.centery < self.destination:
                    self.rect.centery += 20
        else:
            self.deal_delay -= 1
        
    def move_up(self):
        if self.hold == False:
            self.rect.centery -= 20

    def move_hold(self):
        if self.hold == True:
            self.rect.y -= 50
            self.hold = False
        else:
            self.rect.y += 50
            self.hold = True

    def discard(self):
        if self.rect.y < -200:
            self.kill()

    def change_image(self):
        if self.destination > 500:
            if self.rect.centery == self.destination:
                self.image = self.icons[0]
            else:
                self.image = self.icons[1]

    def opponent_display(self):
        self.image = self.icons[0]
        
    def play_sound(self):
        if self.rect.centery == 0:
            self.deal_sound.play()

    def input(self):
        if self.click_cooldown == 0:
            pressed = pygame.mouse.get_pressed()
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                if pressed[0] == True:
                    self.move_hold()
                    self.click_cooldown += 1
        elif self.click_cooldown == 20:
            self.click_cooldown = 0
        else:
            self.click_cooldown += 1 

    def update(self):
        self.change_image()
        self.discard()
        self.play_sound()