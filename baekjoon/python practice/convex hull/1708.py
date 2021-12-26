import sys


def CCW(P1, P2, P3):
    ccw = (P2[0]-P1[0])*(P3[1]-P1[1])-(P3[0]-P1[0])*(P2[1]-P1[1])
    return 0 if ccw==0 else (1 if ccw>0 else -1)


def length(P1, P2):
    return (P2[0]-P1[0])**2+(P2[1]-P1[1])**2


n = int(sys.stdin.readline())
coor = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
convex_hull = []
hI = 0
for i in range(1,n):
    if coor[i][1] < coor[hI][1] or (coor[i][1] == coor[hI][1] and coor[i][0] < coor[hI][0]):
        hI = i
coor[0], coor[hI] = coor[hI], coor[0]

cnt = 1
while True:
    # P1=coor[cnt-1], P2=coor[cnt], P3=coor[i]
    for i in range(cnt+1,n):
        ccw = CCW(coor[cnt-1], coor[cnt], coor[i])
        if ccw < 0 or (ccw==0 and length(coor[cnt-1], coor[cnt]) < length(coor[cnt-1], coor[i])):
            coor[cnt], coor[i] = coor[i], coor[cnt]
    ccw = CCW(coor[cnt-1], coor[cnt], coor[0])
    if ccw < 0 or (ccw == 0 and length(coor[cnt - 1], coor[cnt]) < length(coor[cnt - 1], coor[0])):
        break
    cnt+=1
print(cnt)
