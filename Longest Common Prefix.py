from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    current = 0
    current_letter = None

    while True: 
        if current > len(strs[0]) - 1:
            return strs[0]
        current_letter = strs[0][current]
        for s in strs:
            if current >= len(s):
                return s
            if s[current] != current_letter:
                return s[:current]
        current += 1

print(longestCommonPrefix(["ab", "a"]))