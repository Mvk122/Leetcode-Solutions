class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_vowels = 0
        max_vowels = 0
        s = s.lower()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        if k >= len(s):
            for element in s:
                if element in vowels:
                    current_vowels += 1
            return current_vowels
        else:
            start_pointer = 0
            end_pointer = 0
            while end_pointer < k:
                if s[end_pointer] in vowels:
                    current_vowels += 1
                end_pointer += 1
            max_vowels = current_vowels
            while end_pointer < len(s) -1:
                start_pointer += 1
                end_pointer += 1
                if s[end_pointer] in vowels:
                    current_vowels += 1
                if s[start_pointer-1] in vowels:
                    current_vowels -= 1
                max_vowels = max(max_vowels, current_vowels)
            return max_vowels
            