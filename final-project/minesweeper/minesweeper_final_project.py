# minesweeper_template.py
# Name:
# Collaborators:

# add any imports here

# global variables to-do: See Part 3


'''
The Cell class holds information about a single cell in the board.
'''
# Cell to-do:
# Part 1: 
#   [ ] __init__
#   [ ] getter method
#   [ ] setter method
#   [ ] to_string()

class Cell:
    def __init__(self):
        pass

'''
The Board class holds information about the game board, 
and updates the board's state as the game progresses.
'''
# Board to-do:
# Part 1: 
#   [ ] __init__
#   [ ] pretty_print()
#   [ ] is_in_bounds()
#   [ ] add_random_bombs()
#   [ ] click_on().
# Part 2:
#   [ ] add_random_bombs()
#   [ ] click_on()
#   [ ] search_and_reveal()
#   [ ] nearby_bomb_count()
#   [ ] won_game().

class Board:
    def __init__(self):
        pass
    
    def pretty_print():
        pass
    
    def is_in_bounds(self, row, column):
        # Fill in here
        pass

    def add_random_bombs(self, num_bombs, except_row, except_col):
        # place num_bombs bombs on the board in random places
        # except for on the cell at except_row,  except_col
        pass
    
    def click_on(self, row, col):
        # Fill in
        if self.is_in_bounds(row, col):
            self.board_array[row][col].uncover()
        else:
            print('Error: Inputted row/column not in bounds.')
    
    def search_and_reveal(self, row, col):
        # First, count the number of nearby bombs to (row, col)
        # Next, set the cell's nearby bomb count to reflect the number of bombs
        # Now uncover the cell
        #if # there are no adjacent bombs (i.e. nearby bomb count is 0),
            # reveal all the *neighboring* cells
            # search around *those* cells too
        pass
    
    def won_game(self):
        pass
    
    def nearby_bomb_count(self, row, col):
        #First calculate the number of nearby bombs
        pass


'''
The MinesweeperGame class runs each round of the game.
'''
# MinesweeperGame to-do:
# Part 3: 
#   [ ] __init__()
#   [ ] play_game()
#   [ ] input_helper()
#   [ ] ask_for_input().


class MinesweeperGame:
    def __init__(self, num_rows, num_columns, num_bombs):
        pass
    
    def play_game(self):
        pass
'''
Begin here! Test for the entire game
Uncomment the ROWS, COLUMNS, NUM_BOMBS lines and the two lines under # # play!
'''
# user settings
# ROWS = 5 
# COLUMNS = 7
# NUM_BOMBS = 10
# # play!
# minesweeper = MinesweeperGame(ROWS, COLUMNS, NUM_BOMBS)
# minesweeper.play_game()












# Testing and Part Checklists Below!

# ================================================================== #
#                               Part 1                               #
# ================================================================== #

# Part 1 Checklist:
# Cell: implement __init__(), getter method, setter method, and to_string().
# Board: implement __init__(), pretty_print(), is_in_bounds(), add_random_bombs(), and click_on().
# MinesweeperGame: None



# Testing for Cell class

test_cell = Cell()
test_cell.set_num_nearby_bombs(30)
print(test_cell.to_string()) # should output -

test_cell.uncover()
print(test_cell.to_string()) # should output 30

# Testing for Board class (Part 1) - uncomment the pairs of lines of code! 

# test_board = Board(5, 5)
# test_board.pretty_print()

#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 

# test_board.add_random_bombs(4, 0, 0)
# test_board.pretty_print() # should still have everything covered

#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 

# for r in range (5):
#    for c in range(5):
#        test_board.click_on(r, c)

# test_board.pretty_print() # should count four B's

#| 0 | 0 | 0 | 0 | B | # your board may look different because of random placement
#| B | 0 | 0 | 0 | 0 | 
#| 0 | 0 | 0 | B | 0 | 
#| 0 | 0 | 0 | B | 0 | 
#| 0 | 0 | 0 | 0 | 0 | 

# ================================================================== #
#                               Part 2                               #
# ================================================================== #

# Part 2 Checklist:
# Global Variables
# Cell: None
# Board: click_on(), won_game(), search_and_reveal(), add_random_bombs(), nearby_bomb_count().
# MinesweeperGame: None


# Testing for Board class (Part 2) - uncomment the pairs of lines of code and the print(game_state) methods to run!

# game_state = test_board.click_on(0, 0) 
# test_board.pretty_print()


#| 0 | 1 | - | - | - | 
#| 2 | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - | 
#| - | - | - | - | - |  

# print(game_state) # prints 2 (i.e. IN_PLAY)

# game_state = test_board.click_on(3, 4)
# test_board.pretty_print()

#| 0 | 1 | - | 1 | 0 | 
#| 2 | - | - | 1 | 0 | 
#| - | - | - | 1 | 0 | 
#| 2 | 2 | 1 | 0 | 0 | 
#| 0 | 0 | 0 | 0 | 0 | 

# print(game_state) # prints 2 (i.e. IN_PLAY)


# ================================================================== #
#                               Part 3                               #
# ================================================================== #

# Part 3 Checklist:
# Cell: None
# Board: None
# MinesweeperGame: __init__(), ask_for_input(), play_game()



# ================================================================== #
#                          Part 4 (optional)                         #
# ================================================================== #

# Part 4 Checklist:
# MinesweeperGame: graphical_input_helper(), ask_for_graphical_input()
# Graphics.py: import, make window, print board, win/lose message, etc 
