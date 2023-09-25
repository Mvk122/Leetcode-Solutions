def mergeAlternately(word1: str, word2: str) -> str:
    p1 = 0
    p2 = 0
    left = True
    current = ""
    while p1 < len(word1) and p2 < len(word2):
        if left:
            current = current + word1[p1]
            p1 += 1
            left = False
        else:
            current = current + word2[p2]
            p2 += 1
            left = True
    if p1 == len(word1):
        current = current + word2[p2:]
    elif p2 == len(word2):
        current = current + word1[p1:]
    return current

print(mergeAlternately("abc", "pqr"))