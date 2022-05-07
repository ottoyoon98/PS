#15683 감시
N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(N)]
CCTV = [[i,j,MAP[i][j],0] for i in range(N) for j in range(M) if 1<=MAP[i][j]<=5]
CCTV_dir = (0, 4, 2, 4, 4, 1)
CCTV_dk = ((0,), (0, 2), (0, 1), (0, 1, 2), (0, 1, 2, 3))
dir = [(0,1),(-1,0),(0,-1),(1,0)]
answer = N*M

def DFS(n):
    global CCTV
    global answer
    if n == len(CCTV):
        tMAP = [MAP[i][:] for i in range(N)]
        for x,y,k,d in CCTV:
            for dk in CCTV_dk[k-1]:
                td = (d+dk)%4
                tx, ty = x,y
                while True:
                    tx, ty = tx+dir[td][0], ty+dir[td][1]
                    if tx<0 or tx>=N or ty<0 or ty>=M or tMAP[tx][ty]==6:
                        break
                    if tMAP[tx][ty]==0:
                        tMAP[tx][ty]=7
        cnt = len([1 for i in range(N) for j in range(M) if tMAP[i][j]==0])
        answer = min(answer, cnt)
        return
    
    for i in range(CCTV_dir[CCTV[n][2]]):
        CCTV[n][3] = i
        DFS(n+1)
    return

DFS(0)
print(answer)