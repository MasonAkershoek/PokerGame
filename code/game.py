from re import T
import game_data
from settings import *

class FiveCardDraw:
    def __init__(self):
        self.cards_in_hand = 5
        self.player_hand_y_pos = 700
        self.opponent_hand_y_pos = self.player_hand_y_pos - 500
        self.card_positions = [(370, self.player_hand_y_pos), (560, self.player_hand_y_pos), (750, self.player_hand_y_pos), (940, self.player_hand_y_pos), (1130, self.player_hand_y_pos)]
        self.game_type = 'five_card'
        self.menu_active = False
    
    def check_card_pos(self, table, person):
        flag = True
        for card in person.player_cards:
            if card.rect.centery == person.card_pos:
                flag = True
            else:
                flag = False
        return flag
            
    def input(self, event, table):
        if self.menu_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_active = False
            
            if event.type == MusicToggle:
                table.music_control()
        else:
            if event.type == DealButtonActive:
                    if game_data.phase == 1:
                        table.player.clear_player_cards()
                        table.deal(table.player)
                        table.deal(table.opponent, False)
                        table.annie()
                        game_data.phase += 1

                    if game_data.phase == 3:
                        game_data.phase += 1

                    if game_data.phase == 6:
                        game_data.phase += 1

            if event.type == BetButtonActive:
                if game_data.phase == 3 or game_data.phase == 6:
                    if table.player.player_cash != 0:
                        table.bet(table.player)

            if event.type == FoldButtonActive:
                if game_data.phase == 3 or game_data.phase == 6:
                    table.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_active = True

    def check_winner(self, player, opponent):
        win = True
        if player.player_hand[0] < opponent.player_hand[0]:
            win = False
        elif player.player_hand[0] == opponent.player_hand[0]:
            if player.player_hand[1] < opponent.player_hand[1]:
                win = False
        return win

    def update(self, table):
        if game_data.phase == 1:
            if table.player.player_cash == 0 or table.opponent.player_cash == 0:
                pygame.event.post(pygame.event.Event(EndGame))

        if game_data.phase == 2:
            if self.check_card_pos(table, table.player):
                game_data.phase += 1
            else:
                for card in table.player.player_cards:
                    card.move()
                for card in table.opponent.player_cards:
                    card.move()
            

        if game_data.phase == 3:
            for card in table.player.player_cards:
                card.input()
            table.opponent.think()
            
        if game_data.phase == 4:
            if table.opponent.dis_num == 0:
                if len(table.player.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1
            elif table.player.dis_num == 0:
                if len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1
            else:
                if len(table.player.player_cards.sprites()) < self.cards_in_hand and len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1

            if table.player.dis_num == 0 and table.opponent.dis_num == 0:
                game_data.phase += 1
            else:
                for card in table.player.player_cards:
                    card.move_up()
                for card in table.opponent.player_cards:
                    card.move_up()

        if game_data.phase == 5:
            if len(table.player.player_cards.sprites()) < self.cards_in_hand:
                table.deal(table.player)

            if len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                table.deal(table.opponent)

            if self.check_card_pos(table, table.player) and self.check_card_pos(table, table.opponent):
                game_data.phase += 1
    
            else:
                for card in table.player.player_cards:
                    card.move()
                for card in table.opponent.player_cards:
                    card.move()

        if game_data.phase == 6:
            if len(table.opponent.player_hand) == 0:
                table.opponent.get_hand()
                table.bet(table.opponent)
            for card in table.opponent.player_cards:
                card.opponent_display()

        if game_data.phase == 7:
            if self.check_winner(table.player, table.opponent):
                table.player.player_cash += game_data.pot
            else:
                table.opponent.player_cash += game_data.pot
            table.reset()


            
            
