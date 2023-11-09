from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r_index in range(0, len(board), 3):
            for c_index in range(0, len(board[0]), 3):
                seen_elements = set()
                for small_row in range(r_index, r_index+3):
                    for small_col in range(c_index, c_index+3):
                        elem = board[small_row][small_col]
                        if elem in seen_elements:
                            return False
                        if elem != ".":
                            seen_elements.add(board[small_row][small_col])

        for row in board:
            seen_elements = set()
            for col in row:
                if col in seen_elements:
                    return False
                if col != ".":
                    seen_elements.add(col)
                
        for col_index in range(len(board[0])):
            seen_elements = set()
            for row_index in range(len(board)):
                elem = board[row_index][col_index]
                if elem in seen_elements:
                    return False
                if elem != ".":
                    seen_elements.add(elem)
        return True


