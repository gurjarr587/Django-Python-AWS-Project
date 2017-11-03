import random
turn = 0
score =0
score_this_turn = 0
turn_over = False
game_over = False

def main():
    display_rules()
    play_game()

def display_rules():
    print(" Lets play the game ")
    print()
    print("* See how many turns it takes you to get to 20")
    print("* Turn ends when you hold or roll 1.")
    print("* if you roll a 1, you lose all the points for the turn. ")
    print("* if you hold, you save all the points for the turn")
    print()

def play_game():
    while not game_over:
        take_turn()
    print()
    print("game over!")

def take_turn():
    global turn_over

    print("TURN", turn)
    turn_over = False
    while not turn_over:
        choice = input("Roll or Hold? (r/h) : ")
        if choice == "r":
            roll_die()
        elif choice == "h":
            hold_turn()
        else:
            print("invalid choice for the input")

def roll_die():
    global turn_over,turn,score_this_turn

    die = random.randint(1, 6)
    if die == 1:
        turn += 1
        print("turn over No score \n")
        score_this_turn += 0
        turn_over = True
    else:
        score_this_turn += die

def hold_turn():
    global turn, score_this_turn, score, turn_over, game_over

    print("score for the turn:", score_this_turn)
    score += score_this_turn
    score_this_turn = 0
    print("total score:", score, "\n")

    turn_over = True
    if score >= 20:
        game_over = True
        print("you finished in",turn,"turns!")

    turn += 1
# if started as the main module, call the main function
if __name__ == "__main__":
    main()

