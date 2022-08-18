def whatFlavors(cost, money):
    h = {}
    for index, value in enumerate(cost):
        if money - value in h:
            second = h[money-value]
            if index < second:
                print(index, second)
            else:
                print(second, index)
            return
        else:
            h[value] = index
    

money = 7
cost = [5,3,4,6]
whatFlavors(cost, money)