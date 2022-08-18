def maximum(arr):
    best_sum = -9999999999
    current_sum = 0 
    for x in arr: 
        current_sum = max(x, current_sum + x)
        best_sum = max(current_sum, best_sum)

    return best_sum

print(maximum([-2,1,-3,4,-1,2,1,-5,4]))