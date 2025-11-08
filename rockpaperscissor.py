import random
while True:
    user_action = input("enter a choice (rock, paper, scissors): ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action},\n")
    optuts what is selected by you and computer

#conditions to check who won the game
    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie! ")
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smashes scisors! You win! ")
        else:
            print("Paper covers rock! you lose.")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! you win. ")
        else:
            print("sissors cuts paper! you losse! ")


    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cuts paper you win!  ")
        else:
            print("rock smashes scisors! You win! ")


    play_again = input("play agin? (y/n): ")
    if play_again != "y":
        break

    

