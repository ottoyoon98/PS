n, m = map(int, input().split())
paper = [list(map(int, input().split())) for i in range(n)]
table = [[[0,]*3 for j in range(m)] for i in range(n)]

def tetromino(x, y, k):
    if x<0 or y<0 or x>=n or y>=m:
        return -10000
    if k == 3:
        return paper[x][y]
    if table[x][y][k]!=0:
        return table[x][y][k]
    temp = 0
    if k == 0:
        temp = max(tetromino(x, y+1, 2) + tetromino(x+1, y, 3),
                   tetromino(x, y+1, 3) + tetromino(x+1, y, 2),
                   tetromino(x-1, y+1, 3) + tetromino(x, y+1, 2),
                   tetromino(x, y-1, 3) + tetromino(x-1, y, 3) + max(tetromino(x-2, y, 3), tetromino(x, y-2, 3)),
                   tetromino(x, y+1, 3) + tetromino(x+1, y, 3) + max(tetromino(x+1, y-1, 3), tetromino(x-1, y+1, 3)))
    elif k == 1:
        temp = tetromino(x, y+1, 3) + tetromino(x+1, y, 3)
    temp = max(temp, tetromino(x, y+1, k+1), tetromino(x+1, y, k+1))
    table[x][y][k] = paper[x][y]+temp
    return table[x][y][k]

maxSUM = 0
for i in range(n):
    for j in range(m):
        maxSUM = max(maxSUM, tetromino(i, j, 0))
print(maxSUM)