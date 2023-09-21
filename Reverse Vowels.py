def change_string(string, letter, index):
    return string[:index] + letter + string[index+1:]

class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', "E", 'I', 'O', 'U'}
        while l < r:
            if s[l] in vowels:
                if s[r] in vowels:
                    l_c = s[l]
                    r_c = s[r]
                    s = change_string(s, l_c, r)
                    s = change_string(s, r_c, l)
                    l += 1
                    r -= 1 
                else:
                    r -= 1
            else:
                l += 1
        return s