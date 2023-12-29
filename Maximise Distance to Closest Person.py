from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        left_closest = []
        right_closest = []

        for index, element in enumerate(seats):
            if index == 0:
                left_closest.append(0 if seats[index] else float('inf'))
            else:
                left_closest.append(0 if seats[index] else left_closest[index-1]+1)

        for index, element in enumerate(reversed(seats)):
            if index == 0:
                right_closest.append(0 if element else float('inf'))
            else:
                right_closest.append(0 if element else right_closest[index-1]+1)

        right_closest = reversed(right_closest)

        res = 0
        for left, right in zip(left_closest, right_closest):
            res = max(res, min(left, right))
        return res