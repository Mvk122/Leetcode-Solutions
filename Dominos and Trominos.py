# https://www.youtube.com/watch?v=CecjOo4Zo-g
# DP problem Dynamic Programming
class Solution:
    def __init__(self):
        self.mod = (10**9) + 7
    
    def iterate(self, i, n, t1, t2, dp):
        if i == n:
            return 1
        state = self.make_state(t1, t2)
        if dp[i][state]:
            return dp[i][state]
        
        t3 = i + 1 < n
        t4 = i + 1 < n

        count = 0

        if t1 and t2 and t3:
            count += self.iterate(i+1, n, False, True, dp)
        if t1 and t2 and t4:
            count += self.iterate(i+ 1, n, True, False, dp)
        if t1 and not t2 and t3 and t4:
            count += self.iterate(i+ 1, n, False, False, dp)
        if not t1 and t2 and t3 and t4:
            count += self.iterate(i+ 1, n, False, False, dp)
        if t1 and t2:
            count += self.iterate(i+1, n, True, True, dp)
        if t1 and t2 and t3 and t4:
            count += self.iterate(i+1, n, False, False, dp)
        if t1 and not t2 and t3:
            count += self.iterate(i+1, n, False, True, dp)
        if not t1 and t2 and t4:
            count += self.iterate(i+1, n, True, False, dp)
        if not t1 and not t2:
            count += self.iterate(i+1, n, True, True, dp)
        dp[i][state] = count % self.mod
        return count % self.mod


        
    def make_state(self, t1, t2):
        if not t1 and t2:
            return 0
        elif t1 and not t2:
            return 1
        elif t1 and t2:
            return 2
        else:
            return 3

    def numTilings(self, n: int) -> int:
        dp = [[None for _ in range(4)] for i in range(n+1)]
        return self.iterate(0, n, True, True, dp)


            