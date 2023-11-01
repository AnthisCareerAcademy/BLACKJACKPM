import random

# deck
suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
dealer_hand = []

for suit in suits:
    for num in numbers:
        deck.append([num, suit])

# suffle
random.shuffle(deck)
print(deck)

# populating the hands with cards
# player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
# player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

def hit(hand):
    hand.append(deck.pop(0))

# Valuing
def card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[0])


# deck 1 a,k,q,j


while True:
    # hitting aspect of player
    dealer_score = sum(card_value(card) for card in dealer_hand)
    if dealer_score == 21:
        print('DEALER WINS, DEALER HAS BLACKJACK')
        break
    if dealer_score <= 16:
        hit(dealer_hand)
        continue
    if dealer_score >= 17:
        print(dealer_hand)
        print("staying")
        break
print(dealer_score)
