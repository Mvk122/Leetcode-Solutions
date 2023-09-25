def replace(s, index, newstring):
    return s[:index] + newstring + s[index + 1:]


def reverseVowels(self, s: str) -> str:
    l = 0
    r = len(s) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    while l < r:
        print(l, r)
        if s[l] in vowels:
            if s[r] in vowels:
                temp = s[l]
                s = replace(s, l, s[r])
                s = replace(s, r, temp)
                l += 1
                r -= 1
            else:
                r -= 1
        else:
            l += 1
    return s