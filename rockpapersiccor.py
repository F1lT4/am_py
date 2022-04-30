import random
# game information
game_info ={}
value_stat = {
    "rock": 0,
    "scissors": 1,
    "paper": 2,
}
# score
human = 0
computer = 0
g_round = 0
while human != 3 and computer != 3:
    # game choice list
    the_choices = ["rock", "paper", "scissors"]
    n = random.sample(range(0, 3), 1)
    # item value
    # player choice
    player_choice = input("rock, paper or scissors?: ")

    while player_choice not in the_choices:
        player_choice = input("only three choices: rock, paper or scissors? : ")
    #compare
    the_pc_choice = the_choices[n[0]]
    print("computer chose "+the_pc_choice)
    print("player chose "+player_choice)
    if value_stat[the_pc_choice]-value_stat[player_choice] == 0 :
        print("draw")
    elif value_stat[the_pc_choice]-value_stat[player_choice] == 1 :
        print("human wins")
        human += 1
    elif value_stat[the_pc_choice]-value_stat[player_choice] == -2 :
        print("human wins")
        human += 1
    else:
        print("computer wins")
        computer += 1
    print("human:compter "+str(human)+"-"+str(computer))
    g_round +=1
    score = str(str(human)+"-"+str(computer))
    game_info["Round "+str(g_round)] = {
        "player": player_choice,
        "computer": the_pc_choice,
        "score" : score}

if human > computer:
    print("the winner is human")
else:
    print("the winner is computer")
print(game_info)