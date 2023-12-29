from typing import List

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ret = []
        target_ptr = 0

        for i in range(1,n+1):
            if i == target[target_ptr]:
                ret.append("Push")
                target_ptr += 1
            else:
                ret.append("Push")
                ret.append("Pop")
            if target_ptr == len(target):
                return ret
        return ret