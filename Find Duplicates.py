from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []

        for i, e in enumerate(nums):
            store_pos = abs(e-1)
            print(i,e, store_pos)
            if nums[store_pos] < 0:
                ret.append(store_pos)
                nums[store_pos] = -nums[store_pos]
            else:
                nums[store_pos] = -nums[store_pos]

        return ret
    
if __name__ == "__main__":
    s = Solution()
    a = s.findDuplicates([1,1,2])
    print(a)
