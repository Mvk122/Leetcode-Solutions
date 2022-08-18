def mintTime(machines, goal):
    produced = 0
    days = 0
    while produced < goal:
        days += 1 
        for m in machines:
            if days % m == 0:
                produced += 1
    return days

def minTimeFast(machines, goal):
    day_prod = sum([1/i for i in machines])
    days = goal // day_prod
    produced = sum([days//m for m in machines])
    while produced < goal:
        days += 1 
        for m in machines:
            if days % m == 0:
                produced += 1
    return int(days)


print(minTimeFast([2,3,2],10))