import random
import PySimpleGUI as sg

block_words = "abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz"
word_list = block_words.split(" ")
# the hangman print
hangman_dict = {"first": "_____\n",
                "second": "|       ",
                1: " ",
                "mistake": "\n",
                "third": "|       ",
                2: " ",
                "fourth": "\n",
                "fifth": "|      ",
                3: " ",
                4: " ",
                5: " ",
                "seventh": "\n",
                "eighth": "|      ",
                6: " ",
                "ninth": " ",
                7: " ",
                "tenth": "\n"}

parts_dict = {1: "|",
              2: "o",
              3: "/",
              4: "|",
              5: "\\",
              6: "/",
              7: "\\"}
# to check if the input of the player is correct and not in other language
alphabet_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]


# functions
def select_word():  # find the word make it a list
    rad_num = random.sample(range(0, len(word_list)), 1)
    secret_word = word_list[rad_num[0]]
    letter_list = list(secret_word)
    return secret_word, letter_list


def create_hidden(array):  # make a list with underscores anf a string (input is list)
    hidden_list = []
    for i in range(len(array)):
        hidden_list.append("_")
    return hidden_list


def hid_str(array):
    st = ""
    for el in array:
        st += el
        st += " "
    return st


def hangman_str(dic):  # make dic into str
    st = ""
    for key in dic:
        st += dic[key]
    return st


# construct the window
# start with the layout

the_gallow = hangman_str(hangman_dict)
message_str = "start"
guess_set = set()
sec_word, letter_list = select_word()
hidden_list = create_hidden(letter_list)
hid_text = hid_str(hidden_list)
layout = [
    [sg.Text(the_gallow, key='-TEXT1-')],
    [sg.Text(hid_text, key='-TEXT2-')],
    [sg.Text(message_str, key='-TEXT3-')],
    [sg.Text(" ", key='-TEXT4-'), sg.Text(" ", key='-REPLAY-', enable_events=True)],
    [sg.Text(f"Letters already used: {guess_set}", key='-TEXT5-')],
    [sg.Text('Guess a letter:'), sg.Input(key='-INPUT-', do_not_clear=False)],
    [sg.Button('OK', bind_return_key=True), sg.Button('Give up'), sg.Button('Leave')]
]
window = sg.Window("Hangman", layout)
# start the game
t_tries = 0

while True:
    event, values = window.read()
    if event == 'Give up':
        window['-TEXT3-'].update(f"The word was: {sec_word}")
        window['-REPLAY-'].update("Replay? (Click here)")
    if event == 'OK':
        the_letter = values['-INPUT-']
        the_letter = str(the_letter).lower()
        if the_letter not in alphabet_list:
            window['-TEXT3-'].update("Input must be one english letter")
        elif the_letter in guess_set:
            window['-TEXT3-'].update("Letter already picked")
        elif the_letter in letter_list:
            window['-TEXT3-'].update("Correct!")
            guess_set.add(the_letter)
            window['-TEXT5-'].update(f"Letters already used: {guess_set}")
            for i in range(len(letter_list)):
                if letter_list[i] == the_letter:
                    hidden_list[i] = letter_list[i]
            hid_text = hid_str(hidden_list)
            window['-TEXT2-'].update(hid_text)
        else:
            t_tries += 1
            window['-TEXT3-'].update("Incorrect!")
            guess_set.add(the_letter)
            window['-TEXT5-'].update(f"Letters already used: {guess_set}")
            hangman_dict[t_tries] = parts_dict[t_tries]
            the_gallow = hangman_str(hangman_dict)
            window['-TEXT1-'].update(the_gallow)
    if "_" not in hidden_list:
        window['-TEXT4-'].update("Victory!")
        window['-TEXT3-'].update(f"Well done")
        window['-REPLAY-'].update("Replay?(Click here)")
    if t_tries == 7:
        window['-TEXT4-'].update("You lost")
        window['-TEXT3-'].update(f"The word was: {sec_word}")
        window['-REPLAY-'].update("Replay?(Click here)")
    if event == '-REPLAY-':
        hangman_dict = {"first": "_____\n",
                        "second": "|       ",
                        1: " ",
                        "mistake": "\n",
                        "third": "|       ",
                        2: " ",
                        "fourth": "\n",
                        "fifth": "|      ",
                        3: " ",
                        4: " ",
                        5: " ",
                        "seventh": "\n",
                        "eighth": "|      ",
                        6: " ",
                        "ninth": " ",
                        7: " ",
                        "tenth": "\n"}
        the_gallow = hangman_str(hangman_dict)
        message_str = "start"
        guess_set = set()
        sec_word, letter_list = select_word()
        hidden_list = create_hidden(letter_list)
        hid_text = hid_str(hidden_list)
        t_tries = 0
        window['-TEXT1-'].update(the_gallow)
        window['-TEXT2-'].update(hid_text)
        window['-TEXT3-'].update(message_str)
        window['-TEXT4-'].update(" ")
        window['-TEXT5-'].update(f"Letters already used: {guess_set}")
        window['-REPLAY-'].update(" ")

    if event == sg.WIN_CLOSED or event == 'Leave':
        break

window.close()
