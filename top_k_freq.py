from collections import Counter
def topKFrequent(nums, k):
    c = Counter(nums)
    return [s[0] for s in sorted(c.items(), key=lambda x: x[1], reverse=True)[:k]] 

print(topKFrequent([1,1,1,2,2,3], 2))