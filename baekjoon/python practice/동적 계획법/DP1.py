"""
for i in range(int(input())):
    n=int(input())
    T=[0]*(n+2)
    T[n]=1
    for i in range(n,1,-1):
        T[i-1]+=T[i]
        T[i-2]+=T[i]
    print(T[0], T[1])

    
"""

"""
import sys
def w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return w(20, 20, 20)
    global D
    if D[a][b][c]==-999:
        if a<b and b<c:
            D[a][b][c]=w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        else:
            D[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return D[a][b][c]


D= [[[-999 for _ in range(21)]for _ in range(21)]for _ in range(21)]
while True:
    a,b,c = map(int, input().split())
    if (a,b,c)==(-1,-1,-1):
        break
    sys.stdout.write("w({}, {}, {}) = {}\n".format(a,b,c,w(a,b,c)))





n=int(input())
D=[0 for _ in range(n+2)]
D[0]=1
D[1]=1
for i in range(2,n+1):
    D[i]=(D[i-1]+D[i-2])%15746
print(D[n])




import sys
D=[1,1,1,1,2,2]
for i in range(6,101):
    D.append(D[i-1]+D[i-5])
for i in range(int(input())):
    sys.stdout.write(str(D[int(input())])+"\n")




n = int(input())
D=[[9999999 for _ in range(3)] for _ in range(n+2)]
D[0][0]=D[0][1]=D[0][2]=0
P = [[0,0,0]]
for i in range(n):
    P.append(list(map(int,input().split())))
for i in range(1,n+1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            else:
                D[i][j]=min(D[i][j], D[i-1][k]+P[i][j])
        
print(min(D[n]))






n = int(input())
T = [list(map(int, input().split())) for _ in range(n)]
D = [[0 for _ in range(i+1)] for i in range(n)]
D[0][0]=T[0][0]
for i in range(n-1):
    for j in range(i+1):
        D[i+1][j]=max(D[i][j]+T[i+1][j], D[i+1][j])
        D[i+1][j+1]=max(D[i][j]+T[i+1][j+1], D[i+1][j+1])
print(max(D[n-1]))





from sys import stdin as si
n = int(input())
P = [0]*(n+1)
for i in range(1,n+1):
    P[i]=int(si.readline())
D = [[0, 0] for _ in range(n+1)]
#D[i][j]:(j+1)올라i번 계단을 밟을 때 최대 점수
D[1][0]=D[1][1] = P[1]
for i in range(2,n+1):
    D[i][0]=D[i-1][1]+P[i]
    D[i][1]=max(D[i-2][0]+P[i],D[i-2][1]+P[i])
print(max(D[n]))





n = int(input())
D=[999999]*(n+1)
D[1]=0
for i in range(2,n+1):
    if i%2==0: D[i]=min(D[i],D[i//2]+1)
    if i%3==0: D[i]=min(D[i],D[i//3]+1)
    D[i]=min(D[i],D[i-1]+1)
print(D[n])




D = [[0]*10,[1]*10]
D[1][0]=0
n = int(input())
for i in range(2,n+1):
    x=i%2
    for j in range(10):
        D[x][j]=((D[1-x][j-1] if j>0 else 0)+(D[1-x][j+1] if j<9 else 0))%1000000000
print(sum(D[n%2])%1000000000)


from sys import stdin as si
n = int(input())
P = [0]*(n+1)
for i in range(1,n+1):
    P[i]=int(si.readline())
D = [[0, 0] for _ in range(n+1)]
D[1][0]=D[1][1] = P[1]
for i in range(2,n+1):
    D[i][0]=D[i-1][1]+P[i]
    if i>=3:
        D[i][1]=max(D[i-2][0]+P[i],D[i-2][1]+P[i],D[i-3][0]+P[i],D[i-3][1]+P[i])
    else:
        D[i][1]=max(D[i-2][0]+P[i],D[i-2][1]+P[i])
print(max(max(D[n]),max(D[n-1])))



"""

"""
n = int(input())
A=list(map(int,input().split()))
D=[0]
l=0
for x in A:
    for i in range(l,-1,-1):
        if D[i] < x:
            if i==l:
                D.append(x)
                l+=1
            elif D[i+1] > x:
                D[i+1]=x
print(l)




n = int(input())
A=list(map(int,input().split()))
D1=[0]*(n+2)
D2=[0]*(n+2)
T=[[0,0] for _ in range(n+1)]
l=0
for i in range(n):
    x=A[i]
    for j in range(l,-1,-1):
        if D1[j] < x:
            if j==l:
                l+=1
                D1[l]=x
                T[i][0]=l
                break
            elif D1[j+1] >= x:
                D1[j+1]=x
                T[i][0]=j+1
                break
l=0
for i in range(n-1,-1,-1):
    x=A[i]
    for j in range(l,-1,-1):
        if D2[j] < x:
            if j==l:
                l+=1
                D2[l]=x
                T[i][1]=l
            elif D2[j+1] >= x:
                D2[j+1]=x
                T[i][1]=j+1
print(max([T[i][0]+T[i][1]-1 for i in range(n)]))





n = int(input())
W = [list(map(int,input().split())) for _ in range(n)]
W = sorted(W,key=lambda x: x[0])
D=[0]*(n+1)
c=0
for i in range(n):
    t = W[i][1]
    if D[c] < t:
        c+=1
        D[c]=t
    else:
        for j in range(c-1, -1, -1):
            if D[j] <= t:
                D[j+1]=t
                break
print(n-c)






A=input().strip()
B=input().strip()
D=[[0]*len(A) for _ in range(2)]
for i in range(len(B)):
    x=i%2
    D[x][0]= 1 if A[0]==B[i] else D[1-x][0]
    for j in range(1,len(A)):
        D[x][j]=max(D[x][j-1],D[1-x][j])
        if A[j]==B[i] and D[1-x][j-1]==D[x][j]:
            D[x][j]+=1
print(max(D[(len(B)-1)%2]))






N = int(input())
A = list(map(int,input().split()))
D = [0]*N
D[0]=A[0]
for i in range(1, N):
    D[i] = max(D[i-1],0)+A[i]
print(max(D))






n, k = map(int, input().split())
item = [list(map(int,input().split())) for _ in range(n)]
sumW=0
D=[0]*(k+1)
for i in range(n):
    sumW=min(sumW+item[i][0], k)
    for j in range(sumW, item[i][0]-1,-1):
        if D[j]<D[j-item[i][0]]+item[i][1]:
            D[j]=D[j-item[i][0]]+item[i][1]

print(max(D))






n, k = map(int, input().split())
D={0:0}
for i in range(n):
    w,v = map(int,input().split())
    temp={}
    for a, b in D.items():
        if w+a <= k:
            temp[w+a] = max(v+b, D.get(w+a,0))
    D.update(temp)
print(max(D.values()))


"""
