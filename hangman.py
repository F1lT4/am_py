import random
block_words = "abruptly absurd abyss affix askew avenue awkward axiom azure bagpipes bandwagon banjo bayou beekeeper bikini blitz blizzard boggle bookworm boxcar boxful buckaroo buffalo buffoon buxom buzzard buzzing buzzwords caliph cobweb cockiness croquet crypt curacao cycle daiquiri dirndl disavow dizzying duplex dwarves embezzle equip espionage euouae exodus faking fishhook fixable fjord flapjack flopping fluffiness flyby foxglove frazzled frizzled fuchsia funny gabby galaxy galvanize gazebo giaour gizmo glowworm glyph gnarly gnostic gossip grogginess haiku haphazard hyphen iatrogenic icebox injury ivory ivy jackpot jaundice jawbreaker jaywalk jazziest jazzy jelly jigsaw jinx jiujitsu jockey jogging joking jovial joyful juicy jukebox jumbo kayak kazoo keyhole khaki kilobyte kiosk kitsch kiwifruit klutz knapsack larynx lengths lucky luxury lymph marquis matrix megahertz microwave mnemonic mystify naphtha nightclub nowadays numbskull nymph onyx ovary oxidize oxygen pajama peekaboo phlegm pixel pizazz pneumonia polka pshaw psyche puppy puzzling quartz queue quips quixotic quiz quizzes quorum razzmatazz rhubarb rhythm rickshaw schnapps scratch shiv snazzy sphinx spritz squawk staff strength strengths stretch stronghold stymied subway swivel syndrome thriftless thumbscrew topaz transcript transgress transplant triphthong twelfth twelfths unknown unworthy unzip uptown vaporize vixen vodka voodoo vortex voyeurism walkway waltz"
word_list = block_words.split(" ", 185)
# select a word randomly
rad_num = random.sample(range(0, len(word_list)), 1)
secret_word = word_list[rad_num[0]]
# make a list of th letters
letter_list = list(secret_word)
guess_set = set()
letter_dict = {}
# the hangman print
hangman_dict = {"first": "_____\n",
                "second": "|   ",
                1: " ",
                "mistake": "\n",
                "third": "|   ",
                2: " ",
                "fourth": "\n",
                "fifth": "|  ",
                3: " ",
                4: " ",
                5: " ",
                "seventh": "\n",
                "eighth": "|  ",
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

for key, value in hangman_dict.items():
    print(value, end="")
# dictionary of letters
for i in range(0, len(letter_list)):
    letter_dict[i] = letter_list[i]
# the hidden letter list
print("\n")
hidden_list = []
for element in letter_list:
    hidden_list.append("_")
for element in hidden_list:
    print(element, end=" ")
print(" ")
print("Let's start")
# start the game with the correct input and number of tries
t_tries = 0
while t_tries != 7:
    guess_letter = input("Guess the word! Give me one letter: ")
    while guess_letter.isalpha() is False or len(list(guess_letter)) != 1 or guess_letter in guess_set:
        guess_letter = input("Give me ONE new letter please: ")
    guess_letter = guess_letter.lower()
    if guess_letter in letter_list:
        print("Correct")
        guess_set.add(guess_letter)
        # change the list
        for key, value in letter_dict.items():
            if value == guess_letter:
                hidden_list[key] = guess_letter
        # hangman
        for key, value in hangman_dict.items():
            print(value, end="")
        print("\n")
        # prints
        for element in hidden_list:
            print(element, end=" ")
        print(" ")
        print(f"Letters you've already picked: {guess_set}")
        if "_" not in hidden_list:
            break
    else:
        print("Incorrect")
        t_tries += 1
        # hangman
        hangman_dict[t_tries] = parts_dict[t_tries]
        for key, value in hangman_dict.items():
            print(value, end="")
        print("\n")
        # prints
        for element in hidden_list:
            print(element, end=" ")
        print(" ")
        guess_set.add(guess_letter)
        print(f"Letters you've already picked: {guess_set}")

if t_tries == 7:
    print(f"You lost! The answer was: \"{secret_word}!\"")
else:
    print("Victory!")