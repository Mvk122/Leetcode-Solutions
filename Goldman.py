def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

def isPossible(a, b, c, d):
    if gcd(a,b) == gcd(c,d):
        return "Yes"
    else:
        return "No"
    

def isPossible(a, b, c, d):
    if a == c and b == d: 
        return "Yes"
    if a < c:
        return isPossible(a+b, b, c, d)
    if b < d:
        return isPossible(a, b+a, c, d)
    
    return "No"

def move(a,b,c,d):
    if a==c and b==d:
        return True
    elif a>c or b>d:
        return False
    else:
        ans = False
        if a < c:
            if move(a+b,b,c,d):
                return True
        if b < d:
            if move(a,b+a,c,d):
                return True
    return False



def isPossible(a, b, c, d):
    if a == c and b == d: 
        return "Yes"
    elif a > c or b > d:
        return "No"
    else:    
        if a < c:
            if isPossible(a+b, b, c, d):
                return "Yes"
        if b < d:
            if isPossible(a, b+a, c, d):
                return "Yes"
    return "No"

        
    
    
# Recurses too much but works
def isPossible(a, b, c, d):
    if a == c and b == d: 
        return "Yes"
    elif a > c or b > d:
        return "No"
    else:    
        if a < c and (a+b, b):
            if isPossible(a+b, b, c, d) == "Yes":
                return "Yes"
        if b < d and (a, a+b):
            if isPossible(a, b+a, c, d) == "Yes":
                return "Yes"
    return "No"

# Done with BFS
def isPossible(a, b, c, d):
    queue = []
    queue.append((a,b))
    seen = set()
    
    while queue:
        a, b = queue.pop(0)
        seen.add((a,b))
        if a == c and b == d:
            return "Yes"
        
        new_a, new_b = a, a+b
        if (new_a, new_b) not in seen:
            if new_a <= c and new_b <= d:
                queue.append((new_a, new_b))
        
        new_a, new_b = a+b, b
        if (new_a, new_b) not in seen:
            if new_a <= c and new_b <= d:
                queue.append((new_a, new_b))
    return "No"
    