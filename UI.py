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

print(deck)

