from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_amount = sum(aliceSizes)
        bob_amount = sum(bobSizes)
        alice_available = set(aliceSizes)

        amount_needed = bob_amount - alice_amount

        for b in bobSizes:
            if b - (amount_needed//2) in alice_available:
                return [b- (amount_needed//2), b]
        return [-1,-1]