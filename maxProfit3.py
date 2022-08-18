def getfirst2(arr):
    total = 0
    for index, element in enumerate(arr):
        if index == 2:
            break
        else:
            total += element

    return total


def maxProfitRefined(prices):
    initial_pointer = 0
    profit = []
    while initial_pointer< len(prices):
        test_pointer = initial_pointer
        best_pointer = initial_pointer
        while test_pointer < len(prices)-1:
            test_pointer += 1 
            if prices[test_pointer] > prices[best_pointer]:
                best_pointer = test_pointer
            elif prices[test_pointer] < prices[best_pointer]:
                profit.append(prices[best_pointer] - prices[initial_pointer])
                break
            if test_pointer == len(prices) -1:
                best_pointer = test_pointer
                profit.append(prices[best_pointer] - prices[initial_pointer])
                break
        if initial_pointer < best_pointer:
            initial_pointer = best_pointer
        else:
            initial_pointer += 1
    profit.sort(reverse=True)
    print(profit)
    return getfirst2(profit)


#print(maxProfitRefined([3,3,5,0,0,3,1,4]))
#print(maxProfitRefined([1,2,3,4,5]))
#print(maxProfitRefined([7,6,5,4]))
print(maxProfitRefined([1,2,4,2,5,7,2,4,9,0]))