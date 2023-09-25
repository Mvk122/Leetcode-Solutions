from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        highest = sum(nums[:k])
        current = highest

        for end in range(k, len(nums)):
            current += nums[end] - nums[end-k]
            highest = max(highest, current)
        return highest / k