from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)  
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res

# This is not a working solution
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
