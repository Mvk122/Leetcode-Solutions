# lecture: https://www.youtube.com/watch?v=NdF1QDTRkck&t=716s
def permute_f(current, remainder, result):
    if remainder == "":
        result.append(current)
    else:
        for i in range(len(remainder)):
            permute_f(current+remainder[i], remainder[:i] + remainder[i+1:], result)

#Returns permutation of the chars, eg abc becomes abc, bac, cab etc all with the initial length of the string 
def permute(chars):
    result = []
    permute_f("", chars, result)
    return result
 
def permute_subsets_f(current, remainder, result):
    if remainder == "":
        result.append(current)
    else:
        permute_subsets_f(current+remainder[0], remainder[1:], result)
        permute_subsets_f(current, remainder[1:], result)

#Returns all combinations of the characters in order. eg abc becomes a, ab, bc, abc. There is no ca or ba.
def permute_subsets(chars):
    result = []
    permute_subsets_f("", chars, result)
    return result


# print(permute("abc"))
# print(permute_subsets("abc"))
