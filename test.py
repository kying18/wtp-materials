import unittest
import copy
import sudoku_buggy as s

VALID_INPUT_BOARD = [
    [3, 9, 0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
    [0, 0, 0,   7, 1, 9,   0, 8, 0],

    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 3,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],

    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   1, 0, 5,   0, 4, 0],
    [1, 0, 9,   0, 0, 0,   2, 0, 0]
]

VALID_BOARD_SOLUTION = [
    [3, 9, 1, 8, 5, 6, 4, 2, 7],
    [8, 6, 7, 2, 3, 4, 9, 1, 5],
    [4, 2, 5, 7, 1, 9, 6, 8, 3],
    [7, 5, 4, 9, 6, 8, 1, 3, 2],
    [2, 1, 6, 4, 7, 3, 5, 9, 8],
    [9, 3, 8, 5, 2, 1, 7, 6, 4],
    [5, 4, 3, 6, 9, 2, 8, 7, 1],
    [6, 7, 2, 1, 8, 5, 3, 4, 9],
    [1, 8, 9, 3, 4, 7, 2, 5, 6]
]

INVALID_INPUT_BOARD = [
    [3, 9, 0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
    [0, 0, 0,   7, 1, 9,   0, 8, 0],

    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 8,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],

    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   1, 0, 5,   0, 5, 0],
    [1, 0, 9,   0, 0, 0,   2, 0, 0]
]


class TestNextEmpty(unittest.TestCase):
    def test_next_empty(self):
        r, c = 1, 2
        example_board = copy.deepcopy(VALID_BOARD_SOLUTION)
        example_board[r][c] = 0
        next_empty = s.find_next_empty(example_board)
        self.assertEqual(next_empty, (r, c), "Should be at (1, 2)")

    def test_next_empty_2(self):
        r, c = 8, 8
        example_board = copy.deepcopy(VALID_BOARD_SOLUTION)
        example_board[r][c] = 0
        next_empty = s.find_next_empty(example_board)
        self.assertEqual(next_empty, (r, c), "Should be at (8, 8)")

    def test_next_empty_no_empty(self):
        example_board = copy.deepcopy(VALID_BOARD_SOLUTION)
        next_empty = s.find_next_empty(example_board)
        self.assertIsNone(next_empty, "Should be no empty spots")


class TestValidGuess(unittest.TestCase):
    def test_is_valid_guess(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)
        self.assertTrue(s.is_valid_guess(example_board, 2, 0, 2), "2 is a valid guess")

    def test_is_valid_guess_2(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)
        self.assertTrue(s.is_valid_guess(example_board, 7, 8, 8), "7 is a valid guess")

    def test_is_not_valid_guess_row(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)
        self.assertFalse(s.is_valid_guess(example_board, 8, 3, 2), "Row already has an 8")

    def test_is_not_valid_guess_col(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)
        self.assertFalse(s.is_valid_guess(example_board, 2, 5, 3), "Col already has a 2")

    def test_is_not_valid_guess_square(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)
        self.assertFalse(s.is_valid_guess(example_board, 4, 3, 6), "3x3 square already has a 4")


class TestSudoku(unittest.TestCase):
    def test_sudoku(self):
        example_board = copy.deepcopy(VALID_INPUT_BOARD)

        self.assertTrue(s.solve_sudoku(example_board), "Should be solvable")
        self.assertEqual(example_board, VALID_BOARD_SOLUTION, "Should return solution")

    def test_sudoku_unsolvable(self):
        example_board = copy.deepcopy(INVALID_INPUT_BOARD)

        self.assertFalse(s.solve_sudoku(example_board), "Should not be solvable")


if __name__ == '__main__':
    unittest.main()

# 0 0 6 0 7 0 4 9 0
# 5 2 0 1 0 0 0 6 8
# 4 0 7 0 2 9 0 0 1
# 0 6 3 0 1 0 0 8 7
# 0 0 0 8 6 0 0 2 0
# 0 5 0 0 0 2 6 4 0
# 0 0 8 0 4 0 0 5 0
# 6 0 2 0 0 1 0 7 4
# 7 4 0 0 8 0 3 0 0
