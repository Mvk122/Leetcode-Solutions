def totalMoney(days):
    
    def summation(n): 
        return (n*(n+1))/2

    weeks = days // 7
    week_till = (weeks*28) + 7*summation(weeks)
    days_left = days - (weeks*7)
    left = summation(weeks+1+days_left) - summation(weeks+1)
    return week_till + left


def totalMoney_2(days):
    def summation(n): 
        return (n*(n+1))/2

    

for i in range(10):

    print(i, totalMoney(i)