# Set Matrix Zeroes
from typing import List


class Solution:
    def setZeroes(self, m: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_flag = False
        col_flag = False

        # row and col flag to True if m[0][j] and m[i][0]
        # first row/col to 0 if m[i][j] = 0
        for i in range(len(m)):
            for j in range(len(m[0])):
                if i == 0 and m[i][j] == 0:
                    row_flag = True

                if j == 0 and m[i][j] == 0:
                    col_flag = True

                if m[i][j] == 0:
                    m[0][j] = 0
                    m[i][0] = 0

        # if 0 in first row and col then m[i][j] = 0
        for i in range(1, len(m)):
            for j in range(1, len(m[0])):
                if m[0][j] == 0 or m[i][0] == 0:
                    m[i][j] = 0

        # If True set first row to 0
        if row_flag:
            for j in range(len(m[0])):
                m[0][j] = 0

        # If True set first col to 0
        if col_flag:
            for i in range(len(m)):
                m[i][0] = 0

    def print_matrix(self, mat):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                print(mat[i][j], end=" ")

            print()


s = Solution()

matrix = [[0, 1, 2, 0],
          [3, 4, 5, 2],
          [1, 3, 1, 5]]

s.setZeroes(matrix)
s.print_matrix(matrix)
