print("Welcome to BlackJack")
input("Would you please state your name: ")
suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []

for suit in suits:
    for num in numbers:
        deck.append([num, suit])

print(deck)


player_hand = []
dealer_hand = []

player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

print(f'player hand: {player_hand}')
print(f'dealer hand: {dealer_hand}')

