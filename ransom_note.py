from collections import Counter
def canConstruct(ransomNote: str, magazine: str):
    letters = Counter(magazine)
    for r in ransomNote:
        if letters.get(r, 0) == 0:
            return False
        else:
            letters[r] -= 1
    return True