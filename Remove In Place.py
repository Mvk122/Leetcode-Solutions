from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        free_positions = []
        removed = 0
        for index, element in enumerate(nums):
            if element == val:
                removed += 1
                free_positions.append(index)
            elif len(free_positions) > 0:
                nums[free_positions[0]] = element
                free_positions.pop(0)
                free_positions.append(index)
        return removed
    
if __name__ == "__main__":
    s = Solution()
    a = [0,1,2,2,3,0,4,2]
    print(s.removeElement(a, 2))
    print(a)