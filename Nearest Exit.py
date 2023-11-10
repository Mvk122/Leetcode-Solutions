# BFS Breadth First Search solution
from typing import List
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = [] # 2d matrix of [i, j, steps_to_here]
        queue.append([entrance[0], entrance[1], 0])

        moves = [
            [1,0],
            [0, 1],
            [-1, 0],
            [0, -1]
        ]
        seen_moves = set()

        while queue:
            i, j, steps_to_here = queue.pop(0)
            
            if not (i == entrance[0] and j == entrance[1]):
                if i == 0 or j == 0 or i == len(maze) - 1 or j == len(maze[0]) - 1:
                    return steps_to_here

            for move in moves:
                if (i + move[0], j+move[1]) in seen_moves:
                    continue
                if (i + move[0] >= 0) and (i + move[0] < len(maze)) and (j + move[1] >= 0) and j + move[1] < len(maze[0]) and maze[i+move[0]][j+move[1]] != "+":
                    queue.append([i+move[0], j+move[1], steps_to_here+1])
                    seen_moves.add((i + move[0], j+move[1]))

        return -1