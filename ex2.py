r =2
y = 1

d = 0
while y <= r:
    s = r
    c = y
    while c>0:
        c -= 1 
        s -= 1
    if r != s:
        d = d+1
        r = s
print(r, y, d)