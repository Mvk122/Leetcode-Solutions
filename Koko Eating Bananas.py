from math import ceil
from typing import List

class Solution:
    def check(self, piles, k) -> int:
        hours = 0
        for i in range(len(piles)):
            hours += ceil(piles[i] / k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2
            hours = self.check(piles, mid)
            if hours > h:
                l = mid + 1
            else:
                r = mid - 1
        return l