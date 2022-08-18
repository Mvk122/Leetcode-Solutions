def kClosest(points, k: int):
    points.sort(key = lambda x: abs((x[0]**2) + (x[1]**2)))
    print(points)
    return points[:k]

print(kClosest([[1,3],[-2,2]], 1))