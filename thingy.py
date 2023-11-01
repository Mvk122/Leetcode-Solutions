def solution(A):
    # Implement your solution here
    highest = 0
    for i, e in enumerate(A):
        current_set = set(str(e))
        if len(current_set) > 2:
            continue
        current = 0
        for i2, e2 in enumerate(A[i:]):
            element_set = set(str(e2))
            set_union = current_set.union(element_set)
            current_set = set_union
            if len(set_union) <= 2:
                current += 1
            highest = max(highest, current)
    return highest

print(solution([]))