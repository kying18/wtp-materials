from numpy import iinfo


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[c][r] == -1:  # should be 0 not -1
                return r, c

    return None, None


def is_valid_guess(puzzle, guess, row, col):
    # function where given a puzzle and a number that we guess for a given row/col, returns True if the guess
    # is valid (ie fulfills all the rules of sudoku) otherwise returns False
    valid = False

    # should be for c in puzzle[row]
    for col in puzzle[row]:
        if guess not in col:
            valid = True  # This should just be setting the boolean for false, should not set to true
        else:
            valid = False

    # should be for r in selected_col, where selected_col = [puzzle[i][col] for i in range(9)]
    for row in puzzle[col]:
        if guess not in row:
            valid = True
        else:
            valid = False

    # This whole section is a lil fucked lol
    # row_start should be above the break
    # col_start should have its own loop if we doing it this way
    # > should be >=
    row_start = 0
    col_start = 0
    for i in range(3):
        if i*3 > row:
            col_start = i
            break
            row_start = i

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                valid = False

    # if pass all the tests, then we need to set valid to True
    # should recognize that we should just return True instead of having this boolean

    return valid


def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return True/False as to whether it is solved, should mutate puzzle to produce solution

    empty = find_next_empty(puzzle)

    if empty[0] is None:
        return True

    for guess in range(9):  # should be in range(1, 10)
        if is_valid_guess(puzzle, guess, empty[1], empty[0]):  # row and col flipped
            puzzle[empty[0]][empty[1]] = guess

            if solve_sudoku(puzzle):
                return True

        puzzle[empty[1]][empty[0]] = 0  # row and col flipped

    return False
