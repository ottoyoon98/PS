"""
from sys import stdin as si, stdout as so
n=int(si.readline())
A=list(map(int,si.readline().split()))
m=int(si.readline())
B=list(map(int,si.readline().split()))
A.sort()
for x in B:
    l=0
    r=n-1
    check=False
    while l <= r:
        m=(l+r)//2
        if A[m]==x:
            check=True
            break
        elif A[m] < x:
            l=m+1
        else:
            r=m-1
    so.write("1\n" if check else "0\n")


"""


#si = open('input.txt', 'r')
#so = open('output.txt', 'w')
from sys import stdin as si
from sys import stdout as so
n=int(si.readline().strip())
A=sorted(list(map(int, si.readline().split())))
m=int(si.readline().strip())
B=list(map(int, si.readline().split()))
A2={}
cnt=1; pre=A[0]
for x in A[1:]:
    if pre!=x:
        A2[pre]=cnt
        pre=x
        cnt=1
    else:
        cnt+=1
A2[pre]=cnt
for x in B:
    k=A2.get(x)
    so.write(str(k) if k!=None else "0")
    so.write(" ")
si.close()