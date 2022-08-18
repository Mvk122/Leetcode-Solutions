def plusOne(digits):
    index = len(digits) -1
    while index >= 0:
        if digits[index] == 9:
            if index == 0:
                digits[0] = 0
                digits.insert(1, 0)
            else:
                digits[index] = 0
                index -= 1
        else:
            digits[index] = digits[index] + 1
            break
    return digits

print(plusOne([9,9,9]))