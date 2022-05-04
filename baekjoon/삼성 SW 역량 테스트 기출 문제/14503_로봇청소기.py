n, m = map(int, input().split())
r, c, d = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(n)]
# 0:북, 1:동, 2:남, 3:서
dir = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt=0
fcnt=0
while True:
    if MAP[r][c]==0:
        cnt+=1
    MAP[r][c]=2 #청소 완료 상태
    next_d = (d+4-1)%4
    next_r, next_c = r+dir[next_d][0], c+dir[next_d][1]
    if MAP[next_r][next_c]==0:
        d = next_d
        r, c = next_r, next_c
        fcnt=0
    else:
        d = next_d
        fcnt+=1
    if fcnt==4:
        next_r, next_c = r-dir[next_d][0], c-dir[next_d][1]
        if MAP[next_r][next_c]==1:
            break
        else:
            r, c = next_r, next_c
            fcnt=0
print(cnt)