# https://neetcode.io/problems/valid-sudoku

# Valid Sudoku
# You are given a 9 x 9 Sudoku board board. A Sudoku board is valid if the following rules are followed:

# Each row must contain the digits 1-9 without duplicates.
# Each column must contain the digits 1-9 without duplicates.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without duplicates.
# Return true if the Sudoku board is valid, otherwise return false

# Note: A board does not need to be full or be solvable to be valid.

# Example 1:



# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true
# Example 2:

# Input: board = 
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: false
# Explanation: There are two 1's in the top-left 3x3 sub-box.

# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in square[(r//3, c//3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True
