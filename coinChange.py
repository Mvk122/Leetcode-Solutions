#Greedy algorithm, not exhaustive
def coinChange(coins, amount):
    coins.sort(reverse=True)
    smallest = coins[-1]
    current = amount
    total = 0
    while current > 0:
        if current < smallest:
            return -1
        else:
            for c in coins:
                if c <= current:
                    current -= c
                    total += 1
                    break

    return total

#Recursive algorithm, too slow
def coinChangeRecursive(coins, amount):
    def coinChange_f(coins, current, total, bet):
        if total > bet[0]:
            return
        if current == 0:
            bet[0] = min(total, bet[0])
        elif current < min(coins):
            return
        else:
            for c in coins:
                coinChange_f(coins, current-c, total+1, bet)
        return total

    bet = [float('inf')]
    coinChange_f(coins, amount, 0, bet)
    if bet[0] == float('inf'):
        return -1
    else:
        return bet[0]

def coinChangeDP(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for a in range(1, amount+1):
        for c in coins:
            dp[a] = min(dp[a], 1+ dp[a-c])

    return dp[amount] if dp[amount] != amount +1 else -1


print(coinChangeDP([1,2,5], 11))
print(coinChangeDP([2,], 3))



# print(coinChange([1,2,5], 11))
# print(coinChange([2], 3))
# print(coinChange([1], 0))
