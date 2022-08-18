def combination_sum_f(current, candidates, target, results):
    s = sum(current)

    if s > target:
        return False
    elif s == target:
        results.append(current)
        return True
    elif len(candidates) == 0:
        return False
    else:
        temp = current.copy()
        temp.append(candidates[0])
        combination_sum_f(temp, candidates, target, results)
        combination_sum_f(current, candidates[1:], target, results)
    return False

def combination_sum(candidates, target):
    candidates = list(set(candidates))
    result = []
    combination_sum_f([], candidates, target, result)
    return result