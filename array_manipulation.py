def arrayManipulation_slow(n, queries):
    myarr = [0 for _ in range(n)]
    for query in queries:
        for i in range(query[0]-1, query[1]):
            myarr[i] += query[2]
    return max(myarr)

def arrayManipulation(n, queries):
    myarr = [0] * (n+1)
    for query in queries:
        myarr[query[0]-1] += query[2]
        myarr[query[1]] -= query[2]
    max_number = 0
    current = 0
    for i in range(len(myarr)):
        current += myarr[i]
        if current > max_number:
            max_number = current
    return max_number

with open('new_input.txt', 'r') as f:
    lines = f.read().splitlines()
    n = int(lines[0].split(' ')[0])
    input_arr = []
    for line_number in range(1, len(lines)):
        arr = lines[line_number].split(" ")
        casted = [int(x) for x in arr]
        input_arr.append(casted)

    print(arrayManipulation(n, input_arr))
    #print(arrayManipulation(10, [[1,5,3], [4,8,7], [6,9,1]]))
