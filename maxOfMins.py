import heapq

def min_sum_of_largest(trails, record):
    # Initialize a priority queue with n zeros
    heap = [0] * record
    heapq.heapify(heap)

    # Sort the list in descending order
    trails.sort(reverse=True)

    # For each number, add it to the subgroup with the smallest sum
    for num in trails:
        smallest_sum = heapq.heappop(heap)
        heapq.heappush(heap, smallest_sum + num)

    # The sum of the largest value in each subgroup is the sum of the heap
    return sum(heap)

def efficientTrek(trails, record):
    n = len(trails)
    dp = [[0 for _ in range(n+1)] for _ in range(record+1)]
    
    for i in range(n - 1, -1, -1):
        dp[1][i] = max(dp[1][i + 1], trails[i])
        
    for p in range(1, record + 1):
        i = n - p
        dp[p][i] = trails[i] + dp[p - 1][i + 1]
        
    for p in range(2, record + 1):
        for i in range(record - p, n - p + 1):
            max_val = trails[i]
            result = max_val + dp[p - 1][i + 1]
            for j in range(i + 2, n - p + 1):
                max_val = max(max_val, trails[j - 1])
                if p > 2:
                    result = min(result, max_val + trails[j] + dp[p - 2][j + 1])
            j = n - p + 1
            dp[p][i] = min(result, max(max_val, trails[j - 1]) + dp[p - 1][j])
            
    return dp[record][0]