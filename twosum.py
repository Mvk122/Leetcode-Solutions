import collections
def twoSum(nums, target):
    d = {}
    for index, element in enumerate(nums):
        if target - element in d.keys():
            return [index, d[target-element]]
        d[element] = index

def threeSum(nums, target=0):
    d = {}
    def isValid(s_index, tuple, solutions_numbers):
        tup = tuple + (s_index,)
        s = {nums[t] for t in tup}
        for solution in solutions_numbers:
            if s == solution:
                return False
        return len(set(tup)) == 3
    solutions = []
    solutions_numbers = []
    for f_index, f_element in enumerate(nums):
        for s_index, s_element in enumerate(nums):
            if target-s_element in d.keys() and isValid(s_index, d[target-s_element], solutions_numbers):
                solutions.append(d[target-s_element] + (s_index,))
                x, y = d[target-s_element]
                solutions_numbers.append(set([nums[x], nums[y], s_element]))
            d[f_element+s_element] = (f_index, s_index)

    solution_arr = []
    for s in solutions:
        x, y, z = s
        solution_arr.append([nums[x], nums[y], nums[z]])
    return solution_arr

def threeSumFast(nums, target=0):
    nums.sort()
    solutions = []
    for i in range(len(nums)):
        j = i + 1
        k = len(nums)-1
        while j < k:
            if nums[i] + nums[j] + nums[k] == target:
                solutions.append([nums[i], nums[j], nums[k]])
                while j < k and nums[j] == nums[j+1]:
                    j += 1
                j += 1 
            elif nums[i] + nums[j] + nums[k] < target:
                j += 1
            else:
                k -= 1 
    unique_data = [list(x) for x in set(tuple(x) for x in solutions)]

    return unique_data

#print(twoSum([2,7,11,15], 9))
print(threeSumFast([-1,0,1,2,-1,-4]))
print(threeSumFast([0,0,0]))