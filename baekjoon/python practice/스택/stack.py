"""
from sys import stdin as si, stdout as so
stack=[]
for _ in range(int(si.readline())):
    inst=si.readline().split()
    if inst[0]=='push':
        stack.append(inst[1])
    else:
        temp=0
        if inst[0]=='pop':
            temp = -1 if not len(stack) else stack.pop()
        elif inst[0]=='size':
            temp = len(stack)
        elif inst[0]=='empty':
            temp = 1 if not len(stack) else 0
        elif inst[0]=='top':
            temp = -1 if not len(stack) else stack[len(stack)-1]
        so.write(str(temp)+"\n")



from sys import stdin as si
stack=[]
for _ in range(int(si.readline())):
    num=int(si.readline())
    if num==0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))




from sys import stdin as si, stdout as so
for _ in range(int(si.readline())):
    ps=si.readline().strip()
    stack=[]
    check=True
    for x in ps:
        if x=='(':
            stack.append(x)
        else:
            if not len(stack):
                check=False
                break
            else:
                stack.pop()
    if len(stack):
        check=False
    so.write("YES\n"if check else "NO\n")







from sys import stdin as si, stdout as so
while True:
    line = si.readline().rstrip()
    if line[0]=='.' and len(line)==1:
        break
    check=True
    stack=[]
    for x in line:
        if x=='[':
            stack.append(x)
        elif x=='(':
            stack.append(x)
        elif x==')':
            if len(stack)==0 or stack[len(stack)-1]!='(':
                check=False
                break
            else:
                stack.pop()
        elif x==']':
            if len(stack)==0 or stack[len(stack)-1]!='[':
                check=False
                break
            else:
                stack.pop()
    if len(stack):
        check=False
    so.write("yes\n" if check else "no\n")




from sys import stdin as si, stdout as so
stack=[]
check=True
ans = []
nextN=1
n=int(si.readline())
for _ in range(n):
    k=int(si.readline())
    while nextN <= k:
        stack.append(nextN)
        ans.append('+')
        nextN+=1
    if stack[-1]==k:
        stack.pop()
        ans.append('-')
    else:
        check=False
        break
so.write("\n".join(ans) if check else "NO")
"""

"""
from sys import stdin as si, stdout as so
n = int(si.readline())
A = list(map(int,si.readline().split()))
stack=[]
NGE=['-1']*n
for i in range(n):
    #pop
    while True:
        if len(stack)==0 or stack[-1][1]>=A[i]:
            break
        p = stack.pop()
        NGE[p[0]]=str(A[i])
    #push
    stack.append((i,A[i]))
so.write(" ".join(NGE))
"""

A=list(map(int,input().split()))
S=0
for i in A:
    S+=(i*i)
print(S%10)
