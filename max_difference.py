def maxDifference(px):
    lowest = px[0]
    greatest_difference = -1
    for element in px:
        if element > lowest:
            if element - lowest > greatest_difference:
                greatest_difference = element - lowest
        elif element < lowest:
            lowest = element
                
    return greatest_difference

print(maxDifference([7,5,3,1]))
print(maxDifference([2,3,10,2,4,8,1]))
print(maxDifference([7,9,5,6,3,2]))