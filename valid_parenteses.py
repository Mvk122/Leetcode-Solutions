def isValid(s):
    p_dict = {"(": ")", "{" : "}", "[" : "]"}
    stack = []
    for char in s:
        if char in p_dict.keys():
            stack.append(p_dict[char])
        else:
            if len(stack) == 0:
                return False
            if char == stack[-1]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

print(isValid("(]"))