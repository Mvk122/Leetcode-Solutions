def singleNumber(nums):
    s = set()
    for n in nums:
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    return list(s)[0]

def singleNumber2(nums):
    s1 = set()
    s2 = set()
    for n in nums:
        if n in s1:
            s1.remove(n)
            s2.add(n)
        elif n in s2:
            s2.remove(n)
        else:
            s1.add(n)
    return list(s1)[0]

print(singleNumber([4,1,2,1,2]))

print(singleNumber2([0,1,0,1,0,1,99]))