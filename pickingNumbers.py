def pickingNumbers(a):
    max = 1
    for i in range(len(a)):
        pointer_1 = i 
        pointer_2 = i +1
        lower_max = 0
        higher_max = 0 
        while pointer_2 < len(a):
            res = a[pointer_2] - a[pointer_1]
            if res == 1:
                higher_max += 1
            elif res == 0:
                higher_max += 1 
                lower_max += 1 
            elif res == -1:
                lower_max += 1
            pointer_2 += 1
        if lower_max > max:
            max = lower_max
        elif higher_max > max:
            max = higher_max

    return max +1

print(pickingNumbers([1,1,2,2,4,4,5,5,5]))
print(pickingNumbers([4,6,5,3,3,1]))
print(pickingNumbers([1,2,2,3,1,2]))