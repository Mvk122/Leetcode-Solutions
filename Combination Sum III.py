from typing import List

class Solution:
    def permute(self, current, current_val, k, n, result):
        if current_val == n and len(current) == k:
            result.append(current)
        elif k - len(current) == 0:
            pass
        elif k - len(current) == 1:
            required = n - current_val
            if required in range(1,10) and required not in current:
                temp = current.copy()
                temp.add(required)
                result.append(temp)
        else:
            lowest = (n-current_val) // (k-len(current))
            for i in range(max(lowest,1), 10):
                if i not in current and current_val + i < n:
                    temp = current.copy()
                    temp.add(i)
                    self.permute(temp, current_val+i, k, n, result)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.permute(set(), 0, k, n, result)
        return [set(item) for item in set(frozenset(item) for item in result)]