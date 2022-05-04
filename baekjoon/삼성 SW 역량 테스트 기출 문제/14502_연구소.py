from collections import deque

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(n)]

queue = deque()
candidate = deque()
safe_area = 0
p_cnt = 0
p_bound = n*m
for i in range(n):
    for j in range(m):
        if MAP[i][j]==0:
            safe_area+=1            
            if 0<i and i<n-1 and 0<j and j<m-1 and MAP[i][j+1]+MAP[i][j-1]+MAP[i+1][j]+MAP[i-1][j]==0:
                candidate.append((i,j,1))
            else:
                candidate.append((i,j,0))
            

def check_range(a, b):
    if a<0 or a>=n or b<0 or b>=m:
        return False
    return True


def MAP_scan():
    queue.clear()
    for i in range(n):
        for j in range(m):
            if MAP[i][j] > 2:
                MAP[i][j]=0
            elif MAP[i][j] == 2:
                queue.append((i,j))
                
dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
answer=0
for i in range(len(candidate)):
    for j in range(i+1,len(candidate)):
        for k in range(j+1,len(candidate)):
            MAP[candidate[i][0]][candidate[i][1]]=1
            MAP[candidate[j][0]][candidate[j][1]]=1
            MAP[candidate[k][0]][candidate[k][1]]=1
            p_cnt=0
            MAP_scan()
            while queue:
                x, y = queue.popleft()
                for dx, dy in dir:
                    if check_range(x+dx, y+dy) and MAP[x+dx][y+dy]==0:
                        MAP[x+dx][y+dy]=MAP[x][y]+1
                        queue.append((x+dx, y+dy))
                        p_cnt+=1
                if p_cnt > p_bound:
                    break
            p_bound = min(p_bound, p_cnt)
            MAP[candidate[i][0]][candidate[i][1]]=0
            MAP[candidate[j][0]][candidate[j][1]]=0
            MAP[candidate[k][0]][candidate[k][1]]=0
print(safe_area-3-p_bound)