def moveZeroes(nums):
    count = 0
    for i in range(len(nums)-1, -1, -1):
        if nums[i] == 0:
            nums.pop(i)
            count += 1
    nums.extend([0] * count)
    