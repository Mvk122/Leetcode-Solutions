from typing import List

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        available_numbers = {}
        for index, num in enumerate(nums):
            if num in available_numbers:
                available_numbers[num].append(index)
            else:
                available_numbers[num] = [index]

        used_pairs = set()
        for idx, num in enumerate(nums):
            req = num + k
            if req in available_numbers:
                if str((req, num)) not in used_pairs and str((num,req)) not in used_pairs:
                    for index in available_numbers[req]:
                        if index != idx:
                            used_pairs.add((req,num))
                            break
        
        return len(used_pairs)