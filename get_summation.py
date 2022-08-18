def getSequenceSum(i, j, k):
    def get_summation(n):
        return (n* (n+1))/2
    sum_i = get_summation(j) - get_summation(i-1)
    sum_k = get_summation(j-1) - get_summation(k-1)
    return int(sum_i + sum_k)

print(getSequenceSum(0,5,-1))