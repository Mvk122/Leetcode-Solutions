def maximum_path(node_values):
    n = len(node_values)
    dp = [0] * n
    dp[0] = node_values[0]

    queue = [0]  # Start with the root node

    while queue:
        i = queue.pop(0)  # Get the current node

        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            dp[left] = max(dp[left], dp[i] + node_values[left])
            queue.append(left)
        if right < n:
            dp[right] = max(dp[right], dp[i] + node_values[right])
            queue.append(right)

    return max(dp)

if __name__ == "__main__":
    print(maximum_path([1, 3, -1, 3, 1, 5])) 