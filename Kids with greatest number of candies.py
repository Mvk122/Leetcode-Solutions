from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    highest = max(candies)
    return [element + extraCandies >= highest for element in candies]