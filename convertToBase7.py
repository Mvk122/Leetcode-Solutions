def convertToBase7(num):
    """
    :type num: int
    :rtype: str
    """
    negative = num < 0
    returnstr = ""
    if num == 0:
        return "0"
    
    num = abs(num)
    result = num
    remainder = 0
    while result != 0:
        remainder = result % 7
        result = result // 7
        returnstr = str(remainder) + returnstr

    if negative:
        returnstr = "-" + returnstr
    return returnstr

print(convertToBase7(-100))
print(convertToBase7(1))