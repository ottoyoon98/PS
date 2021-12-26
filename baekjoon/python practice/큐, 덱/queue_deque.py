"""
from sys import stdin as si, stdout as so
queue=[]
front=rear=0
for _ in range(int(si.readline())):
    inst=si.readline().split()
    if inst[0]=="push":
        queue.append(inst[1])
        rear+=1
    elif inst[0]=="pop":
        if front==rear:
            so.write("-1\n")
        else:
            so.write(str(queue[front])+"\n")
            front+=1
    elif inst[0]=="size":
        so.write(str(rear-front)+"\n")
    elif inst[0]=="empty":
        so.write(str(0 if rear>front else 1)+"\n")
    elif inst[0]=="front":
        so.write(str(-1 if rear==front else queue[front])+"\n")
    elif inst[0]=="back":
        so.write(str(-1 if rear==front else queue[rear-1])+"\n")



n=int(input())
queue = list(range(1,n+1))
front=0
rear=n
check=1
while rear-front!=1:
    if check:
        front+=1
    else:
        queue.append(queue[front])
        rear+=1
        front+=1
    check=1-check
print(queue[front])





from sys import stdout as so
n,k=map(int,input().split())
queue=list(range(1,n+1))
front=0
answer=[]
for i in range(n):
    for j in range(k-1):
        queue.append(queue[front])
        front+=1
    answer.append(queue[front])
    front+=1
    if front > 1000:
        queue=queue[front:]
        front=0
so.write("<"+", ".join(list(map(str,answer)))+">")



for _ in range(int(si.readline())):
    n,m = map(int,si.readline().split())
    queue=list(zip(list(map(int,si.readline().split())),list(range(n))))
    front=0
    cnt=[0]*10
    for x in queue:
        cnt[x[0]]+=1

    order=1
    check=False
    for i in range(9,0,-1):
        while cnt[i]>0:
            if queue[front][0]==i:
                if queue[front][1]==m:
                    check=True
                    break
                front+=1
                order+=1
                cnt[i]-=1
            else:
                queue.append(queue[front])
                front+=1        
        if check:
            break
    print(order)



from sys import stdin as si, stdout as so
from collections import deque
d = deque()
for _ in range(int(si.readline())):
    inst=si.readline().split()
    if inst[0]=="push_front":
        d.appendleft(int(inst[1]))
    elif inst[0]=="push_back":
        d.append(int(inst[1]))
    elif inst[0]=="pop_front":
        so.write(str(d.popleft() if len(d) else -1)+"\n")
    elif inst[0]=="pop_back":
        so.write(str(d.pop() if len(d) else -1)+"\n")
    elif inst[0]=="size":
        so.write(str(len(d))+"\n")
    elif inst[0]=="empty":
        so.write(str(0 if len(d) else 1)+"\n")
    elif inst[0]=="front":
        so.write(str(d[0] if len(d) else -1)+"\n")
    elif inst[0]=="back":
        so.write(str(d[-1] if len(d) else -1)+"\n")





from sys import stdin as si, stdout as so
from queue import Queue
n,m=map(int, si.readline().split())
que = Queue()
for i in range(1,n+1):
    que.put(i)
cnt=0
for target in map(int, si.readline().split()):
    size=que.qsize()
    t=0
    while True: 
        temp=que.get()
        if temp==target:
            break
        que.put(temp)
        t+=1
    cnt+=min(t,size-t)
print(cnt)




from sys import stdin as si, stdout as so
for _ in range(int(si.readline())):
    inst=si.readline().strip()
    n = int(si.readline())
    A=[0]+list(si.readline().strip("[]\n").split(','))
    if inst.count('D')>n:
        so.write("error\n")
        continue
    front=1
    rear=n
    state=True
    for x in inst:
        if x=='R':
            state=not state
        elif x=='D':
            if state:
                front+=1
            else:
                rear-=1
    if state:
        answer = A[front:rear+1]
    else:
        answer = A[rear:front-1:-1]
    so.write('['+",".join(answer)+']\n')


"""
