import random
import string

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
player_hand = []
player_split_hand = []
dealer_hand = []


def card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[0])


# NOT WORKING
def draw_cards(hand):
    complete_drawn_hand = []
    drawn_card = []
    mutable = []
    # 10 chars long
    # template = f"""
    #  _________
    # |         |
    # |         |
    # |         |
    # |         |
    # |_________|"""
    #     templatearray = [" _________ ", "|         |", "|         |", "|         |", "|         |", "|_________|"]
    # building algorithm for drawing the hand
    # however long the hand is that's how many cards we'll generate
    for index in range(len(hand)):
        for beep in range(6):
            # so long as the index in not equal to any of those
            if beep == 0:
                drawn_card.append(" _________ ")
            elif beep == 1:
                drawn_card.append(f"|{hand[index][1]}        |")
            elif beep == 3:
                mutable.append(f"|   {hand[index][0]}")
                if len(str(hand[index][0])) == 2:
                    mutable.append("    |")
                else:
                    mutable.append("     |")
                drawn_card.append("".join(mutable))
                mutable.clear()
            elif beep == 5:
                drawn_card.append(f"|________{hand[index][1]}|")
            else:
                drawn_card.append("|         |")
        complete_drawn_hand.append(drawn_card[:])
        drawn_card.clear()
    #     for card in hand:
    #
    # showing the hands (example)
    # print(draw_cards(player_hand))
    example = []
    for level in range(6):
        for card_index in range(len(complete_drawn_hand)):
            example.append(complete_drawn_hand[card_index][level])
        print("      ".join(example))
        example.clear()


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


def standardize(string_to_standardize) -> string:
    return string_to_standardize.lower().strip()


create_deck()
# checking out the deck
# print(deck)

# Intro for the games stating your name and age, then rules
print("Welcome to BlackJack\n")
"""
name = input('Would you state your name: ')
print('Hello, ' + name)

while True:

    age = input('Would you state your age: ')
    if age.isdecimal():
        break
    else:
        print("Please type an integer")
print(age)
print("\nThe rule for this game is to get close to 21 without going over. ")
print("The Ace rules is 11 or 1 - it will auto pick based on if over 21 (built)")
print("The split is to compare both player hands to dealer. Each hand scored individually.")
print("The double down would be the player wins 2 pts awarded, if they lose then 2 pts goes to the dealer")
print("The scores hand would be the total amount for player and dealer.")

print("\nStarting The Game!")
"""
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
# draw_cards(player_hand)

# # showing the hands (example)
# # print(draw_cards(player_hand))
# example = []
# drawn_player_hand = draw_cards(player_hand)
# for level in range(6):
#     for card_index in range(len(drawn_player_hand)):
#         example.append(drawn_player_hand[card_index][level])
#     print("      ".join(example))
#     example.clear()

# example = []
# for card_index in range(len(draw_cards(player_hand))):
#     for level in range(6):

print(f'player hand: {draw_cards(player_hand)}')
print(f'dealer hand: {draw_cards(dealer_hand)}')

# hitting aspect of player
while True:
    player_score = sum(card_value(card) for card in player_hand)
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
        print("dealer hand:")
        print(dealer_hand)
        print(dealer_score)
        print("staying")
        break
    # Dealer Scoring
    # player_score = sum(card_value(card) for card in player_hand)
    dealer_score = sum(card_value(card) for card in dealer_hand)
    if dealer_score == 21:
        print('Dealer Wins, Dealer has Blackjack')
    # if player_score == 21:
    #    print('YOU GOT BLACKJACK')

    do_i_hit = standardize(input('would you like to hit or stand?(H/S): '))
    if do_i_hit == 'h':

        print('dealing hands..."')
        hit(player_hand)
        print(f'players hand: {draw_cards(player_hand)}')

    elif do_i_hit == 's':
        print('moving on to dealer')
        break

# Yes and No to play again
play_again = standardize(input("do you want to play again? Yes or NO?\n"))
if play_again == "yes":
    print("Starting a new game!")
elif play_again == "no":
    print("Game End!\n")
    # break out of game loop

# credit
print(f"UI created by: Martin, Okkar, Brodie, and Pika.")
print(f"Dealer Tasks created by: Indy, Obeth, and Mason.")
print(f"Player Rules created by: Dazion, Logan, Damian, Zane and Avonta.")