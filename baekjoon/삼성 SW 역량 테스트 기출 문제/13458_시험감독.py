n = int(input())
m = tuple(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0
for k in m:
    cnt+=1
    k-=b
    if k>0:
        cnt += (k+c-1)//c
print(cnt)
