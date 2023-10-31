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
