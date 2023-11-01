# deck
suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []

for suit in suits:
    for num in numbers:
        deck.append([num, suit])

# Valuing


import random
random.shuffle(deck)
print(deck)

#pulling index/cards
dealer_card_1 = deck[0][0]
dealer_card_2 = deck[1][0]
dealer_card_3 = deck[2][0]
#deck 1 a,k,q,j
if dealer_card_1 == "K" or dealer_card_1 == "Q" or dealer_card_1 == 'J':
    dealer_card_1 = 10
elif dealer_card_1 == "A":
    dealer_card_1 = 11

#deck 2 a,k,q,j
if dealer_card_2 == "K" or dealer_card_2 == "Q" or dealer_card_2 == 'J':
    dealer_card_2 = 10
elif dealer_card_2 == "A":
    dealer_card_2 = 11

score = dealer_card_1 + dealer_card_2

print(dealer_card_2)

print(dealer_card_1)

print(score)

# hitting aspect of player
while True:
    # DEALER SCORING
    player_score = sum(card_value(card) for card in player_hand)
    dealer_score = sum(card_value(card) for card in dealer_hand)
    if dealer_score == 21:
        print('DEALER WINS, DEALER HAS BLACKJACK')

if score > 17:
    print("staying")
if score <= 16:
    print("hit")
    print(dealer_card_3)
    score = score + dealer_card_3




print(score)
