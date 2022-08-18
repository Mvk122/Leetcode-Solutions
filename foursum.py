def fourSum_f(current, nums, target, result):
    if sum(current) == target and len(current) == 4:
        result.append(current)
        return True
    elif len(current) == 4:
        return False
    elif len(nums) == 0:
        return False
    else:
        temp = current.copy()
        temp.append(nums[0])
        fourSum_f(temp, nums[1:], target, result)
        fourSum_f(current, nums[1:], target, result)
    return False

#This solution is too slow >:(
def fourSum(nums, target: int):
    result = []
    fourSum_f([], nums, target, result)
    for r in result:
        r.sort()
    return [list(item) for item in set(tuple(row) for row in result)]

print(fourSum([1,0,-1,0,-2,2], 0))
print(fourSum([2,2,2,2,2], 8))