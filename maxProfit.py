def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0
    for index, element in enumerate(prices):
        min_price = min(element, min_price)
        if element - min_price > max_profit:
            max_profit = element - min_price
        
    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,5,4]))