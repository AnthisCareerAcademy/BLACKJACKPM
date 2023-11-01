import random
import string

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
player_hand = []
dealer_hand = []

# Valuing
def card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[0])







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
    print("\n".join(templatearray))

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

print("\nThe rule for this game is to get close to 21 without going over. ")
print("The Ace rules is 11 or 1 - it will auto pick based on if over 21 (built)")
print("The split is to compare both player hands to dealer. Each hand scored individually.")
print("The double down would be the player wins 2 pts awarded, if they lose then 2 pts goes to the dealer")
print("The scores hand would be the total amount for player and dealer.")

# visual test
# print(f"""
#           ________           ________
#          |        |         |{deck[0][1]}       |
#          |        |         |        |
#          |   ?    |         |   {deck[0][0]}    |
#          |        |         |        |
#          |________|         |_______{deck[0][1]}|
#           ________           ________
#          |{deck[1][1]}       |         | {deck[2][0]}      |
#          |        |         |        |
#          |   {deck[1][0]}    |         |   {deck[2][1]}    |
#          |        |         |        |
#          |_______{deck[1][1]}|         |_______{deck[2][0]}|
#               """)

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

# hitting aspect of player
while True:
    # DEALER SCORING
    player_score = sum(card_value(card) for card in player_hand)
    dealer_score = sum(card_value(card) for card in dealer_hand)
    for value in dealer_hand:
        dealer_score += value[0]
    if dealer_score == 21:
        print('DEALER WINS, DEALER HAS BLACKJACK')





    hit = input('would you like to hit or stand?(H/S):')
    if hit == 'H':
        player_hand.append(deck.pop())
        print(f'players hand: {player_hand}')
    if hit == 'S':
        print('moving on to dealer')
    break

# Total value of cards

#credit
print(f"UI created by: Martin, Okkar, Brodie, and Pika.")
print(f"Dealer Tasks created by: Indy, Obeth, and Mason.")
print(f"Player Rules created by: Dazion, Logan, and Avonta.")