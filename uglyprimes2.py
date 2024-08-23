from heapq import heappop, heappush

def nthUglyNumber(n: int) -> int:
    primes = [2,3,5]
    nums = [1]
    visited = {1}

    for _ in range(n):
        smallest = heappop(nums)
        for prime in primes:
            if smallest * prime not in visited:
                heappush(nums, smallest * prime)
                visited.add(smallest * prime)


    return nums[-1]

print(nthUglyNumber(10))