def binary_search(nums, target):
    l = 0 
    r = len(nums) - 1
    while l <= r:
        mid = (l+r) //2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    print(l, r)
    return None

def searchRange(nums, target: int):
    good = binary_search(nums, target)
    if good is None:
        return [-1, -1]
    else:
        l = good
        r = good
        while l-1 >=0 and nums[l-1] == target:
            l -= 1
        while r+1 < len(nums) and nums[r+1] == target:
            r += 1
        return [l,r]
print(binary_search([1,2,3,5], 4))
print(searchRange([2,2], 2))