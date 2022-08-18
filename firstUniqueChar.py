def firstUniqChar(s):
    chars = {}
    for index, char in enumerate(s): 
        if char in chars:
            chars[char] = -1
        else:
            chars[char] = index
    minimum = -1
    for c in chars:
        if minimum == -1 and chars[c] != -1:
            minimum = chars[c]
        elif chars[c] == -1:
            pass
        else:
            minimum = min(chars[c], minimum)

    return minimum


print(firstUniqChar("leetcode"))
print(firstUniqChar("aabb"))
print(firstUniqChar("aadadaad"))
