def solution(s):
    red_count = s.count('R')
    # Init indexes to the ends of the string and the result 
    left, right = 0, len(s) - 1
    result = 0
    # moving from the ends to the middle
    while left < right and result <= 10**9:
        # if we meet pair of Rs on the ends
        if s[left] == 'R' and s[right] == 'R':
            # add to the result number of Ws between of these Rs
            red_count -= 2
            result += right - left - 1 - red_count
            # and shrink the processing window
            left += 1
            right -= 1
        # pass all Ws we meet
        elif s[left] != 'R':
            left += 1
        else:
            right -= 1

    if result > 10**9:
        return -1
    return result