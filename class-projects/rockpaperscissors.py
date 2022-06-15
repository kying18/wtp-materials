# Steps:

# The first thing we want to implement is a loop that will keep the game running as long as the player wants to continue to play. (Hint: This should be the main foundation for your code, and should encase most of it.)
# Next, we want to ask the first player what move they want to choose. Immediately after we should hide their choice from the screen so that the next player will not be able to see their choice.
# Now ask player 2 what move they want to choose. Once again, make sure that their choice is hidden!
# After both players have inputted their choice, you need to compare both of them and see which player wins. Remember that rock beats scissors, paper beats rock, and scissors beats paper.
# Add a point to the winner and ask the players if they want to play again.
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
    computer_choice = random.choice(['s', 'r', 'p'])

    # TODO: map the choice to the word
    print(f"Player chose {player_choice}, computer chose {computer_choice}")

    # first, see if a draw
    if player_choice == computer_choice:
        print("It's a tie! No one gets a point")

    elif player_choice == "s" and computer_choice == "p":
        print("Player One wins a point!")
        player_points += 1

    elif player_choice == "r" and computer_choice == "s":
        print("Player One wins a point!")
        player_points += 1

    elif player_choice == "p" and computer_choice == "r":
        print("Player One wins a point!")
        player_points += 1

    else:
        print("Player Two wins a point!")
        computer_points += 1

    new_game = input("Do you want to play again? 'y' for yes, 'n' for no")
    if new_game == 'n':
        play = False

        # if false we exit and print final score

        print("Final scores: ")
        print(f"Player scored {player_points} points and computer scored {computer_points} points")

        if player_points > computer_points:
            print("Player wins!")
        else:
            print("Computer wins!")
