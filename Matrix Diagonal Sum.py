from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            total += mat[i][i]
            if len(mat) -i - 1 != i:
                total += mat[i][len(mat)-1-i]
        return total