def median(arr):
    index = len(arr) // 2
    if len(arr) % 2 != 0:
        return arr[index]
    else:
        return (arr[index - 1] + arr[index]) / 2 

def activityNotifications(expenditure, d):
    notifs = 0
    for i in range(d+1, len(expenditure)):
        m = median(expenditure[i-d-1: i-1])
        print(f'Value: {expenditure[i]} values: {expenditure[i-d:i]}')
        if m * 2 >= expenditure[i]:
            notifs += 1 
            
    return notifs

activityNotifications([i for i in range(10)], 3)



