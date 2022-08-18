def twoSum(numbers, target):
    start_pointer = 0
    end_pointer = len(numbers) -1
    while True:
        if target-numbers[start_pointer] == numbers[end_pointer]:
            return [start_pointer+1, end_pointer+1]
        elif target-numbers[start_pointer] > numbers[end_pointer]:
            start_pointer += 1
        else:
            end_pointer -= 1


print(twoSum([2,7,11,15], 9))