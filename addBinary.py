from itertools import zip_longest
def addBinary(a,b):
    sol = ''
    carry = False
    for a_c, b_c in zip_longest(reversed(a), reversed(b)):
        current = 0
        if a_c is None:
            current += int(b_c)
        elif b_c is None:
            current += int(a_c)
        else:
            current += int(a_c) + int(b_c)
        if carry:
            current += 1
        if current == 1:
            carry = False
            sol += ('1')
        elif current == 0:
            carry = False
            sol += ('0')
        elif current == 2:
            sol += ('0')
            carry = True 
        elif current == 3:
            sol += ('1')
            carry = True

    if carry:
        sol += '1'
    return sol[::-1]

print(addBinary('11', '1'))

        