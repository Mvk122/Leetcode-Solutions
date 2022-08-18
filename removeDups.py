def removeDuplicates(nums) -> int:
    current = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        if nums[i] == current:
            nums.pop(i)
        else:
            current = nums[i]
    return nums

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))