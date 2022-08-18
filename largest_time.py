def largestTimeFromDigits(arr):
    """
    :type arr: List[int]
    :rtype: str
    """
    def get_largest_valid(arr, max_num, taken):
        max = -1
        max_index = -1
        for index, element in enumerate(arr):
            if element > max and element <= max_num and not taken[index]:
                max_index = index
                max = element
        taken[max_index] = True
        return max

    time = ""
    maxes = [2,3,5,10]
    taken = [False] * 4
    for index, max in enumerate(maxes):
        if index == 1 and time[0] != "2":
            num = get_largest_valid(arr, 10, taken)
        else:
            num = get_largest_valid(arr, max, taken)
            print(num)
        if num == -1:
            print(time)
            return ""
        else:
            time += str(num)

    return time[:2] + ':' + time[2:]

print(largestTimeFromDigits([2,0,6,6]))