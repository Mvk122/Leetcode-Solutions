from collections import Counter
from typing import List
from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        prev_value = None
        for key, value in c.items():
            if prev_value is None:
                prev_value = value
                continue

            gcd_val = gcd(value, prev_value) 
            if gcd_val == 1:
                return False
            else:
                prev_value = gcd_val
        return prev_value > 1