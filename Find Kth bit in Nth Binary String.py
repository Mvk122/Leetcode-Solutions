class Solution:

    def invert(self, s):
        ret = ""
        for char in reversed(s):
            if char == "0":
                ret = ret + "1"
            else:
                ret = ret + "0"
        return ret
    
    def findKthBit(self, n: int, k: int) -> str:
        current = "0"
        for i in range(n-1):
            current = current + "1" + (self.invert(current))
        return current[k-1]