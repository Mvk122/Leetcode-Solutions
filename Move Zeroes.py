from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = nums.count(0)
        nums[:] = [e for e in nums if e != 0]
        for i in range(z):
            nums.append(0)