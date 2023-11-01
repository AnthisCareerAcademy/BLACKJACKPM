import random
import string

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
player_hand = []
dealer_hand = []

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
def hit(hand):
    hand.append(deck.pop(0))

def create_deck():
    for suit in suits:
        for num in numbers:
            deck.append([num, suit])
    # shuffling the deck
    random.shuffle(deck)
def can_split(hand) -> bool:
    return hand[0][0] == hand[1][0]

create_deck()
# checking out the deck
print(deck)

# Intro for the games stating your name and age, then rules
print("Welcome to BlackJack\n")

name = input('Would you state your name: ')
print('Hello, ' + name)
age = input('Would you state your age: ')
print(age)

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
hit(player_hand)
hit(dealer_hand)
hit(player_hand)
hit(dealer_hand)

# test
draw_cards(player_hand)

# showing the hands (example)
print(f'player hand: {player_hand}')
print(f'dealer hand: {dealer_hand}')

# hitting aspect of player
while True:
    do_i_hit = input('would you like to hit or stand?(H/S): ')
    if do_i_hit == 'H':
        hit(player_hand)
        print(f'players hand: {player_hand}')
    elif do_i_hit == 'S':
        print('moving on to dealer')
        break

# Total value of cards

#Yes and No to play again
play_again = input("do you want to play again? Yes or NO?\n")
if play_again == "Yes":
    print("Starting a new game!")
elif play_again == "No":
    print("Game End!\n")
    # break out of game loop


#credit
print(f"UI created by: Martin, Okkar, Brodie, and Pika.")
print(f"Dealer Tasks created by: Indy, Obeth, and Mason.")
print(f"Player Rules created by: Dazion, Logan, Damian, Zane and Avonta.")




