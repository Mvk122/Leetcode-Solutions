def mySqrt(x):
    l = 0 
    r = x
    if x == 1:
        return 1
    while True:
        if l == r-1:
            return l
        elif l == r:
            return l
        else:
            res = ((l + r) // 2)
            squared = res ** 2
            if squared > x:
                r = res
            elif squared == x:
                return res
            else:
                l = res

print(mySqrt(9))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(16))
print(mySqrt(2))
            