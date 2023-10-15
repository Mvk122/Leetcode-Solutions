from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        if k == 0:
            return sum(reward2)
        differential_array = [reward1[n] - reward2[n] for n in range(len(reward1))]
        largest_indices = set(sorted(range(len(differential_array)), key = lambda sub: differential_array[sub])[-k:])
        
        total = 0
        for index, element in enumerate(reward1):
            if index in largest_indices:
                total += element
            else:
                total += reward2[index]
        return total