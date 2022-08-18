def maximumBeauty_slow(items, queries):
    answers = []
    for query in queries:
        best = 0
        for item in items:
            if item[0] <= query and item[1] > best:
                best = item[1]
        answers.append(best)
    return answers

def maximumBeauty_memoised(items, queries):
    answers = []
    found = {}
    for query in queries:
        if query in found:
            answers.append(found[query])
            continue
        best = 0
        for item in items:
            if item[0] <= query and item[1] > best:
                best = item[1]
        answers.append(best)
        found[query] = best
    return answers


def maximumBeaty_fast(items, queries):
    best_items = {}
    for item in items:
        if item[0] in best_items:
            if best_items[item[0]] < item[1]:
                best_items[item[0]] = item[1]

    return [best_items[query] for query in queries]
        