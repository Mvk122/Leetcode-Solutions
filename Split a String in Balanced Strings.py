class Solution:
    def balancedStringSplit(self, s: str) -> int:
        current_r = 0
        current_l = 0
        highest = 0
        for index, element in enumerate(s):
            if element == "R":
                current_r += 1
            else:
                current_l += 1
            if current_r == current_l:
                highest += 1
                current_r = 0
                current_l = 0
        return highest