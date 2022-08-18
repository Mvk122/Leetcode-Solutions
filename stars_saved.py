    def find(s, start, end):
        left_present = False
        confirmed = 0
        unconfirmed = 0
        for char in s[start-1:end]:
            if char == '|':
                if left_present:
                    confirmed += unconfirmed
                    unconfirmed = 0
                else:
                    unconfirmed = 0
                    left_present = True
            else:
                if left_present:
                    unconfirmed += 1
        return confirmed
    
    def better_find(s, startIndex, endIndex):
        return s[startIndex-1:endIndex].strip("*").count("*")
    
    results = []
    for index, start in enumerate(startIndex):
        results.append(better_find(s, start, endIndex[index]))
    return results