# hotandcold.py
# Name:
# Collaborators:

# This program uses MIT card counting information to tell
# the user when the current deck is hot (it's time to bet
# big!) or cold (leave the table). It gets user input and
# then keeps track of the MIT card counting score so far.
# It should loop and keep asking you for cards until the
# table becomes hot or cold.

# Write some code that keeps track of the current count for
# the cards that the user inputs.
# Your count should start at 0 and either go up 1, down 1,
# or remain the same every time the user inputs a card
# depending on the value of that card as stated in cardcountvalue.py.

# this is a list containing all of the valid values for a card
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# store the count as a variable named count. Fill in the
# value it starts at here.
count =  # TODO

# Your code should loop and print the new count after every
# time the user inputs a new card.

# start a loop here:

# in the loop, ask for user input (use code from pset3)

# in the loop, add the card counting value to the running total count
# use code from pset3 to get the card counting vlaue

# in the loop, add some statements that check if the count
# is >= 5 (hot) or <= -5 (cold). If the count ever gets hot
# or cold, print a message saying the deck is hot/cold and
# exit the loop.

# NOTE: card counting isn't illegal but it IS effective, so
# the casinos don't like to let their players do it! Make
# sure to keep your current count secret (don't print it)
# and only print a message when the deck gets hot or cold.
