import math
def create_integer_dict(arr):
    int_dict = {}
    for element in arr:
        if element in int_dict.keys():
            int_dict[element] += 1
        else:
            int_dict[element] = 1
    return int_dict

def prime_factorisation(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors

# Complete the countTriplets function below.
def countTriplets(arr, r):
    number_dict = create_integer_dict(arr)
    total = 0
    for number in number_dict.keys():
        prime_factors = prime_factorisation(number)
        #print(prime_factors)
        if r not in prime_factors and prime_factors != []:
            continue
        if prime_factors != []:
            pfs = set(prime_factors)
            pfs.remove(r)
            mul = 1
            for elem in pfs:
                mul *= elem
            exponent = len(prime_factors) - 1
        else:
            mul = 1
            exponent = 1

        #print(r, exponent, mul)
        if mul*(r**exponent) in number_dict.keys() and mul*(r**(exponent+1)) in number_dict.keys() and mul*(r**(exponent+2)) in number_dict.keys():
            total += number_dict[mul*(r**exponent)] * number_dict[mul*(r**(exponent+1))] * number_dict[mul*(r**(exponent+2))]
    return total

print(countTriplets([1,5,5,25,125], 5))
#print(countTriplets([1 for _ in range(100)], 1))
#print(prime_factorisation(2))
