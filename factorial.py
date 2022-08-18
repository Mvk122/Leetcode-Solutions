from math import factorial
def val(n,c):
    return int(factorial(n) / (factorial(c) * factorial(n-c)))

def triangle(n):
    output = []
    for i in range(n):
        for x in range(i+1):
            output.append(val(i,x))
    for o in output:
        print(o, end=" ")

triangle(6)