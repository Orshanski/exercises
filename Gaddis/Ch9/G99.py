import random as rd


def create_deck():
    names = ['Туз', 'Король', 'Дама', 'Валет', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    suits = ['пик', 'червей', 'треф', 'бубей']

    deck = []
    for suit in suits:
        for card_name in names:
            if card_name in ['Король', 'Дама', 'Валет', '10']:
                card_cost = 10
            elif card_name in ['9', '8', '7', '6', '5', '4', '3', '2']:
                card_cost = int(card_name)
            else:
                card_cost = 11
            deck.append([card_name + ' ' + suit, card_cost])

    rd.shuffle(deck)
    rd.shuffle(deck)

    return deck


def sum_of_the_hand(hand):
    try:
        return sum(list(zip(*hand))[1])
    except IndexError:
        return 0


my_deck = create_deck()
losers = []
players = ['Dealer', 'Alexey']
players_hand = {}

while len(my_deck) > 0:
    players_hand.clear()
    for player in players:
        players_hand[player] = []
    overload = False
    while not overload:
        for player in players:
            try:
                new_card = my_deck.pop(0)
            except IndexError:
                overload = True
                print('Кончилась колода')
                break
            name = new_card[0]
            cost = new_card[1]
            print(f'{player} берет {name}')
            if name in ['Туз пик', 'Туз треф', 'Туз бубей', 'Туз червей'] and (sum_of_the_hand(players_hand[player]) + cost) >= 21:
                cost = 1
            players_hand[player].append([name, cost])
            if sum_of_the_hand(players_hand[player]) > 21:
                overload = True
                losers.append(player)
                print(f'{player} проиграл')
                print("--------------------------")
                break

print(losers)
