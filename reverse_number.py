def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    num_str = str(x)
    if num_str[0] == "-":
        number = - int(num_str[1:][::-1])
    else:
        number = int(num_str[::-1])
    print(number)
    if number > (2**31)-1 or number < -(2**31):
        return 0
    else:
        return number

print(reverse(-123))