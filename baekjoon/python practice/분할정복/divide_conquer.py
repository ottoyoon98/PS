"""
from sys import stdin as si
def color(A, size):
    w,b=0,0
    if size==1:
        return (0,1) if A[0][0]==1 else (1,0)
    cnt=0
    for i in range(size):
        cnt+=sum(A[i])
    if cnt==size*size:
        return (0,1)
    if cnt==0:
        return (1,0)
    
    T=[0,size//2,size]
    for i in range(2):
        for j in range(2):
            temp=color(list(row[T[i]:T[i+1]] for row in A[T[j]:T[j+1]]), size//2)
            w+=temp[0]
            b+=temp[1]
    return (w,b)
    
n=int(si.readline())
paper=[list(map(int,si.readline().split())) for i in range(n)]
t=color(paper,n)
print(t[0])
print(t[1])





from sys import stdin as si, stdout as so
def comp(x, y, size):
    global A
    if size==1:
        so.write(str(A[x][y]))
        return
    ct=sum(sum(x[y:y+size]) for x in A[x:x+size])
    if ct==size*size:
        so.write("1")
        return
    if ct==0:
        so.write("0")
        return
    so.write("(")
    comp(x,y,size//2)
    comp(x,y+size//2,size//2)
    comp(x+size//2,y,size//2)
    comp(x+size//2,y+size//2,size//2)
    so.write(")")
    return

n=int(si.readline())
A=[list(map(int,si.readline().strip())) for i in range(n)]
comp(0,0,n)




from sys import stdin as si, stdout as so
def div9(x,y,size):
    global paper
    cnt=[0,0,0]
    if size==1:
        cnt[paper[x][y]+1]=1
    else:
        for i in range(3):
            for j in range(3):
                temp=div9(x+(size//3)*i,y+(size//3)*j,size//3)
                cnt[0]+=temp[0]
                cnt[1]+=temp[1]
                cnt[2]+=temp[2]
        if (9 in cnt) and sum(cnt)==9:
            for i in range(3):
                cnt[i]//=9
    return cnt

n=int(si.readline())
paper=[list(map(int, si.readline().split())) for i in range(n)]
kind=div9(0,0,n)
for i in range(3):
    print(kind[i])







a,b,c=map(int,input().split())
R=[]
while b > 0:
    R.append(b%2)
    b//=2
T=1
for x in R[::-1]:
    T=(T*T)%c
    if x==1:
        T=(T*a)%c
print(T)



"""


#n,k = map(input().split())
#k = min(k, n-k)

"""
from sys import stdin as si, stdout as so
n,m=map(int,si.readline().split())
A=[list(map(int,si.readline().split())) for _ in range(n)]
m,k=map(int,si.readline().split())
B=[list(map(int,si.readline().split())) for _ in range(m)]
C=[[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for t in range(m):
            C[i][j]+=(A[i][t]*B[t][j])
    so.write(" ".join(map(str,C[i]))+"\n")


from sys import stdin as si, stdout as so
def mul(MA, MB, n):
    return [list(sum(MA[i][k]*MB[k][j] for k in range(n))%1000 for j in range(n)) for i in range(n)]
N,B = map(int,si.readline().split())
A=[list(map(int, si.readline().split())) for _ in range(N)]
R=[]
while B>0:
    R.append(True if B%2==1 else False)
    B//=2
R=R[::-1]
C=A
for x in R[1:]:
    C=mul(C,C,N)
    if x:
        C=mul(C,A,N)
C = [list(C[i][j]%1000 for j in range(N)) for i in range(N)]
for i in range(N):
    so.write(" ".join(map(str,C[i]))+"\n")





def mul(MA,MB):
    return [list(sum(MA[i][k]*MB[k][j] for k in range(2))%1000000007 for j in range(2)) for i in range(2)]
n=int(input())
A=[[1,1],[1,0]]
B=[[1,1],[1,0]]
n-=1
R=[]
while n>0:
    R.append(n%2)
    n//=2
R=R[::-1]
for x in R[1:]:
    A=mul(A,A)
    if x==1:
        A=mul(A,B)
print(A[0][0])




from sys import stdin as si, stdout as so
def main():
    def rectangle(left,right):
        temp=[]

        return temp
    
    while True:
        n, *A = map(int, si.readline().split())
        if n==0:
            break
        temp=rectangle(0,n-1)
        so.write(str(max(list(temp[i][0]*temp[i][1] for i in range(3))))+"\n")
main()


"""
import time

from sys import stdin as si
def dis(A, B):
    return ((A[0]-B[0])**2+(A[1]-B[1])**2)
def main():
    n=int(si.readline())
    point=[list(map(int,si.readline().split())) for _ in range(n)]
    point = sorted(point, key=lambda x:(x[0],x[1]))
    for i in range(n-1):
        if point[i]==point[i+1]:
            print(0)
            return
    min_dis=dis(point[0],point[1])
    def pro(left, right):
        nonlocal min_dis
        if right-left <= 100:
            for i in range(left,right+1):
                for j in range(i+1,right+1):
                    if point[j][0]-point[i][0]>min_dis:
                        break
                    min_dis=min(min_dis, dis(point[i],point[j]))
            return min_dis
        else:
            temp=min(pro(left,(left+right)//2),pro((left+right)//2+1,right))
            tl=(left+right)//2
            tr=tl+1
            while tl>left:
                if point[(left+right)//2+1][0]-point[tl][0]>=min_dis:
                    break
                tl-=1
            
            while tr<right:
                if point[tr][0]-point[(left+right)//2][0]>=min_dis:
                    break
                tr+=1
                
            P2=sorted(point[tl:tr+1], key=lambda x:(x[1],x[0]))
            for i in range(tl, tr+1):
                for j in range(i+1,tr+1):
                    if P2[j-tl][1]-P2[i-tl][1]>min_dis:
                        break
                    min_dis=min(min_dis, dis(P2[i-tl],P2[j-tl]))
            return min_dis
        
    pro(0,n-1)
    print(min_dis)
main()
