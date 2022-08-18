def productExceptSelf(nums):
    ret = []
    for i in range(len(nums)):
        current = 1
        for element in nums[:i] + nums[i+1:]:
            current *= element
        ret.append(current)
    return ret

def productExceptSelfCheat(nums):
    current = 1
    for num in nums:
        current *= num
    ret = []
    for num in nums:
        ret.append(current//num)
    return ret

print(productExceptSelfCheat([1,2,3,4]))