from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        for index, element in enumerate(flowerbed):
            right_invalid, left_invalid = None, None
            if element == 1:
                continue
            if index + 1 == len(flowerbed):
                right_invalid = False
            else:
                right_invalid = flowerbed[index+1] == 1
            if index > 0:
                left_invalid = flowerbed[index-1] == 1
            else:
                left_invalid = False

            if right_invalid or left_invalid:
                continue
            else:
                flowerbed[index] = 1
                placed += 1
        return placed >= n
