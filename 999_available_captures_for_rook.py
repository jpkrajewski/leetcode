# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.

# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.

# Return the number of pawns the white rook is attacking.

 

# Example 1:


# Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

# Output: 3

# Explanation:

# In this example, the rook is attacking all the pawns.

from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

        rook_row = None
        rook_col = None
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_row, rook_col = i, j
                    break

        print(rook_row, rook_col)
        attacked = 0

        def dfs(row, col, s):
            print(row, col)


            nonlocal attacked
            if row > 7 or col > 7 or col < 0 or row < 0 or board[row][col] not in [".", "p", "R"]:
                return
            
            print(board[row][col])

            if board[row][col] == "p":
                attacked += 1
                return 
            
            if s == 0:
                dfs(row - 1, col,s)
            elif s == 1:
                dfs(row + 1, col,s)
            elif s == 2:
                dfs(row, col + 1,s)
            elif s == 3:
                dfs(row, col - 1,s)

        dfs(rook_row, rook_col, 0)
        dfs(rook_row, rook_col, 1)
        dfs(rook_row, rook_col, 2)
        dfs(rook_row, rook_col, 3)
        return attacked
    



board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(Solution().numRookCaptures(board))