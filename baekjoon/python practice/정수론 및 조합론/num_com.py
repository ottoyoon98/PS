"""
from sys import stdin as si, stdout as so
while True:
    a,b=map(int,si.readline().split())
    if (a,b)==(0,0):
        break
    if b%a==0:
        so.write("factor\n")
    elif a%b==0:
        so.write("multiple\n")
    else:
        so.write("neither\n")





n=int(input())
A=list(map(int,input().split()))
A.sort()
print(A[0]*A[n-1]) 



def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)
a,b=map(int,input().split())
T = gcd(max(a,b),min(a,b))
print(T)
print(a*b//T)




def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)
for _ in range(int(input())):
    a,b=map(int,input().split())
    T = gcd(max(a,b),min(a,b))
    print(a*b//T)







from sys import stdin as si, stdout as so
def gcd(a,b):
    return b if a%b==0 else gcd(b,a%b)
n=int(si.readline())
num=[int(si.readline()) for _ in range(n)]
num.sort()
dis=((num[i+1]-num[i]) for i in range(n-1))
GCD=num[1]-num[0]
for x in dis:
    GCD = gcd(GCD, x)
x=2
factor=[]
while True:
    cnt=0
    while GCD%x==0:
         GCD//=x
         cnt+=1
    factor.append([x,cnt])
    x+=1
    if GCD==1:
        break
M=[1]
for E in factor:
    empty=[]
    for t in M:
        v=1
        for k in range(1,E[1]+1):
            v*=E[0]
            empty.append(t*v)
    M+=empty
M.sort()
so.write(" ".join(list(map(str,M))[1:]))





def GCD(a,b):
    return b if a%b==0 else GCD(b,a%b)
n = int(input())
R = list(map(int, input().split()))
A=B=1
for i in range(n-1):
    A*=R[i]
    B*=R[i+1]
    gcd=GCD(A,B)
    A//=gcd
    B//=gcd
    print("{}/{}".format(A,B))






n,k=map(int,input().split())
A=B=1
for i in range(k):
    A*=(n-i)
    B*=(i+1)
print(A//B)





def GCD(a,b):
    return b if a%b==0 else GCD(b,a%b)
n,k=map(int,input().split())
A=B=1
for i in range(k-1,-1,-1):
    A*=(n-i)
    B*=(i+1)
    gcd = GCD(A,B)
    A//=gcd
    B//=gcd
print((A//B)%10007)




from sys import stdin as si, stdout as so
for _ in range(int(si.readline())):
    n,m=map(int,si.readline().split())
    a=b=1
    for i in range(n):
        a*=(m-i)
        b*=(i+1)
    so.write(str(a//b)+"\n")





from sys import stdin as si
for _ in range(int(si.readline())):
    n = int(si.readline())
    Item = dict()
    for i in range(n):
        C = si.readline().split()
        Item[C[1]]= (0 if Item.get(C[1])==None else Item.get(C[1]))+1
    answer=1
    for x in Item.values():
        answer*=(x+1)
    answer-=1
    print(answer)





cnt=0
for i in range(5,int(input())+1,5):
    x = i
    while x%5==0:
        cnt+=1
        x//=5
print(cnt)



"""

n,m=map(int,input().split())
cnt1=0
cnt2=0
x=5
while n>=x:
    cnt1+=(n//x)-(m//x)-((n-m)//x)
    x*=5
x=2
while n>=x:
    cnt2+=(n//x)-(m//x)-((n-m)//x)
    x*=2
print(min(cnt1,cnt2)) 
