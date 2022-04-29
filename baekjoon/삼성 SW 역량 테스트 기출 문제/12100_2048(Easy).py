n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
Max = 0


def DFS(c_board, depth):
    def validI(index):
        if index < 0 or index >= n:
            return False
        else:
            return True
    max_value = 0
    for line in c_board:
        max_value = max(max(line), max_value)
    if depth==5:
        return max_value
    else:
        for dx, dy in dirs:
            n_board = [[0 for j in range(n)] for i in range(n)]
            check = [[False for j in range(n)] for i in range(n)]
            for i in (range(n) if dx<=0 else range(n-1,-1,-1)):
                for j in (range(n) if dy<=0 else range(n-1, -1, -1)):
                    k = 0
                    x, y = i, j
                    while validI(x+dx) and validI(y+dy) and n_board[x+dx][y+dy]==0:
                        x, y = x+dx, y+dy
                    if validI(x+dx) and validI(y+dy) and n_board[x+dx][y+dy]==c_board[i][j] and not check[x+dx][y+dy]:
                        n_board[x+dx][y+dy]*=2
                        check[x+dx][y+dy]=True
                    else:
                        n_board[x][y]=c_board[i][j]
                        check[x][y]=False
            if n_board != c_board:
                max_value = max(DFS(n_board, depth+1), max_value)
    return max_value
print(DFS(board, 0))