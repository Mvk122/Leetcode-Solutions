def isPossible(a, b, c, d):
    def test(a,b):
        if a % b == 0:
            return b 
        else:
            return test(b, a%b)
    print(a,b,c,d)
        
    if test(a,b) == test(c,d):
        return 'Yes'
    else:
        return 'No'

print(isPossible(1,2,2,1))