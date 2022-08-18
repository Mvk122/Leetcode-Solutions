def longestCommonPrefix(strs):
    prefix = strs[0]
    for element in strs[1:]:
        if len(prefix) == 0:
            return ""
        if element == "":
            return ""
        for index, (prefix_char, element_char) in enumerate(zip(prefix, element)):
            if prefix_char != element_char:
                prefix = prefix[:index]
                continue 
            if (len(element) < len(prefix)) and index==len(element)-1:
                prefix = prefix[:index+1]
                continue
    return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(['abb', 'ab']))
print(longestCommonPrefix(['ca', 'a']))

