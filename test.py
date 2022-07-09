sorted_cards = [[4, 'Clubs'], [4, 'Spades'], [6, 'Hearts'], [6, 'Spades'], [6, 'Diamonds']]

def test1(sorted_cards):
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

    print(hand)
    print(card_info)
    print(cards_to_skip)

def test2():
    for x, card in enumerate(sorted_cards):
        print(x)

test2()

