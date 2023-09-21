from typing import List

def maxSubArray(nums: List[int]) -> int:
    best_sum = nums[0]
    current_sum = nums[0]

    for index, element in enumerate(nums[1:]):
        current_sum = max(current_sum + element, element)
        best_sum = max(current_sum, best_sum)
    return best_sum