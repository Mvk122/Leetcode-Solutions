from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counts = Counter(nums)
        operations = 0
        seen = set()
        for key in counts:
            if key in seen:
                continue

            if k - key == key:
                operations += counts[key] // 2
                seen.add(key)
            elif k - key in counts:
                operations += min(counts[key], counts[k-key])
                seen.add(key)
                seen.add(k-key)
        return operations