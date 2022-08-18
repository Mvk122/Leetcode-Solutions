def jump(nums):
    def jump_f(current_index, nums):
        if nums[current_index] + current_index >= len(nums) -1:
            return True
        else:
            for i in range(1, nums[current_index]+1):
                if i + current_index < len(nums) and i != 0:
                    return jump_f(i+current_index, nums)
        return False
    return jump_f(0, nums)

print(jump([2,3,1,1,4]))
print(jump([3,2,1,0,4]))
print(jump([1]))
print(jump([1,2,3]))