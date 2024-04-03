import string
import random 
import itertools

def is_flowing(s):
    for i, e in enumerate(s):
        if i == 0:
            continue
        else:
            if ord(e) < ord(s[i-1]):
                return False
    return True

def is_turbulent(s):
    turb = True
    receding = True

    for i, e in enumerate(s):
        if i == 0:
            continue
        elif ord(e) < ord(s[i-1]):
            turb = False
        elif ord(e) > ord(s[i-1]):
            receding = False

    return (not turb) and (not receding)

def is_receding(s):
    for i, e in enumerate(s):
        if i == 0:
            continue
        else:
            if ord(e) > ord(s[i-1]):
                return False
    return True

def calculate_three():
    counted = set()
    count = 0
    for c in string.ascii_lowercase:
        for d in string.ascii_lowercase:
            for e in string.ascii_lowercase:
                if is_turbulent(c+d+e) and c+d+e not in counted:
                    count += 1
                    counted.add(c+d+e)
    return count

def generate_strings(length=3):
    chars = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    for item in itertools.product(chars, repeat=length):
        yield "".join(item)

def check_arb(highest):
    count = 0
    seen = set()
    for i in range(1, highest+1):
        for string in generate_strings(i):
            if string not in seen and is_turbulent(string):
                count += 1
                seen.add(string)
    return count

def check_arb_single(c):
    count = 0
    seen = set()
    for string in generate_strings(c):
        if string not in seen and is_turbulent(string):
            count += 1
            seen.add(string)
    return count

def check_donor_recepient(donor, recepient):
    if donor == "O":
        return True
    if donor == "B" and recepient in ["B", "AB"]:
        return True
    if donor == "AB" and recepient == "AB":
        return True
    if donor == "A" and recepient in ["AB", "A"]:
        return True
    return False

def check_probabilities():
    success = 0 
    fail = 0

    for i in range(100000): 
        if all([check_scenario(), check_scenario(), check_scenario()]):
            success += 1
        else:
            fail += 1

    return success / (success+fail)

def check_scenario():
    donor = random.choice(["A", "B", "O"])
    recepient = random.choice(["A", "B", "AB"])


    if check_donor_recepient(donor, recepient):
        return True

def f(n):
    c = 0
    while n >= 0:
        n -= 2
        c += n-2
    return c

def thing():
    for i in range(-101, 100, 2):
        if f(i) % 2 == 0: 
            print(i, f(i), "here")
            break

def greater_10():
    for i in range(10, 1000):
        if f(i) < 0:
            return False
    return True

def greater_before():
    for i in range(0, 1000, 2):
        if f(i) < f(i-2):
            print(i, f(i), f(i-2))
            return False
    return True


print(greater_before())

