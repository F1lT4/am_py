from random import randrange
import json
# the constants
the_words = []
game_word = []
word_one = ""
board_dic = [
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " "]
]
try:
    with open("score.json", "r") as score:
        score_dic = json.load(score)
except FileNotFoundError:
    score_dic = {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 0,
        "6": 0
    }
try:
    with open("percent.json", "r") as perc:
        percent = json.load(perc)
except FileNotFoundError:
    percent = {
        "wins": 0,
        "loses": 0
    }
# functions
# import the list


def make_the_list():
    global the_words
    # start empty str (st) and add every line
    st = ""
    with open("wordlist.text") as main_str:
        for line in main_str:
            st += str(line).lower()
            # divide the str
    the_words = st.split("\n")


def choose_word():
    global the_words, game_word, word_one
    # choose the word randomly from the list
    rad_num = randrange(len(the_words))
    word_one = the_words[rad_num]
    # make a list of the letters
    for letter in word_one:
        game_word.append(letter)


def board_print():
    print("+---+---+---+---+---+")
    i = 0
    for element in board_dic:
        for value in element:
            print(f"| {value} ", end="")
        print("|")
        i += 1
        if i % 2 == 0:
            print("+---+---+---+---+---+")


def score_print():
    num = percent["wins"] + percent["loses"]
    win_rate = round(percent["wins"] / num * 100)
    print(f"{num} game played. {percent['wins']} games won.")
    print(f"Win rate {win_rate} %")
    print("-"*30)
    for i in range(1, 7):
        print(str(i) + ":" + "=" * score_dic[str(i)] + " ("+str(score_dic[str(i)]) + ")")

# main function


def main_game():
    global the_words, word_one, game_word, board_dic
    make_the_list()
    choose_word()
    board_print()
    player_list = []
    # turns
    i = 0
    # boards place
    ind = 0
    # start the loop
    while i != 6:
        # player fives guess
        # enter loop for correction
        while True:
            try:
                players_guess = input("Give a 5 letter word: ").lower()
                if players_guess not in the_words:
                    print("Input not in the word list")
                    raise ValueError("mistake")
                elif players_guess == "":
                    print("At least put a word in")
                    raise ValueError("mistake")
                else:
                    break
            except ValueError:
                print("try again")
        player_list.clear()
        for letter in players_guess:
            player_list.append(letter)

        # check the letters
        # make a decoy list
        decoy_list = game_word[:]
        for z in range(len(player_list)):
            board_dic[ind][z] = player_list[z]
        for j in range(len(player_list)):
            if player_list[j] == decoy_list[j]:
                board_dic[ind+1][j] = "="
                decoy_list[j] = " "
        for j in range(len(player_list)):
            if player_list[j] in decoy_list:
                if board_dic[ind + 1][j] == " ":
                    board_dic[ind + 1][j] = "-"
                    decoy_list[decoy_list.index(player_list[j])] = " "

        board_print()

        if players_guess == word_one:
            print(f"Victory in {i+1} tries")
            score_dic[str(i+1)] += 1
            with open("score.json", "w") as scr:
                json.dump(score_dic, scr)
            percent["wins"] += 1
            with open("percent.json", "w") as f:
                json.dump(percent, f)
            return
        i += 1
        ind += 2
    else:
        print(f"You lost. The word was {word_one}")
        percent["loses"] += 1
        with open("percent.json", "w") as f:
            json.dump(percent, f)
        return


# start the game
state = "yes"
while state != "no":
    the_words = []
    game_word = []
    word_one = ""
    board_dic = [
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " "]
    ]
    main_game()
    score_print()
    while True:
        state = input("Do you want to play again?(yes or no)").lower()
        if state == "yes" or state == "no":
            break

print("Bye bye!")
