"""
a,b,c=map(int,input().split())
print(a//(c-b)+1 if c>b else -1)



x=int(input())
y=x
for i in range(1,x+2):
    if y <= i:
        if i%2: print("{0}/{1}".format(i-y+1,y))
        else: print("{0}/{1}".format(y,i-y+1))
        break
    y-=i
    


import math
a,b,v = map(int,input().split())
print(math.ceil((v-a)/(a-b))+1)



for t in range(int(input())):
    H, W, N = map(int,input().split())
    print("{}{:02}".format(N%H if N%H!=0 else H,(N-1)//H+1))



import math
for t in range(int(input())):
    k,n = int(input()),int(input())
    print(math.comb(k+n,k+1))
    


n=int(input())
print(max({i+(n-3*i)//5 for i in range(5) if n-3*i>=0 and (n-3*i)%5==0}|{-1}))


"""

b,a = input()[::-1].split()
i = 0
n = max(len(a),len(b))+1
ans=[0]*n
i = 0
while True:
    if i > len(a) and i > len(b):
        break
    else:
        ans[i] += (0 if i >= len(a) else ord(a[i])-ord('0')) + (0 if i >= len(b) else ord(b[i])-ord('0'))
        if ans[i]>9:
            ans[i]-=10
            ans[i+1]+=1
    i+=1
print(int("".join(map(str,ans[::-1]))))
