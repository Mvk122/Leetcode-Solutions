from typing import List

class Solution:
    def __init__(self):
        self.directions = [
            [1,0], [-1, 0], [0, 1], [0,-1]
        ]

    def rot_here(self, r_i, c_i, grid, changed_this_round):
        for direction in self.directions:
            coord_r = direction[0] + r_i
            coord_c = direction[1] + c_i
            if coord_r < 0 or coord_r > len(grid) -1:
                continue
            if coord_c < 0 or coord_c > len(grid[0]) -1:
                continue
            
            if grid[coord_r][coord_c] == 1 and (coord_r, coord_c) not in changed_this_round:
                grid[coord_r][coord_c] = 2
                changed_this_round.add((coord_r,coord_c))

    def orangesRotting(self, grid: List[List[int]]) -> int:
        changed_this_round = set((-1,-1))
        current_round = -1

        while len(changed_this_round) > 0:
            changed_this_round = set()
            for r_i, row in enumerate(grid):
                for c_i, element in enumerate(row):
                    if element == 2 and (r_i, c_i) not in changed_this_round:
                        self.rot_here(r_i, c_i, grid, changed_this_round)
            current_round += 1

        for row in grid:
            for element in row:
                if element == 1:
                    return -1
        return current_round
            