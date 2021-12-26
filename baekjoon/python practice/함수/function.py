"""
def solve(a: list):
    sum = 0
    for num in a:
        sum += num
    return sum

"""

"""
import sys
def selfnumber():
    self = [1]*10001
    for i in range(1,10001):
        if self[i]==0:
            continue
        N=i
        while True:
            nextN = N
            while N>0:
                nextN+=N%10
                N//=10
                
            if nextN > 10000:
                break
            if self[nextN]==0:
                break
            self[nextN]=0
            N = nextN
    for i in range(1,10001):
        if self[i]==1:
            sys.stdout.write(str(i)+"\n")
    return

selfnumber()



r=range(9999)
print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))
"""

def isAP(num):
    return 1 if len({num[i]-num[i-1] for i in range(1,len(num))})<=1 else 0
print(len(list(n for n in range(1,int(input())+1) if isAP(list(map(int,str(n)))))))
