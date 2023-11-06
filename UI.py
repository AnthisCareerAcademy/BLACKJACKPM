import random
import string

suits = ['♠', '♣', '♢', '♡']
numbers = [i for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
deck = []
player_hand = []
player_split_hand = []
dealer_hand = []
splitable = True
dealer_points = 0
player_points = 0



def card_value(card):
    if card[0] in ['J', 'Q', 'K']:
        return 10
    elif card[0] == 'A':
        return 11
    else:
        return int(card[0])


def draw_cards(hand, isDealer):
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
        if isDealer and index == 0:
            complete_drawn_hand.append(
                [" _________ ", "|???      |", "|         |", "|   ???   |", "|         |", "|______???|"])
        for beep in range(6):
            if isDealer and index == 0:
                continue
            else:

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

        if drawn_card:

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


def bust_check(hand, is_hand) -> bool:
    # bust
    if is_hand:

        while True:
            hand_score = sum(card_value(card) for card in hand)
            if hand_score > 21:
                return True
            else:
                return False
    else:
        if hand > 21:
            return True
        else:
            return False


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


def who_wins(player_score, dealer_score) -> bool:
    if player_score == dealer_score:
        return False
    elif player_score == 21:
        return True
    elif dealer_score == 21:
        return False
    elif player_score > 21:
        return False
    elif dealer_score > 21:
        return True
    elif player_score > dealer_score:
        return True
    elif player_score < dealer_score:
        return False
    else:
        return None


# only called when we already ask the user if they want to split


# split(player_hand.pop())
# def split(player_split_card):
#     # we don't need conversions - UI
#     #     if x == 'J' or x == "Q" or x == "K":
#     #         x = 10
#     #     if x == 'A':
#     #         x = 11
#     # Add x to the split hand
#     player_split_hand.append(player_split_card)
#     draw_cards(player_split_hand)
#
#     # d = deck[0][0]  # Check to see if face card after hit first card in split
#
#     #     if d == 'J' or d == 'Q' or d == 'K':
#     #         d = 10
#     #         player_split_hand.append(d)
#     #         hit(cards)
#     #         # card_1 = deck.pop(0)
#     #         #         cards.append(card_1)
#
#     #     elif d == 'a':
#     #         d = 11
#     #         player_split_hand.append(d)
#     #         hit(cards)
#     #         # card_1 = deck.pop(0)
#     #         #         cards.append(card_1)
#     # else:
#     # player_split_hand.append(deck[0])
#
#     # if they want to hit
#     hit(player_split_hand)
#     # card_1 = deck.pop(0)
#     #         cards.append(card_1)
#
#     draw_cards(player_split_hand)
#
#     # game loop don't need this - UI
#     # split_hit = input("Would you like to hit or stand? ")
#     #     while split_hit == 'hit':
#     #         d = deck[0][0]
#     #         if d == 'j' or d == 'q' or d == 'k':
#     #             d = 10
#     #             player_split_hand.append(d)
#     #             card = deck.pop(0)
#     #             cards.append(card)
#     #         elif d == 11:
#     #             d = 11
#     #             player_split_hand.append(d)
#     #             card = deck.pop(0)
#     #             cards.append(card)
#     #
#     #         else:
#     #             player_split_hand.append(deck[0][0])
#     #             card = deck.pop(0)
#     #             cards.append(card)
#     #         print(player_split_hand)
#     #         split_hit = input("Would you like to hit or stand? ")
#     # print(player_split_hand)
#     # print(cards)

def game_loop(double_down):
    global splitable, dealer_points, player_points
    player_score = 0
    dealer_score = 0
    if deck:
        deck.clear()
    if player_hand:
        player_hand.clear()
    if player_split_hand:
        player_split_hand.clear()
    if dealer_hand:
        dealer_hand.clear()

    create_deck()

    # Intro for the games stating your name and age, then rules
    # print("Welcome to BlackJack\n")
    #
    #     name = input('Would you state your name: ')
    #     print('Hello, ' + name)
    #
    #     while True:
    #
    #         age = input('Would you state your age: ')
    #         if age.isdecimal():
    #             break
    #         else:
    #             print("Please type an integer")
    #     print(age)

    print("\nThe rule for this game is to get close to 21 without going over. ")
    print("The Ace rules is 11 or 1 - it will auto pick based on if over 21 (built)")
    print("The split is to compare both player hands to dealer. Each hand scored individually.")
    print("The double down would be the player wins 2 pts awarded, if they lose then 2 pts goes to the dealer")
    print("The scores hand would be the total amount for player and dealer.")

    print("\nStarting The Game!")

    # populating the hands with cards
    hit(player_hand)
    hit(dealer_hand)
    hit(player_hand)
    hit(dealer_hand)

    print(f'player hand: ')
    draw_cards(player_hand, False)
    print(f'dealer hand: ')
    draw_cards(dealer_hand, True)

    # hitting aspect of player
    while True:

        # Dealer Scoring
        if player_hand[0][0] == player_hand[1][0]:
            if splitable:
                while True:

                    do_i_hit = standardize(input('would you like to split? (YES/NO): '))
                    if do_i_hit == 'yes':
                        split_game_loop(double_down)
                        break
                    elif do_i_hit == 'no':
                        splitable = False
                        break
                    else:
                        print("Please choose a valid option")

        do_i_hit = standardize(input('would you like to hit or stand?(hit/stand): '))
        if do_i_hit == 'hit':

            print('dealing hands..."')
            hit(player_hand)
            print(f'players hand: ')
            draw_cards(player_hand, False)
        elif do_i_hit == 'stand':
            print('moving on to dealer')
            break
        else:
            print('Please choose a valid option')

        player_score = sum(card_value(card) for card in player_hand)

        if bust_check(player_hand, True):
            print("YOU BUSTED")
            break

    # Dealer Code here
    while not bust_check(dealer_hand, True):
        dealer_score = sum(card_value(card) for card in dealer_hand)

        if bust_check(dealer_hand, True):
            print("DEALER BUST")
            break
        elif dealer_score <= 16:
            hit(dealer_hand)
            continue
        elif dealer_score >= 17:
            break

    # comparisons here
    # True if player wins false if not
    print("Player hand: ")
    draw_cards(player_hand, False)
    print("Dealer hand: ")
    draw_cards(dealer_hand, False)
    if who_wins(player_score, dealer_score):
        print('Player wins')
        if double_down:
            player_points += 2
        else:
            player_points += 1
    elif not who_wins(player_score, dealer_score):
        print('Dealer wins')
        if double_down:
            dealer_points += 2
        else:
            dealer_points += 1

    else:
        while True:

            double_down = standardize(input('would you like to double down?(yes/no): '))
            if double_down == 'yes':
                print('doubling bet..."')
                game_loop(True)
                break
            elif double_down == 'no':
                break
            else:
                print("Please choose a valid option.")
        # THIS IS USER STUFF NOT SUPPOSED TO BE IN DEALERS STUFF
        #         if player_score > 21:
        #             print(player_hand)
        #             print('Player busted')
        #         if bust_check(player_hand) and bust_check(dealer_hand):
        #             double_down = standardize(input('would you like to double down?(Y/N): '))
        #             if double_down == 'Y':
        #                 print('doubling bet..."')
        #                 game_loop(True)
        #             if double_down == 'N':
        #                 print('moving to dealer')
        #             break

    # Some comparison work that some people didn't even finish???? -Martin
    #     if dealer_score == player_score:
    #         print('PUSH LOSER')
    #     if dealer_score == 21:
    #         print('Dealer Wins, Dealer has Blackjack')
    #     if player_score == 21:
    #         print('YOU GOT BLACKJACK')

    # Yes and No to play again
    print('Player Points:', player_points)
    print('Dealer Points:', dealer_points)
    play_again = standardize(input("do you want to play again? Yes or NO?\n"))
    if play_again == "yes":
        print("Starting a new game!")
        game_loop(None)
    elif play_again == "no":
        print("Game End!\n")
        # break out of game loop


def split_game_loop(double_down):
    global splitable, player_points, dealer_points
    player_split_hand.append(player_hand.pop())
    # hitting aspect of player
    while True:

        # Dealer Scoring if sum(card_value(card) for card in player_hand) > sum(card_value(card) for card in
        # player_split_hand): player_score = sum(card_value(card) for card in player_hand) elif sum(card_value(card)
        # for card in player_hand) < sum(card_value(card) for card in player_split_hand): player_score = sum(
        # card_value(card) for card in player_split_hand) else: player_score = sum(card_value(card) for card in
        # player_split_hand)

        do_i_hit = standardize(input('would you like to hit or stand?(hit/stand): '))
        if do_i_hit == 'hit':

            print('dealing hands..."')
            hit(player_hand)
            print(f'players hand: ')
            draw_cards(player_hand, False)
            draw_cards(player_split_hand, False)
        elif do_i_hit == 'stand':
            break
        else:
            print('Please choose a valid option')

        player_score = sum(card_value(card) for card in player_hand)
        player_split_score = sum(card_value(card) for card in player_split_hand)

        if bust_check(player_hand, True):
            print("YOU BUSTED")
            break

    while True:

        # Dealer Scoring if sum(card_value(card) for card in player_hand) > sum(card_value(card) for card in
        # player_split_hand): player_score = sum(card_value(card) for card in player_hand) elif sum(card_value(card)
        # for card in player_hand) < sum(card_value(card) for card in player_split_hand): player_score = sum(
        # card_value(card) for card in player_split_hand) else: player_score = sum(card_value(card) for card in
        # player_split_hand)

        do_i_hit = standardize(input('would you like to hit or stand?(hit/stand): '))
        if do_i_hit == 'hit':

            print('dealing hands..."')
            hit(player_split_hand)
            print(f'players hand: ')
            draw_cards(player_hand, False)
            draw_cards(player_split_hand, False)
        elif do_i_hit == 'stand':
            break
        else:
            print('Please choose a valid option')

        player_score = sum(card_value(card) for card in player_hand)

        if bust_check(player_split_hand, True):
            print("YOU BUSTED")
            break

    while not bust_check(dealer_hand, True):
        dealer_score = sum(card_value(card) for card in dealer_hand)

        if bust_check(dealer_hand, True):
            print("DEALER BUST")
            break
        elif dealer_score <= 16:
            hit(dealer_hand)
            continue
        elif dealer_score >= 17:
            break

    # comparisons here
    # True if player wins false if not
    print("Player hands: ")
    draw_cards(player_hand, False)
    draw_cards(player_split_hand, False)
    print("Dealer hand: ")
    draw_cards(dealer_hand, False)
    if who_wins(player_score, dealer_score) or who_wins(player_split_score, dealer_score):
        print('Player wins')
        if double_down:
            player_points += 2
        else:
            player_points += 1
    elif not who_wins(player_score, dealer_score) or not who_wins(player_split_score, dealer_score):
        print('Dealer wins')
        if double_down:
            dealer_points += 2
        else:
            dealer_points += 1

    else:
        while True:

            double_down = standardize(input('would you like to double down?(yes/no): '))
            if double_down == 'yes':
                print('doubling bet..."')
                game_loop(True)
                break
            elif double_down == 'no':
                break
            else:
                print("Please choose a valid option.")
            # THIS IS USER STUFF NOT SUPPOSED TO BE IN DEALERS STUFF
            #         if player_score > 21:
            #             print(player_hand)
            #             print('Player busted')
            #         if bust_check(player_hand) and bust_check(dealer_hand):
            #             double_down = standardize(input('would you like to double down?(Y/N): '))
            #             if double_down == 'Y':
            #                 print('doubling bet..."')
            #                 game_loop(True)
            #             if double_down == 'N':
            #                 print('moving to dealer')
            #             break

        # Some comparison work that some people didn't even finish???? -Martin
        #     if dealer_score == player_score:
        #         print('PUSH LOSER')
        #     if dealer_score == 21:
        #         print('Dealer Wins, Dealer has Blackjack')
        #     if player_score == 21:
        #         print('YOU GOT BLACKJACK')

        # Yes and No to play again

    # Yes and No to play again
    play_again = standardize(input("do you want to play again? Yes or NO?\n"))
    if play_again == "yes":
        print("Starting a new game!")
        game_loop(None)
    elif play_again == "no":
        print("Game End!\n")
        # break out of game loop


# split(['K', '♠'])
# split(['Q', '♠'])
# checking out the deck
# print(deck)


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

game_loop(None)

# credit

print(f"UI created by: Martin, Okkar, Brodie, and Pika.")
print(f"Dealer Tasks created by: Indy, Obeth, and Mason.")
print(f"Player Rules created by: Dazion, Logan, Damian, Zane and Avonta.")
