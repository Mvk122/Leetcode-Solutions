from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1c = Counter(word1)
        w2c = Counter(word2)
        return Counter(w1c.values()) == Counter(w2c.values()) and (w1c.keys() == w2c.keys())
            