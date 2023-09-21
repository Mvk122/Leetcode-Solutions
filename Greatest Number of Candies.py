from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highest = max(candies)
        return [(kid + extraCandies >= highest) for kid in candies]