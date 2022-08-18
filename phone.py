import string
def letterCombinations(digits):
    chardict = {}
    for i in range(2,9):
        chardict[str(i)] = string.ascii_lowercase[(i-2)*3:((i-2)*3)+3]
    print(chardict)

letterCombinations(3)