def guess(n):
    final = 6 
    if n == final:
        return 0
    if n > final:
        return -1
    return 1

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        higher = n
        while True:
            current = (lower + higher) // 2
            g = guess(current)
            if g == 0:
                return current
            elif g == -1:
                higher = current - 1
            elif g == 1:
                lower = current + 1
        return -1

s = Solution()
s.guessNumber(10)