def solution(words):
    pairs = 0
    
    for w_i, word in enumerate(words):
        for c_i, check in enumerate(words):
            if w_i == c_i: 
                continue
            
            if word == check: 
                pairs += 1
            elif word.endswith(check) or check.endswith(word):
                pairs += 1
    return pairs // 2


# Works but is too slow
from collections import Counter
import math

def solution(words):
    pairs = 0
    counts = Counter(words)
    seen_words = set()
    
    for word in counts:
        pairs += math.comb(counts[word], 2)
        
        for compare in counts:
            if compare == word:
                continue
                
            if compare.endswith(word):
                pairs += counts[word] * counts[compare]


                
    return pairs
        

# Fast Working Solution
from collections import Counter
import math

def solution(words):
    pairs = 0
    counts = Counter(words)
    
    for word in counts:
        pairs += math.comb(counts[word], 2)
        
        for i in range(1, len(word)):
            suffix = word[i:]
            pairs += counts[suffix] * counts[word]  # Count pairs where current word is a suffix


                
    return pairs
        