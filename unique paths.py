# 2D Dynamic Programming
class Solution:
    def iterate(self, m, n, dp):
        if dp[m][n]:
            return dp[m][n]
        if m == 0 and n == 0:
            return 1

        count = 0
        if m-1 >=0:
            count += self.iterate(m-1, n, dp)
        if n-1 >=0:
            count += self.iterate(m, n-1, dp)

        dp[m][n] = count
        return count        


    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[None for i in range(n)] for j in range(m)]
        return self.iterate(m-1, n-1, dp)