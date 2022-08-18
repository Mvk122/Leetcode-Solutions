def intfrombinary(binary):
    p = 0
    counter = 0
    for character in binary[::-1]:
        counter += int(character) * (2**p)
        p += 1 
    return counter

def hasAllCodes(s,k):

    if len(s) < k:
        return False
    found = [False] * (2**k)
    print(found)
    for i in range(len(s)-k+1):
        found[intfrombinary(s[i:i+k])] = True

    for f in found:
        if not f:
            return False

    return True

print(hasAllCodes('00110110', 2))