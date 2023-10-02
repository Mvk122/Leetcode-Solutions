class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = set()
        while True:
            if n == 1:
                return True
            if n in seen_numbers:
                return False
            seen_numbers.add(n)
            current = 0
            for number in str(n):
                current += int(number) ** 2
            n = current
