def most_water_slow(array):
    max_water = 0
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            water_height = min(array[i], array[j]) * abs(j-i)
            if water_height > max_water:
                max_water = water_height

    return max_water

def most_water(array):
    max_area = 0
    l = 0
    r = len(array) - 1
    while l < r:
        area = min(array[l], array[r]) * (r-l)
        if area > max_area:
            max_area = area
        
        if array[l] < array[r]:
            l += 1
        else:
            r -= 1 
            
    return max_area


print(most_water_slow([1,8,6,2,5,4,8,3,7]))