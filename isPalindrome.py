import string
def isPalindromeP(inp):
    start = 0 
    inp = ''.join([c for c in inp if c in string.ascii_letters + string.digits])
    end = len(inp) - 1
    while start < end:
        if inp[start].lower() != inp[end].lower():
            return False
        start += 1
        end -= 1 
    return True

def isPalindromeRemove(s):


    start = 0
    end = len(s) - 1
    chances = 2
    original = s
    while start < end:
        if s[start] != s[end]:
            if chances == 0:
                return False
            elif chances == 1:
                s = original[:start] + original[start+1:]
                print(s)
                chances -= 1
            else:
                s = original[:end] + original[end+1:]
                print(s)
                chances -= 1 
            start = 0 
            end = len(s) -1
            continue
        start += 1 
        end -= 1

    return True 


# print(isPalindromeRemove("abca"))
# print(isPalindromeRemove("aabaaaa"))
# print(isPalindromeRemove("aaaabaa"))
# print(isPalindromeRemove("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"))
# print(isPalindromeRemove("abc"))
print(isPalindromeRemove("ebcbbececabbacecbbcbe"))