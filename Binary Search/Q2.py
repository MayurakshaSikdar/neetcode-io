# https://neetcode.io/problems/search-2d-matrix

# Search a 2D Matrix
# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

# Can you write a solution that runs in O(log(m * n)) time?

# Example 1:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

# Output: true
# Example 2:



# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15

# Output: false
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10000 <= matrix[i][j], target <= 10000

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])
        i, j = 0, row - 1
        k = 0
        while i <= j:
            k = (i+j)//2
            if matrix[k][0] < target:
                i = k+1
            elif matrix[k][0] > target:
                j = k-1
            else:
                return True
        selected_row = (i+j)//2
        i, j = 0, col - 1
        while i <= j:
            k = (i+j)//2
            if matrix[selected_row][k] < target:
                i = k+1
            elif matrix[selected_row][k] > target:
                j = k-1
            else:
                return True
        return False
