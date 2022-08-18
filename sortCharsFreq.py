from collections import Counter
def frequencySort(s):
    c = Counter(s)
    retstr = ""
    for s in  sorted(c.items(), key= lambda x: x[1], reverse=True):
        retstr += s[0] * s[1]
    return retstr
print(frequencySort('test'))
