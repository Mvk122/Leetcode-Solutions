def find_element(target, elements):
    l = 0 
    r = len(elements) -1
    while l <= r:
        mid = (l + r) // 2
        if elements[mid] == target:
            return mid
        elif elements[mid] < target:
            l = mid + 1 
        else:
            r = mid - 1
    print(l, r)
    return -1
    

elements = [-1,0,4,5,12]
target = 3
print(find_element(target, elements))

