from typing import List

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        distinct = set()
        deleted = set()
        while len(deleted) < len(nums):
            min_n = float('inf')
            min_index = -1
            max_n = float('-inf')
            max_index = -1
            for index, num in enumerate(nums):
                if index in deleted:
                    continue
                if num < min_n:
                    min_n = num
                    min_index = index
                if num > max_n:
                    max_n = num
                    max_index = index
            distinct.add(min_n + max_n)
            deleted.add(min_index)
            deleted.add(max_index)
        return len(distinct)