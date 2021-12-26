"""
from sys import stdin as si
n,k = map(int,si.readline().split())
A = [int(si.readline()) for _ in range(n)]
cnt=0
for x in A[::-1]:
    cnt += (k//x)
    k = k-(k//x)*x
print(cnt)





from sys import stdin as si
n = int(input())
M = [list(map(int,si.readline().split())) for _ in range(n)]
M = sorted(M, key=lambda x: (x[1],x[0]))
cnt=0
lastT=0
for x in M:
    if lastT <= x[0]:
        cnt+=1
        lastT = x[1]
print(cnt)





from sys import stdin as si
n = int(input())
T = list(map(int,si.readline().split()))
T.sort()
S=0
w=0
for x in T:
    w+=x
    S+=w
print(S)





exp=input().strip()
check = False
S=0
v=0
for i in range(len(exp)):
    if exp[i]=='+':
        S += v*(-1 if check else 1)
        v=0
        pass
    elif exp[i]=='-':
        S += v*(-1 if check else 1)
        check=True
        v=0
        pass
    else:
        v=v*10+int(exp[i])
S += v*(-1 if check else 1)
print(S)




"""

from sys import stdin as si
n=int(input())
dis=list(map(int,si.readline().split()))
pri=list(map(int,si.readline().split()))
S=0
t=pri[0]
for i in range(n-1):
    S+=t*dis[i]
    t = min(t,pri[i+1])
print(S)
