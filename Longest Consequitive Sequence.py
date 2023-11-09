from typing import List

"""
From [100,4,200,1,3,2], the consequitive subsequences are:
[1,2,3,4], [100], 200

Intuition:
    Looping over the numbers, if number - 1 doesn't exist in the set of numbers, this is the start of a sequence.
    We can then iterate over number + 1, number + 2... to see how long the sequence is, stopping when number + n doesn't exist in the set.     
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        highest = 0
        for num in nums:
            if num-1 in nums_set:
                continue
            current_increment = 1
            while num + current_increment in nums_set:
                current_increment += 1
            highest = max(highest, current_increment)
        return highest