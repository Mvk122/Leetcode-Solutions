from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        for index, num in enumerate(nums):
            change_index = abs(num)-1
            if nums[change_index] < 0:
                answer.append(abs(num))
            nums[change_index] = -nums[change_index]
        return answer 