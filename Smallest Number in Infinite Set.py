class SmallestInfiniteSet:

    def __init__(self):
        self.smaller_than_current = set()
        self.current_numbers = 1

    def popSmallest(self) -> int:
        if self.smaller_than_current:
            ans = min(self.smaller_than_current)
            self.smaller_than_current.remove(ans)
            return ans
        else:
            self.current_numbers += 1
            return self.current_numbers - 1
        

    def addBack(self, num: int) -> None:
        if num < self.current_numbers:
            self.smaller_than_current.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)