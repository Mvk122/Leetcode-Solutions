def triplets(a,b,c):
    solutions = []
    for x in b:
        for y in a:
            if y > x:
                continue
            for z in c:
                if z > x:
                    continue
                solutions.append([x,y,z])

    unique_data = [list(x) for x in set(tuple(x) for x in solutions)]

    return len(unique_data)

def smallest(arr, target):
    start = 0 
    end = len(arr) -1
    if target > arr[end]:
        return end

    ans = -1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid -1
        else:
            ans = mid
            start = mid + 1
    return ans 

def triplets_fast(a,b,c):
    b = list(set(b))
    b.sort()
    a = list(set(a))
    c = list(set(c))
    a.sort()
    c.sort()
    ans = 0
    for anchor in reversed(b):
        small_a = smallest(a, anchor)
        if small_a == -1:
            continue
        small_c = smallest(c, anchor)
        if small_c == -1:
            continue
        ans += (small_c+1) * (small_a+1)
    return ans

print(triplets_fast([1,3,5],[2,3],[1,2,3]))
                