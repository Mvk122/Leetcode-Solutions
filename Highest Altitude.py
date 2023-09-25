from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        highest = 0
        for element in gain:
            current += element
            highest = max(current, highest)
        return highest