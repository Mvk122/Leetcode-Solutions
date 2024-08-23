#time complexity: O(n)
import collections
def bioHazard(n, allergic, poisonous):
    d = collections.defaultdict(lambda :-1)
    for a,b in zip(allergic, poisonous):
        a,b = sorted([a,b])
        d[b] = max(d[b],a)
        
    for i in range(1, n+1):
        d[i] = max(d[i], d[i-1])
    
    res = 0
    for i in range(1, n+1):
        if d[i]==-1:
            res += i
        else:
            res += i-d[i]
    return res

print(bioHazard(4, [1,2], [3,4]))