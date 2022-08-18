def plusMinus(arr):
    positive = 0 
    negative = 0 
    zero = 0 
    for element in arr:
        if element > 0:
            positive += 1
        elif element == 0:
            zero += 1 
        else:
            negative += 1
    print(f'{(positive / (positive + negative + zero)):.6f}')
    print(f'{(negative / (positive + negative + zero)):.6f}')
    print(f'{(zero / (positive + negative + zero)):.6f}')

plusMinus([1,1,0,-1,-1])