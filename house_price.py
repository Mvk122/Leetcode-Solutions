dp = {}

def check(arr):
    n = int((2 * len(arr)) ** 0.5)
    dp = [0] * len(arr)

    dp[0] = arr[0]

    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i * (i + 1) // 2] = dp[(i - 1) * i // 2] + arr[i * (i + 1) // 2]
            elif i == j:
                dp[i * (i + 1) // 2 + j] = dp[(i - 1) * i // 2 + j - 1] + arr[i * (i + 1) // 2 + j]
            else:
                dp[i * (i + 1) // 2 + j] = max(dp[(i - 1) * i // 2 + j - 1], dp[(i - 1) * i // 2 + j]) + arr[i * (i + 1) // 2 + j]

    return max(dp[(n - 1) * n // 2 : n * (n + 1) // 2])

def solve(arr):
    ans = check(arr)
    return ans

if __name__ == "__main__":
    print(solve([1, 3, -1, 3, 1, 5]))