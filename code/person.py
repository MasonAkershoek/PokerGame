import pygame
from rankofhands import check_hand, check_best_hand

class Person:
    def __init__(self):
        self.player_cards = pygame.sprite.Group()
        self.player_cash = 100
        self.player_hand = []
        self.discards = []
        self.dis_num = 0

    def clear_player_cards(self):
        self.player_cards.empty()

    def discard_count(self):
        if len(self.player_cards.sprites()) == 5:
            discard = []
            num = 0
            for card in self.player_cards:
                discard.append(card.hold)
                if card.hold == False:
                    num += 1
            self.discards = discard
            self.dis_num = num
    
    def update(self):
        self.discard_count()
        self.player_hand = check_hand(self.player_cards)
        



class Player(Person):
    def __init__(self):
        super().__init__()
        self.card_pos = 700

class Opponent(Person):
    def __init__(self):
        super().__init__()
        self.card_pos = 200
        self.best_hand = 0

    def think(self):
        #self.best_hand = check_best_hand(self.player_cards, self.player_hand)
        if self.player_hand[0] == 0:
            x=0
            for card in self.player_cards:
                if str(card.card_num) == str(self.player_hand[1]):
                    card.hold = True
                else:
                    card.hold = False
            print(x)
    
        