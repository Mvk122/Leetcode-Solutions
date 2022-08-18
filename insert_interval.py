def insert(intervals, newInterval):
    start = False
    start_index = 0
    for index, element in enumerate(intervals):
        if newInterval[0] in range(element[0], element[1]+ 1):
            start = element
            start_index = 0
            break
    if not start:
        intervals.append(newInterval)
        return intervals
    else:
        intervals[start_index][0] = min(start[0], newInterval[0])
