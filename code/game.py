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
                    table.show_roh()
            
            if event.type == MusicToggle:
                table.music_control()

            if event.type == ROH:
                table.show_roh()
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
                    table.opponent.player_cash += game_data.pot
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

        # Phase 1 - Check win condition / start new round
        if game_data.phase == 1:

            # Set opponent ui face
            table.opponent_ui.change_face('idle')

            if table.player.player_cash == 0 or table.opponent.player_cash == 0:
                pygame.event.post(pygame.event.Event(EndGame))
                
        # Phase 2 - Deal in new set of cards
        if game_data.phase == 2:

            # When the players cards reach there destination the next phase starts
            if self.check_card_pos(table, table.player):
                game_data.phase += 1

            # If the cards arent in there places there move functions are called
            else:
                for card in table.player.player_cards:
                    card.move()
                for card in table.opponent.player_cards:
                    card.move()
            
        # Phase 3 - Action phase for the player and computer.
        if game_data.phase == 3:

            # Set opponent thinking face
            table.opponent_ui.change_face('think')

            for card in table.player.player_cards:
                card.input()

            table.opponent.think()
        
        # Phase 4 - Discard Phase
        if game_data.phase == 4:
            table.opponent_ui.change_face('idle')

            # If the opponent isnt getting rid of cards and the amount of cards 
            # in the players hand is smaller than it should be go to the next turn.
            if table.opponent.dis_num == 0:
                if len(table.player.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1
            
            # If the player isnt getting rid of cards and the amount of cards 
            # in the opponents hand is smaller than it should be go to the next turn.
            elif table.player.dis_num == 0:
                if len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1

            # If both partys are discarding and both of there 
            # hands have less cards than they should, next turn.
            else:
                if len(table.player.player_cards.sprites()) < self.cards_in_hand and len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                    game_data.phase += 1

            # If neither party is discarding next turn.
            if table.player.dis_num == 0 and table.opponent.dis_num == 0:
                game_data.phase += 1
            
            # If none of the previouse conditions are met move the cards up.
            else:
                for card in table.player.player_cards:
                    card.move_up()
                for card in table.opponent.player_cards:
                    card.move_up()

        # Phase 5 - Second Deal
        if game_data.phase == 5:

            # If the player has less cards in his hand than he should deal him cards
            if len(table.player.player_cards.sprites()) < self.cards_in_hand:
                table.deal(table.player)

            # If the opponent has less cards in hand than they should deal them cards
            if len(table.opponent.player_cards.sprites()) < self.cards_in_hand:
                table.deal(table.opponent)

            # If all cards are in there correct possitions go to next phase
            if self.check_card_pos(table, table.player) and self.check_card_pos(table, table.opponent):
                game_data.phase += 1
            
            # If no previouse conditions are meet then move cards down
            else:
                for card in table.player.player_cards:
                    card.move()
                for card in table.opponent.player_cards:
                    card.move()

        # Phase 6 - Display 
        if game_data.phase == 6:
            if len(table.opponent.player_hand) == 0:
                table.opponent.get_hand()
            for card in table.opponent.player_cards:
                card.opponent_display()
            
            if self.check_winner(table.player, table.opponent):
                table.opponent_ui.change_face('lose')
                #display ui showing winner is player
            else:
                table.opponent_ui.change_face('win')
                # display ui showing opponent won

        # Phase 7 - Money changing phase and reset
        if game_data.phase == 7:
            if self.check_winner(table.player, table.opponent):
                table.player.player_cash += game_data.pot
            else:
                table.opponent.player_cash += game_data.pot
            table.reset()


            
            
