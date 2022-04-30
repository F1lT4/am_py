card_colour = ["spade", "diamond", "club", "heart"]
card_type = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
four_in_a_row = set()
for type_card in card_colour:
    the_Ace = (card_type[0], type_card)
    four_in_a_row.add(the_Ace)
import random
moirasma = 0
while True:
    the_cards = []
    for type_of in card_type:
        for colour in card_colour:
            a_card = (type_of, colour)
            the_cards.append(a_card)
    player_1 = set()
    for card_1 in range(0, 5):
        car_num_list = list(range(0, len(the_cards)))
        random_order_1 = random.sample(car_num_list, 1)
        hand = the_cards[sum(random_order_1)]
        player_1.add(hand)
        the_cards.pop(sum(random_order_1))
    print(player_1)

    player_2 = set()
    for card_2 in range(0, 5):
        car_num_list_2 = list(range(0, len(the_cards)))
        random_order_2 = random.sample(car_num_list_2, 1)
        hand_2 = the_cards[sum(random_order_2)]
        player_2.add(hand_2)
        the_cards.pop(sum(random_order_2))
    print(player_2)
    moirasma += 1
    lucky_1_1 = four_in_a_row.issubset(player_1)
    if lucky_1_1 is True:
        print("player 1 has four aces")
        break
    lucky_2_1 = four_in_a_row.issubset(player_2)
    if lucky_2_1 is True:
        print("player 2 has four aces")
        break
print(moirasma)