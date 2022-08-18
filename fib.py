def fib(iterations):
    f = 0
    s = 1
    total = [0, 1]
    for _ in range(iterations):
        new = f + s
        total.append(new)
        f = s
        s = new
    return total

def fib_list(iterations):
    total = [0, 1]
    for i in range(iterations):
        total.append(total[i] + total[i+1])
    return total

print(fib(100))
print(fib_list(100))