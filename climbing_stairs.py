stored_dict = {}
def climbStairs(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        if n in stored_dict:
            return stored_dict[n]
        else:
            res = climbStairs(n-1) + climbStairs(n-2)
            stored_dict[n] = res
            return res

print(climbStairs(38))
