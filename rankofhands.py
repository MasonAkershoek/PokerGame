from debug import debug

def check_hand(cards):
    hand = [0,0]
    sorted_cards = sort_hand(cards)
    pairs = get_num_of_cards(sorted_cards)
    pairs.sort()

    #check to make sure the list is full
    if len(sorted_cards) == 5:
        #set high card
        hand[1] = sorted_cards[4][0]
        

        #check for pairs or full house
        if pairs != None:
            if len(pairs) == 1:
                hand[1] = pairs[-1][0]
                if pairs[0][1] == 3:
                    hand[0] = 3
                elif pairs[0][1] == 4:
                    hand[0] = 7
                else:
                    hand[0] = 1
            if len(pairs) == 2:
                if pairs[0][1] == 3 or pairs[1][1] == 3:
                    hand[0] = 6
                else:
                    hand[0] = 2
                hand[1] = pairs[-1][0]

        #check for straight flush
        if check_flush(sorted_cards) and check_straight(sorted_cards):
            hand[0] = 8
        
        elif check_flush(sorted_cards) and check_royal_flush(sorted_cards):
            hand[0]= 9

        else:
            #check for flush
            if check_flush(sorted_cards):
                hand[0] = 5

            if check_straight(sorted_cards):
                hand[0] = 4

    return hand

def sort_hand(cards):
    sorted_cards = []

    for card in sorted_cards:
        if card[0] == 1:
            card[0] = 14
    
    for card in cards:
        a = []
        a.append(int(card.card_num))
        a.append(card.suit)
        sorted_cards.append(a)
    sorted_cards.sort()
    return sorted_cards

def check_flush(cards):
    flush = True
    for card in cards:
        if cards[0][1] != card[1]:
            flush = False
    return flush

def check_straight(cards):
    straight = True
    comp_card = cards[0][0]
    for x, card in enumerate(cards):
        if x != 0:
            if card[0] == (comp_card + x) and card[0] != comp_card:
                straight = True
            else:
                return False
    return straight

def check_royal_flush(cards):
    royal_flush = True
    for card in cards:
        if card[0] != 1:
            if card[0] < 10:
                royal_flush = False
    return royal_flush

def get_num_of_cards(sorted_cards):
    hand = []
    cards_to_skip = []
    comp_card = 0

    for x, card in enumerate(sorted_cards):
        comp_card = x
        num_of_card = 1
        if x not in cards_to_skip:
            for y,c in enumerate(sorted_cards):
                if y != comp_card:
                    if card[0] == c[0]:
                        if y not in cards_to_skip:
                            cards_to_skip.append(y)
                        num_of_card += 1
            if num_of_card > 1:
                card_info = []
                card_info.append(card[0])
                card_info.append(num_of_card)
                hand.append(card_info)

            if y not in cards_to_skip:
                cards_to_skip.append(y)

    return hand
    


def check_best_hand(cards, hand):
    
    


    def flush():
        pass

    def straight():
        pass

    def royal_flush():
        pass