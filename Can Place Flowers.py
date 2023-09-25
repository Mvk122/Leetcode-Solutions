from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        placed = 0
        for index, element in enumerate(flowerbed):
            if index == 0 and len(flowerbed) > 1:
                if flowerbed[index+1] == 0 and element == 0:
                    flowerbed[index] = 1
                    placed += 1 
            elif index == 0 and len(flowerbed) == 1:
                if element == 0:
                    flowerbed[index] = 1
                    placed += 1
            elif index == len(flowerbed) - 1:
                if flowerbed[index-1] == 0 and element != 1:
                    flowerbed[index] = 1
                    placed += 1
            else:
                if flowerbed[index-1] == 0 and flowerbed[index+1] == 0 and flowerbed[index] == 0:
                    placed += 1
                    flowerbed[index] = 1
        print(flowerbed)
        return placed >= n
