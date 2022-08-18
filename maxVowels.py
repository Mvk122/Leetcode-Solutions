def maxVowels(s,k):
    maximum = 0
    for i in range(len(s)-k+1):
        temp = 0
        for j in range(k):
            if s[i+j] in 'aeiou':
                temp += 1
        if temp > maximum:
            maximum = temp

    return maximum

def maxVowels_better(s, k):
    maximum = 0
    for i in range(k):
        if s[i] in 'aeiou':
            maximum += 1
    current = maximum
    for i in range(1, len(s)-k+1):
        if s[i-1] in 'aeiou':
            current -= 1
        if s[i+k-1] in 'aeiou':
            current += 1
        if current > maximum:
            maximum = current
    return maximum
    
    

print(maxVowels('abdiiidef',3 ))
print(maxVowels_better('leetcode',3))