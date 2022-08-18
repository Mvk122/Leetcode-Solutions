def floodFill(image,sr, sc, newColor):
    rows = len(image[0])
    cols = len(image)
    dirs = [[1,0], [0, -1], [-1, 0], [0, 1]]
    visited = [[0 for i in range(rows)] for i in range(cols)]

    def floodFill_f(image, sr,sc, newColor, oldColor, dirs, visited):
        if image[sr][sc] == oldColor:
            image[sr][sc] = newColor
            for d in dirs:
                if sr + d[0] < cols and sc + d[1] < rows and sr + d[0] >= 0 and sc + d[1] >= 0 and visited[sr+d[0]][sc+d[1]] != 1:
                    visited[sr+d[0]][sc+d[1]] = 1
                    floodFill_f(image, sr+d[0], sc+d[1], newColor, oldColor, dirs, visited)
        else:
            return 

    floodFill_f(image, sr, sc, newColor, image[sr][sc], dirs, visited)
    return image

floodFill([[1,1,1],[1,1,0],[1,0,1]], 1,1, 2)
floodFill([[0,0,0], [0,0,0]], 0, 0, 2)
floodFill([[0,0,0], [0,1,1]], 1, 1, 1)