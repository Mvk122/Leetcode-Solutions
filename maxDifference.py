def maximumDifference(nums):
    min_element = nums[0]
    max_difference = -1
    for element in nums:
        if element <= min_element:
            min_element = element
            continue
        elif element - min_element > max_difference:
            max_difference = element - min_element
    return max_difference
print(maximumDifference([9,4,3,2]))
print(maximumDifference([1,5,2,10]))