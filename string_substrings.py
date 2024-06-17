from collections import Counter


def func(s, k):
    found = 0

    l = Counter("")
    r = Counter(s)

    for char in s:
        if len(set(l).intersection(set(r))) > k:
            found += 1
        
        if char in l:
            l[char] += 1
        else:
            l[char] = 1
        
        if char in r:
            if r[char] == 1:
                del r[char]
            else: 
                r[char] -= 1
    
    return found

    

if __name__ == "__main__":
    print(func('abbcac', 1))