import time
import random

play_again = "yes"

while play_again == "yes":
    name = str(input("What is your name?\n>>> "))
    time.sleep(0.5)
    print("\nLet's play Rock, Paper, Scissors\n")
    time.sleep(0.5)
    number_of_rounds = input("How many rounds do you want to play?\n>>> ")
    try:
        number_of_rounds = int(number_of_rounds)
    except ValueError:
        print("You must choose a number")
        number_of_rounds = int(input("How many rounds do you want to play?\n>>> "))
    print("\nOkay, let's start")
    current_round = 1
    acceptable_choices = ("r", "p", "s", "rock", "paper", "scissors")
    while current_round != number_of_rounds + 1:
        time.sleep(0.5)
        print("\n\nROUND {}".format(current_round))
        time.sleep(0.3)
        print("Rock")
        time.sleep(0.2)
        print("Paper")
        time.sleep(0.2)
        print("Scissors")
        time.sleep(0.3)
        players_choice = ""
        computers_choice = 0
        player_victory = False
        computer_victory = False
        tie = False
        player_wins = 0
        computer_wins = 0
        while players_choice.lower() not in acceptable_choices:
            players_choice = input("\nWhat do you choose?\n>>> ")
            with open("choices.txt", "a+") as file:
                file.write("{} choose {},\n".format(name, players_choice))
        players_choice = players_choice.lower()
        if players_choice == "r":
            players_choice = "rock"
        elif players_choice == "p":
            players_choice = "paper"
        elif players_choice == "s":
            players_choice = "scissors"
        computers_choice = random.randint(1, 3)
        if computers_choice == 1:
            computers_choice = "scissors"
        elif computers_choice == 2:
            computers_choice = "paper"
        elif computers_choice == 3:
            computers_choice = "rock"

        time.sleep(0.3)
        print("\nI choose {}".format(computers_choice))

        if players_choice == "rock":
            if computers_choice == "scissors":
                player_victory = True
            if computers_choice == "paper":
                computer_victory = True
            if computers_choice == "rock":
                tie = True

        elif players_choice == "paper":
            if computers_choice == "rock":
                player_victory = True
            if computers_choice == "scissors":
                computer_victory = True
            if computers_choice == "paper":
                tie = True

        elif players_choice == "scissors":
            if computers_choice == "paper":
                player_victory = True
            if computers_choice == "rock":
                computer_victory = True
            if computers_choice == "scissors":
                tie = True
        time.sleep(0.5)

        if tie == True:
            print("\nIt was a tie")

        if player_victory == True:
            print("\nYou won that round")
            player_wins += 1

        if computer_victory == True:
            print("\nI win this round")
            computer_wins += 1

        time.sleep(0.5)

        current_round += 1
        print("\nComputer's Wins: {}\n{}'s Wins: {}".format(computer_wins, name,  player_wins))

    print("\n")

    if computer_wins > player_wins:
        print("YOU LOST")

    elif player_wins > computer_wins:
        print('YOU WON')

    elif player_wins == computer_wins:
        print("TIE")

