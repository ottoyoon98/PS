n, l = map(int, input().split())
MAP = [list(map(int, input().split())) for i in range(n)]
answer=0

def sub_routine(i, mode):
    global answer
    check = True
    cnt=1
    pre_h = MAP[i][0] if mode==0 else MAP[0][i]
    for j in range(1, n):
        M = MAP[i][j] if mode==0 else MAP[j][i]
        if pre_h == M:
            cnt+=1
        elif pre_h+1 == M:
            if cnt>=l and check:
                cnt=1
                pre_h=M
            else:
                check=False
                break
        elif pre_h-1 == M  and check:
            cnt=1
            pre_h=M
            check=False
        else:
            check=False
            break
        if not check and cnt>=l:
            cnt-=l
            check=True
    if check:
        answer+=1    
        
for i in range(n):
    sub_routine(i, 0)
    sub_routine(i, 1)
print(answer)