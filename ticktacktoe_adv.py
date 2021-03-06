from random import randrange

print("start!")
tictac_list = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player_1row = 0
player_1col = 0
player_2row = 0
player_2col = 0
turns = 0
row_l = [1, 2, 3]
# functions
def board_print():
    print("   1     2     3")
    for space in range(0, 3):
        print("+-----+-----+-----+")
        for position in range(0, 3):
            print("|  " + tictac_list[space][position] + "  ", end="")
        print(f"|  {space+1}")
    print("+-----+-----+-----+")


def computers_move_rad():
    player_2row = randrange(1, 4)
    player_2col = randrange(1, 4)
    while (player_2row not in row_l) or (player_2col not in row_l) or tictac_list[player_2row - 1][
        player_2col - 1] != " ":
        player_2row = randrange(1, 4)
        player_2col = randrange(1, 4)
    else:
        tictac_list[player_2row - 1][player_2col - 1] = "O"


def computers_move_smart():
    if turns == 1 and tictac_list[1][1] == " ":
        tictac_list[1][1] = "O"
        return
    elif turns == 1:
        tictac_list[0][0] = "O"
        return
    for j in range(0, 3):
        if tictac_list[j][0] ==  tictac_list[j][1] != " " and tictac_list[j][2] == " ":
            tictac_list[j][2] = "O"
            return
        elif tictac_list[j][0] ==  tictac_list[j][2] != " " and tictac_list[j][1] == " ":
            tictac_list[j][1] = "O"
            return
        elif tictac_list[j][1] ==  tictac_list[j][2] != " " and tictac_list[j][0] == " ":
            tictac_list[j][0] = "O"
            return
    for i in range(0, 3):
        if tictac_list[0][i] ==  tictac_list[1][i] != " " and tictac_list[2][i] == " ":
            tictac_list[2][i] = "O"
            return
        elif tictac_list[0][i] ==  tictac_list[2][i] != " " and tictac_list[1][i] == " ":
            tictac_list[1][i] = "O"
            return
        elif tictac_list[1][i] ==  tictac_list[2][i] != " " and tictac_list[0][i] == " ":
            tictac_list[0][i] = "O"
            return
    if tictac_list[0][0] ==  tictac_list[1][1] != " " and tictac_list[2][2] == " ":
        tictac_list[2][2] = "O"
        return
    elif tictac_list[1][1] == tictac_list[2][2] != " " and tictac_list[0][0] == " ":
        tictac_list[0][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[1][1] != " " and tictac_list[2][0] == " ":
        tictac_list[2][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[2][0] != " " and tictac_list[0][2] == " ":
        tictac_list[0][2] = "O"
        return
    player_2row = randrange(1, 4)
    player_2col = randrange(1, 4)
    while (player_2row not in row_l) or (player_2col not in row_l) or tictac_list[player_2row - 1][
        player_2col - 1] != " ":
        player_2row = randrange(1, 4)
        player_2col = randrange(1, 4)
    else:
        tictac_list[player_2row - 1][player_2col - 1] = "O"

def computer_move_smarter():
    if turns == 1 and tictac_list[1][1] == " ":
        tictac_list[1][1] = "O"
        return
    elif turns == 1:
        tictac_list[0][0] = "O"
        return
    for j in range(0, 3):
        if tictac_list[j][0] ==  tictac_list[j][1] == "O" and tictac_list[j][2] == " ":
            tictac_list[j][2] = "O"
            return
        elif tictac_list[j][0] ==  tictac_list[j][2] == "O" and tictac_list[j][1] == " ":
            tictac_list[j][1] = "O"
            return
        elif tictac_list[j][1] ==  tictac_list[j][2] == "O" and tictac_list[j][0] == " ":
            tictac_list[j][0] = "O"
            return
    for i in range(0, 3):
        if tictac_list[0][i] ==  tictac_list[1][i] == "O" and tictac_list[2][i] == " ":
            tictac_list[2][i] = "O"
            return
        elif tictac_list[0][i] ==  tictac_list[2][i] == "O" and tictac_list[1][i] == " ":
            tictac_list[1][i] = "O"
            return
        elif tictac_list[1][i] ==  tictac_list[2][i] == "O" and tictac_list[0][i] == " ":
            tictac_list[0][i] = "O"
            return
    if tictac_list[0][0] ==  tictac_list[1][1] == "O" and tictac_list[2][2] == " ":
        tictac_list[2][2] = "O"
        return
    elif tictac_list[1][1] == tictac_list[2][2] == "O" and tictac_list[0][0] == " ":
        tictac_list[0][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[1][1] == "O" and tictac_list[2][0] == " ":
        tictac_list[2][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[2][0] == "O" and tictac_list[0][2] == " ":
        tictac_list[0][2] = "O"
        return
    for j in range(0, 3):
        if tictac_list[j][0] ==  tictac_list[j][1] != " " and tictac_list[j][2] == " ":
            tictac_list[j][2] = "O"
            return
        elif tictac_list[j][0] ==  tictac_list[j][2] != " " and tictac_list[j][1] == " ":
            tictac_list[j][1] = "O"
            return
        elif tictac_list[j][1] ==  tictac_list[j][2] != " " and tictac_list[j][0] == " ":
            tictac_list[j][0] = "O"
            return

    for i in range(0, 3):
        if tictac_list[0][i] ==  tictac_list[1][i] != " " and tictac_list[2][i] == " ":
            tictac_list[2][i] = "O"
            return
        elif tictac_list[0][i] ==  tictac_list[2][i] != " " and tictac_list[1][i] == " ":
            tictac_list[1][i] = "O"
            return
        elif tictac_list[1][i] ==  tictac_list[2][i] != " " and tictac_list[0][i] == " ":
            tictac_list[0][i] = "O"
            return

    if tictac_list[0][0] ==  tictac_list[1][1] != " " and tictac_list[2][2] == " ":
        tictac_list[2][2] = "O"
        return
    elif tictac_list[1][1] == tictac_list[2][2] != " " and tictac_list[0][0] == " ":
        tictac_list[0][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[1][1] != " " and tictac_list[2][0] == " ":
        tictac_list[2][0] = "O"
        return
    elif tictac_list[0][2] == tictac_list[2][0] != " " and tictac_list[0][2] == " ":
        tictac_list[0][2] = "O"
        return
    if turns == 3 and tictac_list[0][2] == " " and tictac_list[1][1] == "X":
        tictac_list[0][2] = "O"
        return
    elif turns == 3 and tictac_list[1][1] == "X":
        tictac_list[2][0] = "O"
        return
    elif turns ==3 and tictac_list[0][0] == tictac_list[2][2] != " " and tictac_list[1][0] == " ":
        tictac_list[1][0] = "O"
        return
    elif turns ==3 and " " != tictac_list[1][1] != tictac_list[2][2] != " " and tictac_list[0][0] == " ":
        tictac_list[0][0] = "O"
        return
    elif turns ==3 and " " != tictac_list[1][1] != tictac_list[0][0] != " " and tictac_list[2][2] == " ":
        tictac_list[2][2] = "O"
        return
    elif turns ==3 and " " != tictac_list[1][1] != tictac_list[0][2] != " " and tictac_list[2][0] == " ":
        tictac_list[2][0] = "O"
        return
    elif turns ==3 and " " != tictac_list[1][1] != tictac_list[2][0] != " " and tictac_list[0][2] == " ":
        tictac_list[0][2] = "O"
        return
    elif turns ==3 and tictac_list[0][2] == tictac_list[2][0] != " ":
        tictac_list[1][0] = "O"
        return
    elif turns == 3 and tictac_list[0][2] == " ":
        tictac_list[0][2] = "O"
        return
    elif turns == 3:
        tictac_list[2][0] = "O"
        return
    player_2row = randrange(1, 4)
    player_2col = randrange(1, 4)
    while (player_2row not in row_l) or (player_2col not in row_l) or tictac_list[player_2row - 1][
        player_2col - 1] != " ":
        player_2row = randrange(1, 4)
        player_2col = randrange(1, 4)
    else:
        tictac_list[player_2row - 1][player_2col - 1] = "O"

# start
print("choose difficulty")
dif_level = input("easy (press 1), hard (press 2), impossible (press 3):")
while dif_level != "1" and dif_level != "2" and dif_level != "3":
    dif_level = input("easy (press 1), hard (press 2), impossible (press 3):")
dif_level = int(dif_level)
board_print()
while turns != 9:
# players move
    print("players move")
    player_1row = int(input("give number of row:"))
    player_1col = int(input("give number of col: "))
    while (player_1row not in row_l) or (player_1col not in row_l) or tictac_list[player_1row-1][player_1col-1] != " ":
        print("can not put it there choose again.")
        player_1row = int(input("give number of row:"))
        player_1col = int(input("give number of col: "))
    else:
        tictac_list[player_1row-1][player_1col-1] = "X"
    board_print()
# check for victory
    for j in range(0, 3):
        if tictac_list[j][0] == "X" and tictac_list[j][1] == "X" and tictac_list[j][2] == "X":
            print("you won!")
            turns = 11
            break
    for j in range(0, 3):
        if tictac_list[0][j] == "X" and tictac_list[1][j] == "X" and tictac_list[2][j] == "X":
            print("you won!")
            turns = 11
            break
    if tictac_list[0][0] == "X" and tictac_list[1][1] == "X" and tictac_list[2][2] == "X":
        print("you won!")
        turns = 11
        break
    if tictac_list[2][0] == "X" and tictac_list[1][1] == "X" and tictac_list[0][2] == "X":
        print("you won!")
        turns = 11
        break
# checj for drw
    turns += 1
    if turns >= 9:
        break
# computer
    print("computers turn")
    if dif_level == 1:
        computers_move_rad()
    elif dif_level == 2:
        computers_move_smart()
    else:
        computer_move_smarter()
    board_print()
# check for victory
    for j in range(0, 3):
        if tictac_list[j][0] == "O" and tictac_list[j][1] == "O" and tictac_list[j][2] == "O":
            print("computer won")
            turns = 11
            break
    for j in range(0, 3):
        if tictac_list[0][j] == "O" and tictac_list[1][j] == "O" and tictac_list[2][j] == "O":
            print("computer won")
            turns = 11
            break
    if tictac_list[0][0] == "O" and tictac_list[1][1] == "O" and tictac_list[2][2] == "O":
        print("computer won")
        turns = 11
        break
    if tictac_list[2][0] == "O" and tictac_list[1][1] == "O" and tictac_list[0][2] == "O":
        print("computer won")
        turns = 11
        break
    turns += 1
    if turns >= 9:
        break


if turns == 9:
    print("draw!")
