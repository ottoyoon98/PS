"""
n = int(input())
for i in range(1, 10):
    print("{} * {} = {}".format(n,i,n*i))


n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(a+b)


n = int(input())
sum = 0
for i in range(n+1):
    sum += i
print(sum)


"""

"""
import sys
n = int(sys.stdin.readline())
ls = ['']*n
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    ls[i] = str(a+b)
sys.stdout.write('\n'.join(ls))


from sys import stdin as si, stdout as so
n = int(si.readline())
for i in range(n,0,-1):
    so.write(str(i)+"\n")


import sys
n = int(sys.stdin.readline())
for i in range(n):
    a,b = map(int, sys.stdin.readline().split())
    sys.stdout.write("Case #{}: {} + {} = {}\n".format(i+1,a,b,a+b))

import sys
n = int(sys.stdin.readline())
for i in range(1,n+1):
    sys.stdout.write(" "*(n-i)+"*"*i+"\n")

"""
import sys
n,x = map(int,sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
ls = []
for num in nums:
    if num < x:
        ls.append(str(num))
sys.stdout.write(" ".join(ls))
