from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        
        if len(cost) <= 2:
            return min(first, second)

        for i in range(2, len(cost)):
            current = cost[i] + min(first, second)
            first = second
            second = current
        return min(first, second)
        