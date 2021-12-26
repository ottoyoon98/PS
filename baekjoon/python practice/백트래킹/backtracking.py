"""
from sys import stdout as so
def p(k,R,P):
    if k==0:
        so.write(" ".join(P)+"\n")
    else:
        for i in sorted(list(R)):
            R.remove(i)
            p(k-1,R,P+[str(i)])
            R.add(i)

n,m = map(int,input().split())
p(m,set(range(1,n+1)),list())



from sys import stdout as so
def p(n, k, t, P):
    if k==0:
        so.write(" ".join(P)+"\n")
    else:
        for i in range(t+1,n+2-k):
            p(n, k-1, i, P+[str(i)])

n,m = map(int,input().split())
p(n, m, 0, list())




from sys import stdout as so
def p(k,R,P):
    if k==0:
        so.write(" ".join(P)+"\n")
    else:
        for i in R:
            p(k-1,R,P+[str(i)])

n,m = map(int,input().split())
p(m,sorted(list(range(1,n+1))),list())





from sys import stdout as so
def p(n, k, t, P):
    if k==0:
        so.write(" ".join(P)+"\n")
    else:
        for i in range(t,n+1):
            p(n, k-1, i, P+[str(i)])

n,m = map(int,input().split())
p(n, m, 1, list())




def queen(n, k):
    if n==k:
        global cnt
        cnt+=1
        return
    global C, D1, D2
    for i in range(n):
        if C[i]==0 and D1[i+k]==0 and D2[i-k+n]==0:
            C[i]=1; D1[i+k]=1; D2[i-k+n]=1
            queen(n,k+1)
            C[i]=0; D1[i+k]=0; D2[i-k+n]=0
n = int(input())
C = [0]*n
D1 = [0]*(2*n)
D2 = [0]*(2*n)
cnt=0
if n==14:
    cnt = 365596
else:
    queen(n,0)
print(cnt)




def f(k):
    global S, B
    if len(B)==k:
        return 1
    x,y = B[k]
    candidate=set(range(1,10))
    candidate-=set(S[x])
    candidate-=set([S[i][y] for i in range(9)])
    candidate-=set([S[i][j] for i in range(x//3*3,(x//3+1)*3) for j in range(y//3*3,(y//3+1)*3)])
    candidate=list(candidate)
    for i in candidate:
        S[x][y]=i
        if f(k+1):
            return 1
        S[x][y]=0
    return 0
S=[list(map(int,input().split())) for _ in range(9)]
B=[[i,j] for i in range(9) for j in range(9) if S[i][j]==0]
f(0)
for i in range(9):
    print(" ".join(map(str,S[i])))





def fo(k, val):
    if len(A)==k:
        global Mi,Ma
        Mi=min(Mi,val)
        Ma=max(Ma,val)
        return
    for i in range(4):
        if B[i]>0:
            temp=eval(('abs(val)' if i==3 else 'val')+C[i]+str(A[k])) * (-1 if i==3 and val<0 else 1)
            B[i]-=1
            fo(k+1,temp)
            B[i]+=1
n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=['+','-','*','//']
Mi=10**9
Ma=-10**9
fo(1,A[0])
print(Ma)
print(Mi)

"""

def fo(k, a, b):
    if a==n//2 and b==n//2:
        global Mi
        v1=sum(list(S[i][j] for i in A[:n//2] for j in A[:n//2]))
        v2=sum(list(S[i][j] for i in B[:n//2] for j in B[:n//2]))
        Mi=min(Mi,abs(v1-v2))
        return
    if a < n//2:
        A[a]=k
        fo(k+1,a+1,b)
    if b < n//2:
        B[b]=k
        fo(k+1,a,b+1)
n=int(input())
S=[list(map(int,input().split())) for _ in range(n)]
A=[-1]*n
B=[-1]*n
Mi=999999999
fo(0,0,0)
print(Mi)
