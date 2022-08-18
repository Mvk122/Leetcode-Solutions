def numSpecial(mat):
    def count(arr, counter):
        c = 0 
        for a in arr:
            if a == counter:
                c += 1 
        return c

    rows = [0] * len(mat)
    cols = [0] * len(mat[0])
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 1:
                rows[row] += 1 
                cols[col] += 1
    out = 0
    print(rows, cols)
    for r, c in zip(rows, cols):
        if r == 1 and c == 1:
            out += 1
    return out

print(numSpecial([[1,0,0],[0,1,0],[0,0,1]]))
print(numSpecial([[1,0,0],[0,0,1],[1,0,0]]))
print(numSpecial([[0,0,1,0],[0,0,0,0],[0,0,0,0],[0,1,0,0]]))
print(numSpecial([[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,1],[0,0,0,0,1,0,0,0],[1,0,0,0,1,0,0,0],[0,0,1,1,0,0,0,0]]))