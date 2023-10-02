class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current_vowels = 0
        max_vowels = 0
        s = s.lower()
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(min(k, len(s))):
            if s[i] in vowels:
                current_vowels += 1
        max_vowels = current_vowels
        for i in range(k, len(s)):
            if s[i] in vowels:
                current_vowels += 1
            if s[i-k] in vowels:
                current_vowels -= 1
            max_vowels = max(current_vowels, max_vowels)
        return max_vowels
            