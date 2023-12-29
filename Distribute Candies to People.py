from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ret = [0 for _ in range(num_people)]
        previous_end = 1
        while candies > 0:
            for index, element in enumerate(ret):
                to_give = index+previous_end
                if candies <= to_give:
                    ret[index] += candies
                    return ret
                else:
                    ret[index] += to_give
                    candies -= to_give
            previous_end += num_people

        return ret
