arr = [[1,2,3], 
       [4,5,6],
       [7,8,9]]

arr2 = [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]

def ld(arr):
    c = 0
    for i in range(3):
        c += arr[i][i]
    return c

def rd(arr):
    c = 0
    for i in range(3):
        c += arr[i][2-i]
    return c

print(rd(arr))