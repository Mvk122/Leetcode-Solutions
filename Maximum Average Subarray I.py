# This solution doesn't work TODO: Fix

from typing import List

def findMaxAverage(nums: List[int], k: int) -> float:
    highest = sum(nums[:k])
    current = highest
    print(highest)

    for end in range(k, len(nums)):
        print(end, nums[end], nums[end-k])
        current += nums[end] - nums[end-k]
        highest = max(highest, current)
    return highest / k

# print(findMaxAverage([0,4,0,3,2], 1))
print(findMaxAverage([4,2,1,3,3], 2))
print(findMaxAverage([1,12,-5,-6,50,3], 4))