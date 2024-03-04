class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check rows
        for row in board:
            if not self.isValidRow(row):
                return False
        
        # Check columns
        for col in range(9):
            column = [board[row][col] for row in range(9)]
            if not self.isValidRow(column):
                return False
        
        # Check 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                sub_box = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
                if not self.isValidRow(sub_box):
                    return False
        
        return True
    
    def isValidRow(self, row):
        seen = set()
        for cell in row:
            if cell != '.':
                if cell in seen:
                    return False
                seen.add(cell)
        return True




# Example usage:
sol = Solution()
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board1))  # Output: True

board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(sol.isValidSudoku(board2))  # Output: False