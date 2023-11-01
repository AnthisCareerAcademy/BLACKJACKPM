
dealer_score = 0
for value in dealer_hand:
    if value[0] == 'K':
        value[0] = 10
    elif value[0] == 'Q':
        value[0] = 10
    elif value[0] == 'J':
        value[0] = 10
    elif value[0] == 'A':
        value[0] = 11
    dealer_score += value[0]