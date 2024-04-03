def permute_array(arr):
    def permute_arr_f(current, remainder, result):
        if len(remainder) == 0:
            result.append(current)
        else:
            for i in range(len(remainder)):
                temp = current.copy()
                temp.append(remainder[i])
                permute_arr_f(temp, remainder[:i] + remainder[i+1:], result)

    result = []
    permute_arr_f([], arr, result)
    return result


def permute_array_subsets(arr):
    def permute_arr_subsets_f(current, remainder, result):
        if len(remainder) == 0:
            result.append(current)
        else:
            temp = current.copy()
            temp.append(remainder[0])
            permute_arr_subsets_f(temp, remainder[1:], result)
            permute_arr_subsets_f(current, remainder[1:], result)
    result = []
    permute_arr_subsets_f([], arr, result)
    return result


def partition_array(arr):
    def partition(arr, partitions):
        if not arr:
            print(partitions)
            result.append(partitions)
        else:
            for i in range(1, len(arr) + 1):
                partition(arr[i:], partitions + [arr[:i]])

    result = []
    partition(arr, [])
    return result


def verify_subarray(array):
    for arr in array:
        if max(arr) == arr[-1]:
            return False
    return True

    

def findMaximumBalancedShipments(weight):
    def partition_f(arr, partitions, amount):

        if not arr:
            if verify_subarray(partitions):
                amount[0] = max(len(partitions), amount[0])

        else:
            for i in range(1, len(arr) + 1):
                if max(arr[:i]) == arr[i-1]:
                    continue
                if max(arr[:i]) == arr[-1] and len(arr[:i]) > 1:
                    continue
                print(arr[:i], partitions + [arr[:i]])
                partition_f(arr[i:], partitions + [arr[:i]], amount)

    amount = [0]
    partition_f(weight, [], amount)
    return amount[0]


def findMaximumBalancedShipments2(weight):
    weight.sort()
    dp = [0] * (len(weight) + 1)
    for i in range(1, len(weight) + 1):
        dp[i] = dp[i - 1]
        if weight[i - 1] != weight[i - 2]:
            dp[i] = max(dp[i], 1 + dp[i - 2])
    return dp[-1]

# print(permute_array([1,2,3]))
# print(permute_array_subsets([1,2,3]))
# print(partition_array([1,2,3]))


def max_balanced_shipments(weights):
    n = len(weights)
    dp = [0] * n
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if weights[i] != max(weights[j:i+1]):
                dp[i] = max(dp[i], dp[j] + 1)
    return dp[-1]


from collections import deque 
class Solution:
    def maxSlidingWindow(self, nums, k: int):
        d = deque()
        n = len(nums)
        res = []
        
        for i in range(k):
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
        res.append(nums[d[0]])

        for i in range(k,n):
            if i-d[0] >= k :
                d.popleft()
            while d and nums[d[-1]] <= nums[i]:
                d.pop()
            d.append(i)
            res.append(nums[d[0]])
        return res

# print(findMaximumBalancedShipments2([1, 2, 3, 2, 6, 3]))
# print(findMaximumBalancedShipments([4, 3, 6, 5, 3, 4, 7, 1]))

# print(max_balanced_shipments([4, 3, 6, 5, 3, 4, 7, 1]))


def partition(collection):
    collection_except_last = reversed(collection[:-1])
    only_last = list(collection[-1:])

    # start with the partition for a 1-element collection and then add elements
    partitions = [[only_last]]
    for element in collection_except_last:
        refined_partitions = []
        for partition_ in partitions:
            # insert `element` in each of the subpartition's subsets
            for n, subset in enumerate(partition_):
                refined = partition_[:n] + [[element] + subset] + partition_[n + 1 :]
                refined_partitions.append(refined)
            # put `element` in its own subset
            refined_partitions.append([[element]] + partition_)
        partitions = refined_partitions
    
    count = 0
    for partition_ in partitions:
        if verify_subarray(partition_):
            count == max(count, len(partition_))
    return count

print(partition([4, 3, 6, 5, 3, 4, 7, 1]))