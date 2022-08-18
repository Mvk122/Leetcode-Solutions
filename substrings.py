def get_substrings(s):
    strings = []
    for length in range(1, len(s)):
        part = []
        for index in range(len(s) - length + 1):
            part.append(s[index:index+length])
        strings.append(part)
    strings.append([s])
    return strings

def get_character_counts(string):
    char_dict = {}
    for char in string:
        if char in char_dict.keys():
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def get_anagram_count(arr, index):
    element = arr[index]
    other_arr = arr[:index] + arr[index+1:]
    count = 0
    for e in other_arr:
        if e == element:
            count += 1
    return count

def sherlockAndAnagrams(s):
    substrings = get_substrings(s)
    character_counts = [[get_character_counts(s) for s in arr] for arr in substrings]
    c = 0
    for array in character_counts:
        for i in range(len(array)):
            c += get_anagram_count(array, i)
    return int(c/2)


print(sherlockAndAnagrams('abba'))
