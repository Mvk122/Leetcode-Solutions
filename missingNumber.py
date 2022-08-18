def missingNumber(nums):
    m = [False] * (len(nums) + 1)
    for n in nums:
        m[n] = True 
    for index, l in enumerate(m):
        if l is False:
            return index

print(missingNumber([3,0,1]))