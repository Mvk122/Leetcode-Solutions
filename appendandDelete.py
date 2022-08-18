def appendAndDelete(s,t,k):
    similar = 0
    for a, b in zip(s,t):
        if a == b:
            similar += 1 
        else:
            break
    return similar

print(appendAndDelete('aaa', 'aabccc', 5))