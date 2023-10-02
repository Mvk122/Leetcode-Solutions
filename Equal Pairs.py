from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counter = {}
        for row in grid:
            tup = tuple(row)
            if tup in row_counter:
                row_counter[tup] += 1
            else:
                row_counter[tup] = 1
        
        col_counter = {}
        for i in range(len(grid[0])):
            tup = tuple([grid[x][i] for x in range(len(grid))])
            if tup in col_counter:
                col_counter[tup] += 1
            else:
                col_counter[tup] = 1
        total = 0
        for col in col_counter:
            if col in row_counter:
                total += col_counter[col]* row_counter[col]
        return total