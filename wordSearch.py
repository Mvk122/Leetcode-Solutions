from typing import List

# Working solution
class Solution:
    def __init__(self):
        self.directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]
    def iterate(self, board, current_row, current_col, word, current_word_index, used_indices):
        if current_word_index == len(word):
            return True
        
        for direction in self.directions:
            new_row, new_col = current_row + direction[0], current_col + direction[1]
            if new_row >= 0 and new_row < len(board) and new_col >= 0 and new_col < len(board[0]) and (new_row, new_col) not in used_indices:
                if board[new_row][new_col] == word[current_word_index]:
                    new_used_indices = used_indices.copy()
                    new_used_indices.add((new_row, new_col))
                    if self.iterate(board, new_row, new_col, word, current_word_index+1, new_used_indices):
                        return True
        return False

        
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row_index, row in enumerate(board):
            for col_index, col in enumerate(row):
                if col == word[0]:
                    used_indices = set()
                    used_indices.add((row_index, col_index))
                    if self.iterate(board, row_index, col_index, word, 1, used_indices):
                        return True
        return False
                



# This solution might not work
def exist(board, word):
    def exist_f(current, word, letter_index, visited, dirs, board):
        visited[current[0]][current[1]] = 1
        if letter_index == len(word) -1:
            return True
        else:
            for d in dirs:
                temp = [current[0] +d[0], current[1] + d[1]]
                if temp[0] < len(board) and temp[1] < len(board[0]) and temp[0] >= 0 and temp[1] >= 0 and visited[temp[0]][temp[1]] != 1 and board[temp[0]][temp[1]] == word[letter_index+1]:
                    visited_t = visited.copy()
                    exist_f(temp, word, letter_index+1, visited_t, dirs, board)
        return False


    starting_points = []
    for row_index, row in enumerate(board):
        for col_index, letter in enumerate(row):
            if word[0] == letter:
                starting_points.append([row_index, col_index])

    dirs = [[1,0], [0, -1], [-1, 0], [0, 1]]
    for point in starting_points:
        visited = [[0 for i in range(len(board[0]))] for x in range(len(board))]
        print('callin')
        if exist_f(point, word, 0, visited, dirs, board):
            return True

    return False

# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],  "ABCCED"))
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))

print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))