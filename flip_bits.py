def flippingBits(n):
    binary = '{:032b}'.format(n)
    r = ''
    for char in binary:
        if char == '0':
            r += '1'
        else:
            r += '0'
        
    return int(r, 2)