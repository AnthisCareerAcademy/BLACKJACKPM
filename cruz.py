import random
import string

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
player_hand = []
dealer_hand = []

# Valuing


def hit(hand):
    hand.append(deck.pop(0))



# NOT WORKING
def draw_cards(hand) -> string:
    drawn_hand = []
    template = f"""          
 ________ 
|        | 
|        |
|        |
|        |
|________|"""
    templatearray = [" ________ ", "|        |", "|        |", "|        |", "|        |", "|________|"]

    # building algorithm for drawing the hand
    for index in range(len(hand)):
        # so long as the index in not equal to any of those
        if index == 0:
            drawn_hand.append(" ________ ")
        elif index == 1:
            drawn_hand.append(f"|        |")
        elif index != 1 and index != 5 and index != 3:
            print("working")
    #     for card in hand:
    #


for suit in suits:
    for num in numbers:
        deck.append([num, suit])
# shuffling the deck
random.shuffle(deck)

# checking out the deck
print(deck)

# Intro for the games stating your name and age, then rules
print("Welcome to BlackJack\n")

# name = input('Would you state your name:')
# print('Hello, ' + name)
# age = input('Would you state your age:')
# print(age)




# populating the hands with cards
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

# test
draw_cards(player_hand)

# showing the hands (example)
print(f'player hand: {player_hand}')
print(f'dealer hand: {dealer_hand}')

dealer_score = 0

# Testing
def card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    if card[0] == 'A':
        if dealer_score >= 11:
            return 1
        if dealer_score < 11:
            return 11
    else:
        return int(card[0])


# hitting aspect of player
while True:
    # hitting aspect of player
    dealer_score = sum(card_value(card) for card in dealer_hand)
    if dealer_score == 21:
        print(dealer_hand)
        print('DEALER WINS, DEALER HAS BLACKJACK')
        break
    if dealer_score > 21:
        print(dealer_hand)
        print("DEALER BUST")
        break
    if dealer_score <= 16:
        hit(dealer_hand)
        continue
    if dealer_score >= 17:
        print(dealer_hand)
        print("STAYING")
        break

print(dealer_score)
# Total value of cards


