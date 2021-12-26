#print("".join(map(str,sorted(list(map(int,input())),reverse=True))))




"""
from sys import stdin as si
coor = (list(map(int,si.readline().split())) for i in range(int(si.readline())))
coor = sorted(coor,key=lambda x:(x[0],x[1]))
print("\n".join(list(str(c[0])+" "+str(c[1]) for c in coor)))



from sys import stdin as si
n=int(si.readline())
num=[int(si.readline()) for i in range(n)]
num.sort()
c = [0]*n
long_len=0; long_i=0; check=0
for i in range(1,n):
    c[i] = 0 if num[i]!=num[i-1] else c[i-1]+1
    if long_len==c[i] and check==0:
        check=1; long_i=i
    if long_len < c[i]:
        long_len=c[i]; check=0; long_i=i;
print("{:.0f}".format(sum(num)/n))
print(num[n//2])
print(num[long_i])
print(max(num)-min(num))



from sys import stdin as si
n=int(si.readline())
word=list(set([si.readline().rstrip() for i in range(n)]))
word.sort(key=lambda x : (len(x),x))
print("\n".join(word))




from sys import stdin, stdout
stdout.write("\n".join(list(map(str,sorted([int(stdin.readline()) for i in range(int(input()))])))))




from sys import stdin as si, stdout as so
coor = (list(map(int,si.readline().split())) for i in range(int(si.readline())))
coor = sorted(coor,key=lambda x:(x[1],x[0]))
so.write("\n".join(list(str(c[0])+" "+str(c[1]) for c in coor)))




from sys import stdin as si, stdout as so
user=[[i]+si.readline().split() for i in range(int(input()))]
so.write("\n".join([(i[1]+" "+i[2]) for i in sorted(user,key=lambda x:(int(x[1]),x[0]))]))



from sys import stdin as si, stdout as so
n=int(input())
x=list(map(int,si.readline().strip().split()))
y=sorted(list(zip(range(n),x)),key=lambda t:t[1])
cnt=0
x2=[-1]*n
for i in range(n):
    if i>0 and y[i][1]!=y[i-1][1]:
        cnt+=1
    x2[y[i][0]]=str(cnt)
so.write(" ".join(x2))


"""

from sys import stdin as si, stdout as so
x=[0]*10001
n = int(input())
i = 0
while i < n:
    x[int(si.readline())]+=1
    i+=1
i = 0
while i<=10000:
    j = 0
    while j < x[i]:
        so.write(str(i)+"\n")
        j+=1
    i+=1

