def permute_array(arr):
    def permute_arr_f(current, remainder, result):
        if len(remainder) == 0:
            result.append(current)
        else:
            for i in range(len(remainder)):
                temp = current.copy()
                temp.append(remainder[i])
                permute_arr_f(temp, remainder[:i] + remainder[i+1:], result)

    result = []
    permute_arr_f([], arr, result)
    return result

def permute_array_subsets(arr):
    def permute_arr_subsets_f(current, remainder, result):
        if len(remainder) == 0:
            result.append(current)
        else:
            temp = current.copy()
            temp.append(remainder[0])
            permute_arr_subsets_f(temp, remainder[1:], result)
            permute_arr_subsets_f(current, remainder[1:], result)
    result = []
    permute_arr_subsets_f([], arr, result)
    return result

print(permute_array([1,2,3]))
print(permute_array_subsets([1,2,3]))