def ahead(array, position):
    ahead_count = 0
    for i in range(0, position):
        if array[i] > array[position]:
            ahead_count += 1
    return ahead_count 

def minimumBribes(q):
    bribes = 0
    for position, element in enumerate(q):
        bribe = element - position + ahead(q, position) -1
        print(bribe, position, element, ahead(q,position))
        if bribe > 2:
            print("Too chaotic")
        bribes += bribe
    print(bribes)

minimumBribes([5,1, 2 ,3, 7, 8, 6, 4])