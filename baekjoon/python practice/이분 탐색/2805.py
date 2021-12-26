"""
from sys import stdin as si
n, m = map(int, si.readline().split())
A = sorted(list(map(int, si.readline().split())), reverse=True)
A.append(0)
l = 0
r = A[0]
ans=0; sum=0; pre=0
for i in range(1,n+1):
    pre=sum
    sum+=(A[i-1]-A[i])*i
    if sum >= m:
        ans=A[i-1]-((m-pre)+(i-1))//i
        break
print(ans)

"""

from sys import stdin as si
w=int(si.readline())
n=int(si.readline())
sum=0
for _ in range(n):
    wi, li = map(int, si.readline().split())
    sum+=wi*li
print(sum//w)