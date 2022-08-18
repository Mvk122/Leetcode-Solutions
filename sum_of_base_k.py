def sumBase(n, k):
    def getDigits(number):
        print(number)
        total = 0
        for d in str(number):
            total += int(d)
        return total
    quotient = n 
    remainders = 0
    while quotient >= k:
        remainders += getDigits(quotient % k)
        quotient = quotient // k
    remainders += getDigits(quotient)
    return remainders

print(sumBase(42, 2))