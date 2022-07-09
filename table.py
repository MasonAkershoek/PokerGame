import pygame
from mainmenu import ESCMenu
from debug import debug
from card import *
from buttons import *
from ui import PlayerUI, PotUI
from settings import *
from person import *
import game_data

class Table():
    def __init__(self, screen, game):
        self.table_bg = table_default
        self.table_bg_rect = self.table_bg.get_rect(topleft = (0,0))
        self.display_surface = screen
        self.music = pygame.mixer.Sound('../music/music2.mp3')
        self.music.set_volume(.5)
        self.music.play(-1)
        self.playing = True
        self.game = game()
        self.forced_deal = forced_deal = [[5, "Hearts"], [10, "Hearts"], [6, "Hearts"], [2, "Diamonds"], [1, "Diamonds"]]

        #deck
        self.deck = Deck()

        #player cards info
        self.player = Player()

        #opponent
        self.opponent = Opponent()
        
        #buttons
        self.deal_button = DealButton((100,50), ((750 + 200),885), 'black', 'black', 'Deal', 40)
        self.bet_button = BetButton((100,50), ((750 - 200), 885), 'black', 'black', 'Bet', 40)
        self.fold_button = FoldButton((100,50), (750,885), "black", "black", "Fold", 40)

        #UI
        self.player_ui = PlayerUI((0,958), 40 , '../graphics/UI.png', self.game.game_type)
        self.pot_ui = PotUI((((self.display_surface.get_width() / 2) - 600), ((self.display_surface.get_height() / 2) - 40)), 40, '../graphics/UI2.png')

        #menu
        self.menu = ESCMenu('../graphics/menu.png', ((self.display_surface.get_width() / 2), (self.display_surface.get_height() / 2)) )

    def music_control(self):
        if self.playing == True:
            self.music.stop()
            self.playing = False
        else:
            self.music.play(-1)
            self.playing = True

    def change_bg(self):
        pass

    def reset(self):
        game_data.phase = 1
        self.player.clear_player_cards()
        self.opponent.clear_player_cards()
        self.deck.used_cards.clear()
        self.opponent.player_hand.clear()
        game_data.pot = 0

    def endgame(self):
        self.kill()

    def annie(self):
        self.player.player_cash -= 10
        self.opponent.player_cash -= 10
        game_data.pot += 20

    def bet(self, person):
        person.player_cash -= 10
        game_data.pot += 10
    
    def deal(self, person, level=True):
        y = person.card_pos
            
        if len(self.forced_deal) == 0:
            if self.game.game_type == 'five_card':
                if len(person.player_cards.sprites()) != 0:
                    for x in (range(5)):
                        if person.discards[x] == False:
                            card = self.deck.deal_card()
                            person.player_cards.add(Card(card[2],card[1], card[0], (self.game.card_positions[x][0], card_spawn_y), y, (x * 10)))
                else:
                    index = 0
                    for x in (range(self.game.cards_in_hand)):
                        card = self.deck.deal_card()
                        person.player_cards.add(Card(card[2],card[1], card[0], (self.game.card_positions[index][0], card_spawn_y), y, (x * 10)))
                        index += 1
        else:
            index = 0
            for x in self.forced_deal:
                card = self.deck.get_card(x[0], x[1])
                person.player_cards.add(Card(card[2],card[1], card[0], (self.game.card_positions[index][0], card_spawn_y), y, (index * 10)))
                index += 1
            self.forced_deal.clear()

    def update(self):
        if self.game.menu_active:
            self.menu.update()
        else:
            self.game.update(self)

            #draw background
            self.display_surface.blit(self.table_bg, self.table_bg_rect)

            #ui
            self.player_ui.update(str(self.player.player_cash), self.player.player_hand)
            self.pot_ui.update(game_data.pot)

            #draw cards
            self.player.player_cards.update()
            self.player.player_cards.draw(self.display_surface)

            self.opponent.player_cards.update()
            self.opponent.player_cards.draw(self.display_surface)

            self.opponent.update()
            self.player.update()

            
            #self.pot_ui.update(game_data.pot)

            #buttons
            self.deal_button.update()
            self.bet_button.update()
            self.fold_button.update()

            debug('opponet: ' + str(self.opponent.player_hand), 30)
            debug('player: ' + str(self.player.player_hand), 50)
            debug("opponent cash: " + str(self.opponent.player_cash), 70)
