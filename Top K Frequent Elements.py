from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        highest_amount = 0
        for key, value in counts.items():
            highest_amount = max(value, highest_amount)
        
        highs = [[] for _ in range(highest_amount)]
        print(highs)

        for key, value in counts.items():
            highs[value-1].append(key)

        k_frequent = []
        for element in reversed(highs):
            if len(k_frequent) >= k:
                return k_frequent[:k+1]
            k_frequent.extend(element)
        return k_frequent