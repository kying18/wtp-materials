class Board:
    def __init__(self):
        self.current_winner = None
        self.board = [' ' for i in range(9)]

    def print_board(self):
        row1 = self.board[:3]
        row2 = self.board[3:6]
        row3 = self.board[6:]

        for row in [row1, row2, row3]:
            print("| " + " | ".join(row) + " |")

    def draw_move(self, position, letter):
        board_index = position - 1
        self.board[board_index] = letter
        # [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # return True if there is a winner, False if not
    def check_winner(self):
        for letter in ["X", "O"]:
            comparison = [letter for _ in range(3)]

            # check each row
            if self.board[:3] == comparison:  # first row
                return True
            if self.board[3:6] == comparison:  # second row
                return True
            if self.board[6:] == comparison:  # third row
                return True

            # check each column
            if self.board[0:9:3] == comparison:  # first col
                return True
            if self.board[1:9:3] == comparison:  # second col
                return True
            if self.board[2:9:3] == comparison:  # third col
                return True

            # check the 2 diagonals
            if self.board[0:9:4] == comparison:  # left to right diagonal
                return True
            if self.board[2:7:2] == comparison:  # right to left diagonal
                return True

        return False


class Player:
    # what belongs in this class (attributes, methods)?
    def __init__(self, letter):
        self.letter = letter

    def get_move(self):
        # get the move of the player
        # 1-3 is row 1, 4-6 row 2, 7-9 row 3
        move = int(input(f"{self.letter}'s turn. Input a cell (1-9): "))
        return move


def play(board, player1, player2):
    player_counter = 0

    while player_counter < 9 and not board.check_winner():

        # getting the current player
        if player_counter % 2 == 0:
            current_player = player1
        else:
            current_player = player2

        move_position = current_player.get_move()
        board.draw_move(move_position, current_player.letter)
        board.print_board()

        player_counter += 1

    if board.check_winner():
        print(f"{current_player.letter} wins!")
    else:
        print("It's a tie")


b = Board()
b.print_board()
player1 = Player("X")
player2 = Player("O")

play(b, player1, player2)
