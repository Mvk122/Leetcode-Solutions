def maxProfit(prices):
    profit = 0
    pairs = []
    for index, element in enumerate(prices):
        best_sell = element
        for s_index, s_element in enumerate(prices[index:]):
            if s_element > best_sell:
                best_sell = s_element
            elif s_element < best_sell:
                pairs.append([element, best_sell])
                break
    for pair in pairs:
        profit += pair[1] - pair[0]
    return profit

def maxProfitBetter(prices):
    initial_pointer = 0
    pairs = []
    while initial_pointer< len(prices):
        test_pointer = initial_pointer
        best = prices[initial_pointer]
        best_pointer = initial_pointer
        while test_pointer < len(prices)-1:
            test_pointer += 1 
            if prices[test_pointer] > best:
                best = prices[test_pointer]
                best_pointer = test_pointer
            elif prices[test_pointer] < best:
                pairs.append([prices[initial_pointer], best])
                break
            if test_pointer == len(prices) -1:
                best = prices[test_pointer]
                best_pointer = test_pointer
                pairs.append([prices[initial_pointer], best])
                break
        if initial_pointer < best_pointer:
            initial_pointer = best_pointer
        else:
            initial_pointer += 1
    profit = 0
    for pair in pairs:
        profit += pair[1] - pair[0]
    return profit

def maxProfitRefined(prices):
    initial_pointer = 0
    profit = 0
    while initial_pointer< len(prices):
        test_pointer = initial_pointer
        best_pointer = initial_pointer
        while test_pointer < len(prices)-1:
            test_pointer += 1 
            if prices[test_pointer] > prices[best_pointer]:
                best_pointer = test_pointer
            elif prices[test_pointer] < prices[best_pointer]:
                profit += prices[best_pointer] - prices[initial_pointer]
                break
            if test_pointer == len(prices) -1:
                best_pointer = test_pointer
                profit += prices[best_pointer] - prices[initial_pointer]
                break
        if initial_pointer < best_pointer:
            initial_pointer = best_pointer
        else:
            initial_pointer += 1
    return profit
    


print(maxProfitRefined([7,1,5,3,6,4]))
print(maxProfitRefined([7,6,5,4]))
print(maxProfitRefined([1,2,3,4,5]))
