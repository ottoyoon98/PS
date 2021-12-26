"""
n,m = map(int,input().split())
card = list(map(int,input().split()))
max=0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            if max < card[i]+card[j]+card[k] and card[i]+card[j]+card[k] <= m:
                max = card[i]+card[j]+card[k]
print(max)




n = int(input())
print(min([i for i in range(max(0,n-len(str(n))*9),n+1) if i+sum(map(int,str(i)))==n]or[0]))




n=int(input())
player=[]
for i in range(n):
    player.append(list(map(int, input().split())))
rank =[]
for a in player:
    rank.append(len(list(b for b in player if a[0]<b[0] and a[1]<b[1]))+1)
print(" ".join(map(str,rank)))




def compare(s, t):
    return [c1 == c2 for c1, c2 in zip(s,t)].count(True)
n,m=map(int,input().split())
s=("WBWBWBWB"+"BWBWBWBW")*4
board=[]
for i in range(n):
    board.append(input())
minV = 64
for i in range(n-7):
    for j in range(m-7):
        t=""
        for k in range(8):
            t+=board[i+k][j:j+8]
        a = compare(s,t)
        b = 64-a
        minV = min(a,64-a,minV)
print(minV)


k = 0
i = 666
n = int(input())
while True:
    if str(i).find("666")!=-1:
        k+=1
        if k==n:
            break
    i+=1
print(i)



num=[]
for i in range(10000):
    for j in range(1000):
        num.append(int(str(i*1000+j)+"666"))
        num.append(int("666"+str(i*1000+j)))
        num.append(int(str(i)+"666"+str(j)))
num=set(num)
num=list(num)
num.sort()
print(num[int(input())-1])

"""
