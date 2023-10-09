from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return 0
        while l <= r:
            mid = (l+r) // 2

            if mid == 0 and nums[mid] > nums[mid+1]:
                return mid
            if mid == len(nums) - 1 and nums[mid] > nums[mid-1]:
                return mid
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            if nums[mid] > nums[mid-1] or mid==0:
                l = mid + 1
            else:
                r = mid - 1

        return -1