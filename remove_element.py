

def removeElement(nums, val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
            i += -1
        i+=1 
    return nums

print(removeElement([3,2,2,3],3))
print(removeElement([0,1,2,2,3,0,4,2],2))