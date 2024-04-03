from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, e in enumerate(nums):
            neg_index = abs(e)-1
            if nums[neg_index] < 1:
                return abs(e)
            nums[neg_index] = -nums[neg_index]
        