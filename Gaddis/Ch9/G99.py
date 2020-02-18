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


my_deck = create_deck()
# my_deck =[['Туз пик', 11], ['Туз бубей', 11], ['10 треф', 10]]
wins = []

while len(my_deck) > 0:
    dealer_hand = []
    player_hand = []
    while True:
        try:
            new_card = my_deck.pop(0)
        except IndexError:
            break
        name = new_card[0]
        cost = new_card[1]
        print(f'Дилер берет {name}')
        try:
            sum_of_the_hand = sum(list(zip(*dealer_hand))[1])
        except IndexError:
            sum_of_the_hand = 0
        if name in ['Туз пик', 'Туз треф', 'Туз бубей', 'Туз червей'] and (sum_of_the_hand + cost) >= 21:
            cost = 1
        dealer_hand.append([name, cost])
        sum_of_the_hand = sum(list(zip(*dealer_hand))[1])
        if sum_of_the_hand > 21:
            wins.append('player')
            print('Игрок выиграл')
            print('---------------------------------------------------------------------------------------------------')
            break

        try:
            new_card = my_deck.pop(0)
        except IndexError:
            break
        name = new_card[0]
        cost = new_card[1]
        print(f'Игрок берет {name}')
        try:
            sum_of_the_hand = sum(list(zip(*player_hand))[1])
        except IndexError:
            sum_of_the_hand = 0
        if name in ['Туз пик', 'Туз треф', 'Туз бубей', 'Туз червей'] and (sum_of_the_hand + cost) >= 21:
            cost = 1
        player_hand.append([name, cost])
        sum_of_the_hand = sum(list(zip(*player_hand))[1])
        if sum_of_the_hand > 21:
            wins.append('dealer')
            print('Дилер выиграл')
            print('---------------------------------------------------------------------------------------------------')
            break

print(wins)
