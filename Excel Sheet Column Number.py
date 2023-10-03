class Solution:   
    def titleToNumber(self, columnTitle: str) -> int:
        total = 0
        for i, e in enumerate(reversed(columnTitle)):
            total += (26 **i) * (ord(e) - 64)
        return total