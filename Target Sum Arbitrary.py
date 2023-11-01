from collections import Counter
from typing import List

class Solution:
    def permute(self, current: List[int], current_total: int, target: int, available: List[int], result, seen_counters):
        if current_total == target:
            c = Counter(current)
            for counter in seen_counters:
                print(counter)
                if counter == c:
                    return
            result.append(current)
            seen_counters.append(c)
        else:
            for element in available:
                if element + current_total <= target:
                    temp = current.copy()
                    temp.append(element)
                    self.permute(temp, current_total+element, target, available, result, seen_counters)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        seen_counters = []
        self.permute([], 0, target, candidates, result, seen_counters)
        return result
    
if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7], 7))