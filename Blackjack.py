# starting variables
card_colour = ["♠", "♦", "♣", "♥"]
card_type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
the_cards = set()
Ace = 0
sum_com = 0
sum_play = 0
players_hand = []
mothers_hand = []
los_win = False
# functions


def shuffle_c():
    for type_of in card_type:
        for colour in card_colour:
            a_card = (type_of, colour)
            the_cards.add(a_card)
    return the_cards


def card_value(pos):
    if str(players_hand[pos][0]).isdigit():
        value = int(players_hand[pos][0])
    elif players_hand[pos][0] in ["K", "J", "Q"]:
        value = 10
    else:
        if pos == 0 and players_hand[pos][0] == players_hand[pos + 1][0] == "A":
            value = 1
        elif sum_play > 21:
            value = 1
        elif sum_play == 0:
            value = 11
        else:
            value = 11
    return value


def computer_value(pos):
    if str(mothers_hand[pos][0]).isdigit():
        points = int(mothers_hand[pos][0])
    elif mothers_hand[pos][0] in ["K", "J", "Q"]:
        points = 10
    else:
        if pos == 0 and mothers_hand[pos][0] == mothers_hand[pos + 1][0] == "A":
            points = 1
        elif sum_com > 21:
            points = 1
        elif sum_com == 0:
            points = 11
        else:
            points = 11
    return points


def players_sum():
    hand_list = []
    for i in range(0, len(players_hand)):
        hand_list.append(card_value(i))
    return sum(hand_list)


def mothers_sum():
    hand_list = []
    for i in range(0, len(mothers_hand)):
        hand_list.append(computer_value(i))
    return sum(hand_list)


def dis_win():
    global los_win
    if sum_play <= sum_com <= 21:
        los_win = True
    elif sum_com > 21:
        los_win = False


# start of the game


shuffle_c()


for _ in range(0, 2):
    mothers_hand.append(the_cards.pop())
    players_hand.append(the_cards.pop())

print(f"Your cards are: {players_hand}")
print(f"the mothers first card is {mothers_hand[1]}")
status = ""
sum_play = players_sum()
while True:
    if sum_play == 21:
        break
    status = input("Do you draw another card?('draw'-'pass'): ").lower()
    while status != "draw" and status != "pass":
        status = input("Do you draw another card? type the words:'draw' or 'pass':").lower()
    if status == "draw":
        players_hand.append(the_cards.pop())
        print(f"Your cards are: {players_hand}")
        sum_play = players_sum()
        if sum_play > 21:
            sum_play = players_sum()
            if sum_play > 21:
                break
    else:
        break

if sum_play > 21:
    print("I am sorry you lost! :(")
    print(f"The dealers cards are: {mothers_hand}")
elif sum_play == 21:
    print("Blackjack! You won!")
else:
    print(f"Your cards are: {players_hand}")
    print(f"The dealers cards are: {mothers_hand}")
    sum_com = mothers_sum()
    dis_win()
    while True:
        if los_win:
            break
        mothers_hand.append(the_cards.pop())
        sum_com = mothers_sum()
        dis_win()
        if sum_com > 21:
            sum_com = mothers_sum()
            if sum_com > 21:
                break
        print(f"The dealers cards are: {mothers_hand}")

    dis_win()
    if los_win:
        print(f"Your cards are: {players_hand},({sum_play})")
        print(f"The dealers cards are: {mothers_hand},({sum_com})")
        print('I am sorry you lost!')
    else:
        print(f"Your cards are: {players_hand},({sum_play})")
        print(f"The dealers cards are: {mothers_hand},({sum_com})")
        print('You won, great success! :)')
