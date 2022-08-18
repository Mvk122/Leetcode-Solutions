def uniquePaths(m, n):
    if m==1 or n==1:
        return 1
    else:
        return uniquePaths(m-1, n) + uniquePaths(m, n-1)

def uniquePathsDP(m, n):
    def uniquePathsDP_f(m,n, dp):
        if m == 1 or n == 1:
            return 1
        else:
            if dp[m][n] != 0:
                return dp[m][n]
            else:
                temp = uniquePathsDP_f(m-1, n, dp) + uniquePathsDP_f(m, n-1, dp)
                dp[m][n] = temp 
                return temp
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    return uniquePathsDP_f(m,n, dp)


print(uniquePathsDP(3,7))