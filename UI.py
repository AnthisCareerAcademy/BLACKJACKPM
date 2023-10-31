print("Welcome to BlackJack")

name = input('Would you state your name:')
print('Hello, ' + name)
age = input('Would you state your age:')
print(age)

print("The rule for this game is to get close to 21 or get to 21. ")

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []

for suit in suits:
    for num in numbers:
        deck.append([num, suit])


import random
random.shuffle(deck)
print(deck)
#visual
print(f"""          
          ________           ________
         |        |         |{deck[0][1]}       |
         |        |         |        |
         |   ?    |         |   {deck[0][0]}    |
         |        |         |        |
         |________|         |_______{deck[0][1]}|
          ________           ________
         |{deck[1][1]}       |         | {deck[2][0]}      |
         |        |         |        |
         |   {deck[1][0]}    |         |   {deck[2][1]}    |
         |        |         |        | 
         |_______{deck[1][1]}|         |_______{deck[2][0]}|
              """)

player_hand = []
dealer_hand = []

player_hand.append(deck.pop())
dealer_hand.append(deck.pop())
player_hand.append(deck.pop())
dealer_hand.append(deck.pop())

print(f'player hand: {player_hand}')
print(f'dealer hand: {dealer_hand}')

while True:
    hit = input('would you like to hit?(Y/N):')
    if hit == 'Y':
        player_hand.append(deck.pop())
        print(f'players hand: {player_hand}')
    if hit == 'N':
        print('moving on to dealer')








