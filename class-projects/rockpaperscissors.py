# Steps:

# 1. The first thing we want to implement is a loop that will keep the game running as long as the player wants to continue to play. (Hint: This should be the main foundation for your code, and should encase most of it.)

# 2. Next, we want to ask the player what move they want to choose, and then store it.

# 3. Once the player has inputted their choice, we now randomly generate the computer's choice. This can be done by importing random 
#    and then using random.choice()!

# 4. After both choices have been stored, you now need to compare them and see who wins! Remember that rock beats scissors, paper beats rock, and scissors beats paper.

# 5. Add a point to the winner and ask the player if they want to play again.
# If they say no, compare the two players’ points and print out the winner!

# Notes:
# If extra time, we can ask them to change this to be 2-player
# We can add extra spacing so that they can't see each other's answer

import random

play = True
player_points = 0
computer_points = 0

while play:
    print("Let's play rock, paper, scissors!")
    print("Type 's' for scissors, 'r' for rock, and 'p' for paper")
    player_choice = input("Player, enter your selection: ")
    while player_choice not in ["s","r","p"]:
        print("That is not a valid input. Please enter either 's','r', or 'p'")
        player_choice = input("Player, enter your selection: ")
    
    computer_choice = random.choice(['s', 'r', 'p'])

    mapping_choices = {'s':'Scissors','r':"Rock",'p':'Paper'}
    player_full_choice=mapping_choices[player_choice]
    computer_full_choice=mapping_choices[computer_choice]

    print(f"Player chose {player_full_choice}, computer chose {computer_full_choice}")

    # first, see if a draw
    if player_choice == computer_choice:
        print("It's a tie! No one gets a point")

    elif player_choice == "s" and computer_choice == "p":
        print("Player wins a point!")
        player_points += 1

    elif player_choice == "r" and computer_choice == "s":
        print("Player wins a point!")
        player_points += 1

    elif player_choice == "p" and computer_choice == "r":
        print("Player wins a point!")
        player_points += 1

    else:
        print("Computer wins a point!")
        computer_points += 1

    new_game = input("Do you want to play again? 'y' for yes, 'n' for no")
    if new_game == 'n':
        play = False

        # if false we exit and print final score

        print("Final scores: ")
        print(f"Player scored {player_points} points and computer scored {computer_points} points")

        if player_points > computer_points:
            print("Player wins!")
        elif player_points==computer_points:
            print("It's a tie!")
        else:
            print("Computer wins!")
