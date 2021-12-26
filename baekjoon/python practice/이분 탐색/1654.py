from sys import stdin as si
k, n = map(int, si.readline().split())
A = sorted(list([int(si.readline()) for _ in range(k)]))
l=1
r=A[k-1]
ans=0
while l<=r:
    m=(l+r)//2
    cnt = 0
    for x in A:
        cnt+=(x//m)
    if cnt >= n:
        l=m+1
        ans=max(ans,m)
    else:
        r=m-1
print(ans)
