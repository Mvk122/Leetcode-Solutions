import collections
def longestPalindrome(s):
    c = collections.Counter(s)
    one_found = False
    total = 0 
    for i in c:
        if c[i] % 2 == 0:
            total += c[i]
        elif not one_found:
            total += c[i]
            one_found = True
        else:
            total += max(0, c[i]-1)
    return total
