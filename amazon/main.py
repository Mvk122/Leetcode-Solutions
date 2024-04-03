def maxBalancedShipments(weights):
    n = len(weights)
    weights.sort()
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, i+1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            elif weights[i-1] == j:
                dp[i][j] = max(dp[i-1][j], 1 + dp[i-1][j-1])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][weights[i-1]] + 1)
    return max(dp[-1])

def maxBalancedShipments2(weights):
    weights.sort()
    max_shipments = 0
    max_weight = weights[-1]
    for weight in reversed(weights):
        if weight < max_weight:
            max_shipments += 1
            max_weight = weight
    return max_shipments

print(maxBalancedShipments2([1,2,3,2,6,3]))