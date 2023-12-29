def solution(numRows, numColumns, curRow, curColumn, laserCoordinates):

    
    highest_top = max(0,curRow-1)
    highest_bottom = numRows - curRow 
    highest_left = max(0,curColumn -1)
    highest_right = numColumns - curColumn
    for coordinate in laserCoordinates:
        if coordinate[0] == curRow:
            highest_left = min(highest_left, abs(curColumn - coordinate[1]) - 1)
            highest_right = min(highest_right, abs(curColumn - coordinate[1]) - 1)
        elif coordinate[1] == curColumn:
            highest_top = min(highest_top, abs(curRow - coordinate[0]) - 1)
            highest_bottom = min(highest_bottom, abs(curRow - coordinate[0]) - 1)
        else:
            if coordinate[0] < curRow:
                highest_top = min(highest_top, curRow - coordinate[0]-1 )
            else:
                highest_bottom = min(highest_bottom, coordinate[0] - curRow - 1)
            
            if coordinate[1] < curColumn:
                highest_left = min(highest_left, curColumn - coordinate[1]-1)
            else: 
                highest_right = min(highest_right, coordinate[1] - curColumn-1)
            
    return max(highest_top, highest_bottom, highest_left, highest_right)