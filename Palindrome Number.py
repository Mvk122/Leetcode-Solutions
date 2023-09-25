class Solution:
    def isPalindrome(self, x: int) -> bool:
        as_string = str(x)
        l = 0
        r = len(as_string) - 1

        while l < r:
            if as_string[l] != as_string[r]:
                return False
            l += 1
            r -= 1
        return True