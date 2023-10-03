from typing import List

class Solution:
    def maxAreaSlow(self, height: List[int]) -> int:
        highest = float('-inf')
        for i in range(len(height)):
            for j in range(i, len(height)):
                highest = max(highest, (j-i)*min(height[i], height[j]))
        return highest

    def maxAreaOptimised(self, height: List[int]) -> int:
        highest = 0
        l = 0
        r = len(height) - 1
        while l < r:
            highest = max(highest, (r-l)*min(height[r], height[l]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return highest