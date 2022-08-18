def build_dict(string):
    return_dict = {}
    for char in string:
        if char in return_dict.keys():
            return_dict[char] += 1
        else:
            return_dict[char] = 1 
    return return_dict

def isValid(s):
    char_dict = build_dict(s)
    chr_set = set(char_dict.values())
    print(chr_set)
    if len(chr_set) == 1:
        return "YES"
    elif len(chr_set) == 2:
        set_list = list(chr_set)
        if abs(set_list[0] - set_list[1] > 1):
            return "NO"
        else:
            return "YES"
    else:
        return "NO"
            

print(isValid('aabbcd'))